SET ECHO OFF;
SET VERI OFF;
SET FEEDBACK OFF;
SET TERMOUT ON;
SET HEADING OFF;
SET TRIMSPOOL ON;

VARIABLE rpt_options NUMBER;
DEFINE no_options = 0;

define ENABLE_ADDM = 8;

REM according to your needs, the value can be 'text' or 'html'

DEFINE report_type='html';

BEGIN
   :rpt_options := &no_options;
END;
/

VARIABLE dbid NUMBER;
VARIABLE inst_num NUMBER;
VARIABLE bid NUMBER;
VARIABLE eid NUMBER;

BEGIN
	dbms_workload_repository.create_snapshot();
	SELECT max(snap_id)
	INTO :bid
	FROM dba_hist_snapshot;
		
	DBMS_LOCK.SLEEP('&1');
		
	dbms_workload_repository.create_snapshot();
	SELECT max(snap_id)
	INTO :eid
	FROM dba_hist_snapshot;

SELECT dbid INTO :dbid FROM v$database;
SELECT instance_number INTO :inst_num FROM v$instance;

END;
/


COLUMN ext NEW_VALUE ext NOPRINT
COLUMN fn_name NEW_VALUE fn_name NOPRINT;
COLUMN lnsz NEW_VALUE lnsz NOPRINT;
SELECT 'txt' ext
  FROM DUAL
 WHERE LOWER ('&report_type') = 'text';

SELECT 'html' ext
  FROM DUAL
 WHERE LOWER ('&report_type') = 'html';

SELECT 'awr_report_text' fn_name
  FROM DUAL
 WHERE LOWER ('&report_type') = 'text';

SELECT 'awr_report_html' fn_name
  FROM DUAL
 WHERE LOWER ('&report_type') = 'html';

SELECT '80' lnsz
  FROM DUAL
 WHERE LOWER ('&report_type') = 'text';

SELECT '1500' lnsz
  FROM DUAL
 WHERE LOWER ('&report_type') = 'html';

set linesize &lnsz;
COLUMN report_name NEW_VALUE report_name NOPRINT;

--SELECT instance_name||'_awrrpt_'||'&1'||'.'||'&ext'
SELECT 'oracle_monior_report.'||'&ext'
          report_name
  FROM v$instance a,
       (SELECT TO_CHAR (begin_interval_time, 'yyyymmdd') timestamp
          FROM dba_hist_snapshot
         WHERE snap_id = :bid) b;

SET TERMOUT OFF;
SPOOL ${AWR_DIR}/&report_name;
--SPOOL &report_name

SELECT output
  FROM TABLE (DBMS_WORKLOAD_REPOSITORY.&fn_name (:dbid,
                                                 :inst_num,
                                                 :bid,
                                                 :eid,
                                                 :rpt_options));
SPOOL OFF;
SET TERMOUT ON;
CLEAR COLUMNS SQL;
TTITLE OFF;
BTITLE OFF;
REPFOOTER OFF;
SET TRIMSPOOL OFF;

UNDEFINE report_name
UNDEFINE report_type
UNDEFINE fn_name
UNDEFINE lnsz
UNDEFINE no_options
exit; 

