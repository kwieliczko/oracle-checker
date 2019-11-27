----- DDL ---------------------------------------------------------------------

--------------------------------------------------------
--  DDL for Table VALUES_IN_BASES
--------------------------------------------------------

  CREATE TABLE "ORACLECHECKER"."VALUES_IN_BASES" 
   (    "ID" NUMBER GENERATED ALWAYS AS IDENTITY MINVALUE 1 MAXVALUE 9999999999999999999999999999 INCREMENT BY 1 START WITH 1 CACHE 20 NOORDER  NOCYCLE  NOKEEP  NOSCALE , 
    "DATA" DATE, 
    "DB_ID" VARCHAR2(20 BYTE), 
    "DB_NAME" VARCHAR2(20 BYTE), 
    "INSTANCE_NAME" VARCHAR2(20 BYTE), 
    "DB_SIZE" NUMBER, 
    "SGA_SIZE" NUMBER, 
    "PGA_SIZE" NUMBER, 
    "VERSION" VARCHAR2(20 BYTE), 
    "PATCH_ID" NUMBER, 
    "CPU" NUMBER, 
    "CONTROL_FILE_RECORD_KEEP_TIME" NUMBER
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "ORACLECHECKER" ;
  
  
--------------------------------------------------------
--  DDL for Index VALUES_IN_BASES_PK
--------------------------------------------------------

  CREATE UNIQUE INDEX "ORACLECHECKER"."VALUES_IN_BASES_PK" ON "ORACLECHECKER"."VALUES_IN_BASES" ("ID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "ORACLECHECKER" ;
  
  
--------------------------------------------------------
--  Constraints for Table VALUES_IN_BASES
--------------------------------------------------------

  ALTER TABLE "ORACLECHECKER"."VALUES_IN_BASES" MODIFY ("ID" NOT NULL ENABLE);






--------------------------------------------------------
--  DDL for Table CONNECTING_STRING
--------------------------------------------------------

  CREATE TABLE "CONNECTING_STRING" 
   (    "ID" NUMBER(*,0), 
    "HOST_NAME" VARCHAR2(60 BYTE), 
    "DB_PORT" VARCHAR2(5 BYTE), 
    "DB_SERVICE_NAME" VARCHAR2(40 BYTE), 
    "DB_USER" VARCHAR2(40 BYTE), 
    "DB_PASSWORD" VARCHAR2(40 BYTE)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "ORACLECHECKER" ;



--------------------------------------------------------
--  DDL for Table QUERIES
--------------------------------------------------------

  CREATE TABLE "QUERIES" 
   (    "ID" NUMBER(*,0), 
    "QUERIE" VARCHAR2(200 BYTE)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "ORACLECHECKER" ;
  
  
--------------------------------------------------------
--  DDL for Table VALUES_IN_BASES_TEMP
--------------------------------------------------------

  CREATE TABLE "ORACLECHECKER"."VALUES_IN_BASES_TEMP" 
   (    "DB_ID" VARCHAR2(20 BYTE), 
    "DB_NAME" VARCHAR2(20 BYTE), 
    "INSTANCE_NAME" VARCHAR2(20 BYTE), 
    "DB_SIZE" NUMBER, 
    "SGA_SIZE" NUMBER, 
    "PGA_SIZE" NUMBER, 
    "VERSION" VARCHAR2(20 BYTE), 
    "PATCH_ID" NUMBER, 
    "CPU" NUMBER, 
    "CONTROL_FILE_RECORD_KEEP_TIME" NUMBER
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "ORACLECHECKER" ;




-- SQL-s for database queries 

INSERT INTO queries(id, querie) VALUES(1,q'[select dbid from v$database]');
INSERT INTO queries(id, querie) VALUES(2,q'[SELECT name from v$database]');
INSERT INTO queries(id, querie) VALUES(3,q'[select INSTANCE_NAME from V$INSTANCE]');
INSERT INTO queries(id, querie) VALUES(4,q'[select sum(bytes) from dba_segments]');
INSERT INTO queries(id, querie) VALUES(5,q'[SELECT sum(value) FROM v$sga]');
INSERT INTO queries(id, querie) VALUES(6,q'[SELECT value FROM V$PGASTAT WHERE NAME = 'total PGA allocated']');
INSERT INTO queries(id, querie) VALUES(7,q'[select version from v$instance]');
INSERT INTO queries(id, querie) VALUES(8,q'[select value from V$OSSTAT where stat_name = 'NUM_CPUS']');
INSERT INTO queries(id, querie) VALUES(9,q'[select PATCH_ID from DBA_REGISTRY_SQLPATCH]');
INSERT INTO queries(id, querie) VALUES(10,q'[select value from v$parameter where name = 'control_file_record_keep_time']');
commit;

-------------------------------------------------------------------------------------------


-- database inventory
INSERT INTO connecting_string VALUES(1, 'dbhost001.domain.com', 1523, 'hr', 'dbsnmp', 'password');
INSERT INTO connecting_string VALUES(2, 'dbhost002.domain.com', 1521, 'crm', 'dbsnmp', 'password');
INSERT INTO connecting_string VALUES(3, 'dbhost003.domain.com', 1521, 'sales', 'dbsnmp', 'password');
INSERT INTO connecting_string VALUES(4, 'dbhost004.domain.com', 1521, 'db_sap', 'dbsnmp', 'password');
INSERT INTO connecting_string VALUES(5, 'dbhost005.domain.com', 1530, 'hr_tst', 'dbsnmp', 'password');
INSERT INTO connecting_string VALUES(6, 'dbhost006.domain.com', 1531, 'crm_tst', 'dbsnmp', 'password');
commit;





