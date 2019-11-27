import cx_Oracle
from modules import functions 
import inspect

# Oracle class of operations inheriting from GeneralFunctions

class DbOracle(functions.GeneralFunctions):
    
    def db_connect(self,host_name, db_port, db_service_name, db_user, db_password):
        
        try:
            dsn_tns = cx_Oracle.makedsn(host_name, db_port, db_service_name)
            conn=cx_Oracle.connect(user=db_user, password=db_password, dsn=dsn_tns)
            c = conn.cursor()
        except:
            c = ""
            self.print_error("Failed to connect to the database in db_connect. Base:", db_service_name)
        
        return c
    



    def print_query_result(self, con, query, number_of_columns):

        try:
            con.execute(query)
            for row in con:
                print(*row[:number_of_columns])

        except:
            self.print_error("Select failed in print_query_result: ", query)




    def get_query_result(self, con ,query, number_of_columns):
        
        try:
            con.execute(query)
            for row in con:
                return row[:number_of_columns]
            
        except:
            #self.print_error("Select failed in get_query_result: ", query)
            return '0'
            pass
            
            
            
            
    def get_count_of_table(self, con, table):
        
        query_count  = 'select count(*) from ' + table
          
        try:
            con.execute(query_count)
            for row in con:
                return row[0]
            
        except:
            self.print_error("Select failed in get_count_of_table. Table: ", table)
            
            
            
            
    def get_query_from_db(self, con ,query):
        
        
        try:
            con.execute(query)
            for row in con:
                return row[0]
            
        except:
            self.print_error("Select failed in get_query_from_db: ", query)
            
    
    
    
    def insert_to_table(self, con, query_insert):
        try:
            con.execute(query_insert)
            con.execute('commit')
            
        except:
            self.print_error("Insert failed in insert_to_table: ", query_insert)
            
    
    
    
    def truncate_table_temp(self, con):
        try:
            con.execute('truncate table VALUES_IN_BASES_TEMP')
            con.execute('commit')
            
        except:
            self.print_error("Truncate error in truncate_table_temp")
            
            
                
            
            
            
    def add_to_values_from_databases_tab(self, tab, conn_db, query, number_of_columns):
        try:
            tab.extend(self.get_query_result(conn_db, query, number_of_columns))
        except:
            self.print_error("Select failed in add_to_values_from_databases_tab")
            pass
        
            
        