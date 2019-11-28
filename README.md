# oracle-checker
### Queries databases for parameters and places the result in Excel or an Oracle table.


First, set up a set of tables using the queries available in the .sql file

The source of the program's information is a table with a list of hosts and access parameters to all our databases.


 ```
 ID HOST_NAME                DB_PO DB_SERVICE_NAME   DB_USER     DB_PASSWORD 
 -- ----------------------   ----- ----------------  ---------   -------------
 01 dbhost001.domain.com     1523  hr                dbsnmp      password     
 02 dbhost002.domain.com     1521  crm               dbsnmp      password     
 03 dbhost003.domain.com     1521  sales             dbsnmp      password     
 04 dbhost004.domain.com     1521  db_sap            dbsnmp      password  
 ```

In addition, there is also a table with queries that we want to query all our databases (you can enter everything that returns the values we are interested in: database size, number of processors, revision number, version etc.).

It is recommended to run the program cyclically with the --sql parameter to create a history of changes in size and parameters in the examined databases.

 ```                                                                                                    
ID    DATA                DB_ID         DB_NAME    DB_SIZE      SGA_SIZE   PGA_SIZE   VERSION     CPU
----- ------------------- -----------   ---------  ----------   ---------- ---------- ----------- --- 
 3303 21-11-2019 20:00:13 2537186398    hr        37219860480   1912602624  118849086  18.0.0.0.0   2 
 3304 21-11-2019 20:00:14 6147797409    crm      118734848000   1593835520  405258920  19.0.0.0.0   2 
 3305 21-11-2019 20:00:15 2935983433    sales     33166393344    687865856  116666638  12.1.0.2.0   2 
 3306 21-11-2019 20:00:15 2239237862    db_sap    41165793346   2471931904  114179950  19.0.0.0.0   4
```

If we run the program with the --xls parameter, then the current data was saved in an Excel file (for further manual processing of the type charts or presentations)
