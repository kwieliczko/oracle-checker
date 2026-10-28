import argparse
import logging
from cfg.config import Config
from modules.db_oracle import DbOracle
from modules import table2Excel

EXPECTED_VALUES = 10


def run():
    parser = argparse.ArgumentParser(description="Oracle Checker")
    parser.add_argument("-V", "--version", action="store_true", help="Wersja")
    parser.add_argument("-X", "--xls", action="store_true", help="Eksport do XLS")
    parser.add_argument("-Q", "--sql", action="store_true", help="Zapis historii do Oracle")
    args = parser.parse_args()
    if args.version:
        print("Oracle Checker 1.1")
        return
    if not (args.xls or args.sql):
        parser.print_help()
        return

    db = DbOracle()
    cfg = Config()
    try:
        main_conn = db.db_connect(cfg.host_name, cfg.db_port, cfg.db_service_name,
                                  cfg.db_user, cfg.db_password)
    except Exception:
        logging.exception("Nie mozna polaczyc sie z centralna baza")
        return

    try:
        connections = db.get_connections(main_conn)
        queries = db.get_queries(main_conn)
        if len(queries) != EXPECTED_VALUES:
            raise ValueError(f"Oczekiwano {EXPECTED_VALUES} zapytan w QUERIES, znaleziono {len(queries)}")
        # TRUNCATE wykonuje implicit COMMIT w Oracle; pozostaje jak w oryginale.
        db.truncate_table_temp(main_conn)
        for record in connections:
            db_id, host, port, service, user, password = record
            target_conn = None
            try:
                target_conn = db.db_connect(host, port, service, user, password)
                values = [db.get_query_result(target_conn, sql) for _, sql in queries]
                # Najpierw tabela tymczasowa, potem opcjonalnie historia.
                db.insert_to_table(main_conn, "VALUES_IN_BASES_TEMP", values)
                if args.sql:
                    db.insert_to_table(main_conn, "VALUES_IN_BASES", values)
                main_conn.commit()
                print(f"{service} [OK]")
            except Exception:
                main_conn.rollback()
                logging.exception("Blad sprawdzania bazy ID=%s, service=%s", db_id, service)
            finally:
                if target_conn is not None:
                    target_conn.close()
        if args.xls:
            try:
                with main_conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM VALUES_IN_BASES_TEMP")
                    table2Excel.write_cursor_to_excel(cursor, "Oracle_db.xls", "Oracle")
                print("Wygenerowano Oracle_db.xls")
            except Exception:
                logging.exception("Nie udalo sie wygenerowac pliku XLS")
    finally:
        main_conn.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    run()
