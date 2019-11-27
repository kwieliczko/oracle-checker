# oracle-checker
Queries databases for parameters and places the result in Excel or an Oracle table.


First, set up a set of tables using the queries available in the .sql file

The source of the program's information is a table with a list of hosts and access parameters to all our databases.


 ID HOST_NAME                DB_PO DB_SERVICE_NAME   DB_USER     DB_PASSWORD ::
 -- ----------------------   ----- ----------------  ---------   -------------
 01 dbhost001.domain.com     1523  hr                dbsnmp      password     
 02 dbhost002.domain.com     1521  crm               dbsnmp      password     
 03 dbhost003.domain.com     1521  sales             dbsnmp      password     
 04 dbhost004.domain.com     1521  db_sap            dbsnmp      password  
  

In addition, there is also a table with queries that we want to query all our databases (you can enter everything that returns the values we are interested in: database size, number of processors, revision number, version etc.).

It is recommended to run the program cyclically with the --sql parameter to create a history of changes in size and parameters in the examined databases.

If we run the program with the --xls parameter, then the current data was saved in an Excel file (for further manual processing of the type charts or presentations)
