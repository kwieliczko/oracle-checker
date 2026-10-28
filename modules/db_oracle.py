import cx_Oracle
from modules import functions


class DbOracle(functions.GeneralFunctions):
    def db_connect(self, host_name, db_port, db_service_name, db_user, db_password):
        dsn = cx_Oracle.makedsn(host_name, int(db_port), service_name=db_service_name)
        return cx_Oracle.connect(user=db_user, password=db_password, dsn=dsn)

    def get_query_result(self, connection, query, parameters=None):
        with connection.cursor() as cursor:
            cursor.execute(query, parameters or {})
            row = cursor.fetchone()
            if row is None:
                raise ValueError("Zapytanie nie zwrocilo zadnego wiersza: " + query)
            return row[0]

    def get_connections(self, connection):
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, host_name, db_port, db_service_name, db_user, db_password FROM connecting_string ORDER BY id")
            return cursor.fetchall()

    def get_queries(self, connection):
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, querie FROM queries ORDER BY id")
            return cursor.fetchall()

    def insert_to_table(self, connection, table_name, values):
        if table_name not in ("VALUES_IN_BASES", "VALUES_IN_BASES_TEMP"):
            raise ValueError("Niedozwolona tabela: " + table_name)
        columns = ("db_id", "db_name", "instance_name", "db_size", "sga_size",
                   "pga_size", "version", "cpu", "patch_id", "control_file_record_keep_time")
        placeholders = ", ".join(":" + name for name in columns)
        names = ", ".join(columns)
        if table_name == "VALUES_IN_BASES":
            query = f"INSERT INTO {table_name} (data, {names}) VALUES (SYSDATE, {placeholders})"
        else:
            query = f"INSERT INTO {table_name} ({names}) VALUES ({placeholders})"
        parameters = dict(zip(columns, values))
        with connection.cursor() as cursor:
            cursor.execute(query, parameters)

    def truncate_table_temp(self, connection):
        with connection.cursor() as cursor:
            cursor.execute("TRUNCATE TABLE VALUES_IN_BASES_TEMP")
