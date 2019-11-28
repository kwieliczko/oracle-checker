#################################################
#									
# 	Created 27-11-2019 by Karol Wieliczko	
#						
#################################################


import logging, sys
from cfg import config
from modules import db_oracle 
from modules import functions 
from builtins import staticmethod
import argparse
from modules import table2Excel

# Runtime class inheriting from GeneralFunctions
class main(functions.GeneralFunctions):
    
    @staticmethod
    def run():
        
        # Enable DEBUG mode
        logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
        
        # Gruments
        parser = argparse.ArgumentParser()
        parser.add_argument("-V", "--version", help="Version", action="store_true")
        parser.add_argument("-X", "--xls", help="Save to Excel", action="store_true")
        parser.add_argument("-Q", "--sql", help="Save to database", action="store_true")
        
        args = parser.parse_args()
        
        if len(sys.argv)==1:
            parser.print_help(sys.stderr)
            sys.exit(1)
        
        if args.version:
            print("Oracle checker version 1.0")
            exit()
            
            
            
        # DbOracle class object
        db = db_oracle.DbOracle()

        
        queries_tab = []
        
        
        # Connection to the main database of the program based on parameters from the 'cfg\config.py' file 
		# to download connection string to the database
        conn_main = db.db_connect(config.Config().host_name, 
                                  config.Config().db_port, 
                                  config.Config().db_service_name, 
                                  config.Config().db_user, 
                                  config.Config().db_password)
        
        
        # Clean the temporary table for Excel
        db.truncate_table_temp(conn_main)
            
        values_from_databases = []  
        
        number_of_records_connecting_strings = db.get_count_of_table(conn_main, 'CONNECTING_STRING')
        
        i = 1
        while i <= number_of_records_connecting_strings:
            
            values_from_databases = []
            
            db_query_connection_strings  = 'SELECT * FROM CONNECTING_STRING where id = ' + str(i)
            connection_string_tab  = db.get_query_result(conn_main, db_query_connection_strings, 6) 
            
            # podlaczenie do baz
            conn_db = db.db_connect(connection_string_tab[1], 
                                    connection_string_tab[2], 
                                    connection_string_tab[3], 
                                    connection_string_tab[4], 
                                    connection_string_tab[5])
            

            
            # Querrys from database            
            number_of_records_queries = db.get_count_of_table(conn_main, 'queries')
            
            
            # Main loop
            j = 1
            while j <= number_of_records_queries :
                db_query_queries = 'select querie from queries where id =' + str(j)
                
                
                queries_tab = db.get_query_from_db(conn_main, db_query_queries)
               
                db.add_to_values_from_databases_tab(values_from_databases, conn_db, queries_tab, 1)
                j = j + 1
                
            print (values_from_databases[1], end="")

            #logging.debug(values_from_databases)
            
            c = 0
            query_insert = ''
            query_insert_temp = '' 
            query_insert = query_insert + 'INSERT INTO VALUES_IN_BASES (data, db_id, db_name, instance_name, db_size, sga_size, pga_size, version, cpu, patch_id, CONTROL_FILE_RECORD_KEEP_TIME  ) VALUES (sysdate, '
            query_insert_temp = query_insert_temp + 'INSERT INTO VALUES_IN_BASES_TEMP (db_id, db_name, instance_name, db_size, sga_size, pga_size, version, cpu, patch_id, CONTROL_FILE_RECORD_KEEP_TIME  ) VALUES ('



            for row in values_from_databases[0:-1]:

                query_insert = query_insert + "'" + str(values_from_databases[c]) + "', "
                query_insert_temp = query_insert_temp + "'" + str(values_from_databases[c]) + "', "

                c = c + 1
                
            # The last element in list
            query_insert = query_insert + "'" + str(values_from_databases[-1]) + "')"
            query_insert_temp = query_insert_temp + "'" + str(values_from_databases[-1]) + "')"
           
            
            # Save to database
            if args.sql:
                db.insert_to_table(conn_main, query_insert)
            
            
            db.insert_to_table(conn_main, query_insert_temp)
               
            query_insert=''
            query_insert_temp=''

            i = i + 1
            
            print ("\t\t\t\t[ OK ]")
        

        # Excel generating
        if args.xls:
            try:
                conn_main.execute('SELECT * FROM values_in_bases_temp')
                table2Excel.write_data_to_excel(conn_main, 'Oracle_db.xls', 'Oracle')
                print("Excel file generated")
            except:
                print("Error generating Excel file")



        # Close connecton  
        conn_main.close()
        conn_db.close()
        print("End")
        


# Running main program
main().run()    



