#!/usr/bin/python
# -*- encoding: utf8 -*-

from __future__ import division
import MySQLdb, random, datetime, time, os, sys
import ConfigParser
import string, os, sys

host = '127.0.0.1'
user = 'root'
password = ''
db = ''

#----------------------------------------------------------------------
def getConn(host, user, passwd, db='', port=3306, charset=''):
  try:
    conn = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db, port=port, charset=charset)
    return conn
  except MySQLdb.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

#----------------------------------------------------------------------
def closeConn(conn):
  """close mysql connection"""
  conn.close()

#----------------------------------------------------------------------
def getValue(conn, query):
  """ get value of query """
  cursor = conn.cursor()
  cursor.execute(query)
  result = cursor.fetchone()
  return int(result[1])

def getValue1(conn, query):
  """ get value of query """
  cursor = conn.cursor()
  cursor.execute(query)
  result = cursor.fetchone()
  return result[1]  
  
def getQuery(conn, query):
  """ get more queries """
  cursor = conn.cursor()
  cursor.execute(query)
  result = cursor.fetchall()
  return result

#当前使用的引擎 
Storage_engine = "show variables like 'storage_engine%';"
Max_connections = "show variables like 'max_connections';"
Max_used_connections = "show global status like 'Max_used_connections';"
#Questions：每秒钟获得的查询数量
Questions = "show global status like 'Questions'"
Uptime = "show global status like 'Uptime'"
Com_commit = "show global status like 'Com_commit'"
Com_rollback = "show global status like 'Com_rollback'"
Key_reads = "show global status like 'Key_reads'"
Key_read_requests = "show global status like 'Key_read_requests'"
Key_writes = "show global status like 'Key_writes'"
Key_write_requests = "show global status like 'Key_write_requests'"
Have_innodb = "show global variables like 'have_innodb'"
Innodb_buffer_pool_reads = "show global status like 'Innodb_buffer_pool_reads'"
Innodb_buffer_pool_read_requests = "show global status like 'Innodb_buffer_pool_read_requests'"
Qcache_hits = "show global status like 'Qcache_hits'"
Qcache_inserts = "show global status like 'Qcache_inserts'"
Query_cache_size = "show variables like 'query_cache_size'"
Open_tables = "show global status like 'Open_tables'"
Opened_tables = "show global status like 'Opened_tables'"
Thread_cache_size = "show variables like 'thread_cache_size'"
Threads_created = "show global status like 'Threads_created'"
Connections = "show global status like 'Connections'"
Com_select = "show global status like 'Com_select'"
Com_insert = "show global status like 'Com_insert'"
Com_update = "show global status like 'Com_update'"
Com_delete = "show global status like 'Com_delete'"
Com_replace = "show global status like 'Com_replace'"
Table_locks_waited = "show global status like 'Table_locks_waited'"
Table_locks_immediate = "show global status like 'Table_locks_immediate'"
Innodb_row_lock_time_max = "show status like 'Innodb_row_lock_time_max'"
Created_tmp_tables = "show global status like 'Created_tmp_tables'"
Created_tmp_disk_tables = "show global status like 'Created_tmp_disk_tables'"
#Slow_queries：超过该值（--long-query-time）的查询数量，或没有使用索引查询数量。对于全部查询会有小的冲突。如果该值增长，表明系统有性能问题。
Slow_query_log = "show variables like 'slow_query_log'"
Slow_launch_time = "show variables like 'slow_launch_time'"
Slow_query_log_file = "show variables like 'slow_query_log_file'"
Slow_queries = "show global status like 'Slow_queries'"
#Select_full_join：没有主键（key）联合（Join）的执行。该值可能是零。这是捕获开发错误的好方法，因为一些这样的查询可能降低系统的性能。
Select_full_join = "show global status like 'Select_full_join'"
#Select_scan：执行全表搜索查询的数量。在某些情况下是没问题的，但占总查询数量该比值应该是常量（即Select_scan/总查询数量商应该是常数）。如果你发现该值持续增长，说明需要优化，缺乏必要的索引或其他问题。
Select_scan = "show global status like 'Select_scan'"
Binlog_cache_disk_use = "show global status like 'Binlog_cache_disk_use'"
Innodb_log_waits = "show global status like 'innodb_log_waits'"
Handler_read_rnd_next = "show global status like 'Handler_read_rnd_next'"
InnoDB_engine_status = "show engine innodb status"

if __name__ == "__main__":
  conn = getConn(host, user, password, db)
  
  Storage_engine = getValue1(conn, Storage_engine)
  Max_connections = getValue(conn, Max_connections)
  Max_used_connections = getValue(conn, Max_used_connections)
  Questions = getValue(conn, Questions)
  Uptime = getValue(conn, Uptime)
  Com_commit = getValue(conn, Com_commit)
  Com_rollback = getValue(conn, Com_rollback)
  Key_reads = getValue(conn, Key_reads)
  Key_read_requests = getValue(conn, Key_read_requests)
  Key_writes = getValue(conn, Key_writes)
  Key_write_requests = getValue(conn, Key_write_requests)
  Innodb_buffer_pool_reads = getValue(conn, Innodb_buffer_pool_reads)
  Innodb_buffer_pool_read_requests = getValue(conn, Innodb_buffer_pool_read_requests)
  Query_cache_size = getValue(conn, Query_cache_size)
  Qcache_hits = getValue(conn, Qcache_hits)
  Qcache_inserts = getValue(conn, Qcache_inserts)
  Open_tables = getValue(conn, Open_tables)
  Opened_tables = getValue(conn, Opened_tables)
  Thread_cache_size = getValue(conn, Thread_cache_size)
  Threads_created = getValue(conn, Threads_created)
  Connections = getValue(conn, Connections)
  Com_select = getValue(conn, Com_select)
  Com_insert = getValue(conn, Com_insert)
  Com_update = getValue(conn, Com_update)
  Com_delete = getValue(conn, Com_delete)
  Com_replace = getValue(conn, Com_replace)
  Table_locks_immediate = getValue(conn, Table_locks_immediate)
  Table_locks_waited = getValue(conn, Table_locks_waited)
  Innodb_row_lock_time_max = getValue(conn, Innodb_row_lock_time_max)
  Created_tmp_tables = getValue(conn, Created_tmp_tables)
  Created_tmp_disk_tables = getValue(conn, Created_tmp_disk_tables)
  Slow_query_log = getValue1(conn, Slow_query_log)
  Slow_launch_time = getValue1(conn, Slow_launch_time)
  Slow_query_log_file = getValue1(conn, Slow_query_log_file)
  Slow_queries = getValue(conn, Slow_queries)
  Select_full_join = getValue(conn, Select_full_join)
  Select_scan =  getValue(conn, Select_scan)
  Binlog_cache_disk_use = getValue(conn, Binlog_cache_disk_use)
  Innodb_log_waits = getValue(conn, Innodb_log_waits)
  Handler_read_rnd_next = getValue(conn, Handler_read_rnd_next)
  InnoDB_engine_status = getQuery(conn, InnoDB_engine_status)
  
  #print "_____Gerneral Information___________________"
  # QPS = Questions / Seconds
  print "Mysql Storage engine: " + Storage_engine
  QPS = str(round(Questions / Uptime, 5))
  print "QPS (Query per seconds): " + QPS

  # TPS = (Com_commit + Com_rollback ) / Seconds
  TPS = str(round((Com_commit + Com_rollback)/Uptime, 5))
  print "TPS(transactin per seconds): " + TPS
  
  # Read/Writes Ratio
  rwr = str(round((Com_select + Qcache_hits) / (Com_insert + Com_update + Com_delete + Com_replace) * 100, 5))
  print "Read/Writes Ratio(%): " + rwr
  
  #print "_____Cache Usage___________________"
  if(Storage_engine == 'MyISAM'):
  # Key_buffer_read_hits = (1 - Key_reads / Key_read_requests) * 100%
  # Key_buffer_write_hits = (1 - Key_writes / Key_write_requests) * 100%
    if (Key_read_requests <> 0):
       Key_buffer_read_hits = str(round((1 - Key_reads/Key_read_requests) * 100, 5))
    else:
       Key_buffer_read_hits = 'NA'
    print "MyISAM Key buffer read ratio(99.3% - 99.9% target)(%): " + Key_buffer_read_hits
	 
    if (Key_write_requests <> 0):
       Key_buffer_write_hits = str(round((1 - Key_writes/Key_write_requests) * 100, 5))
    else:
       Key_buffer_write_hits = 'NA'
    print "MyISAM Key buffer write ratio(%): " + Key_buffer_write_hits
	 
  # Query_cache_hits = (Qcache_hits / (Qcache_hits + Com_select)) * 100%
  if(Query_cache_size <> 0):
    if ((Qcache_hits + Com_select) <> 0):
       if (Qcache_hits <> 0):
         Query_cache_hits = str(round((Qcache_hits/(Qcache_hits + Com_select)) * 100, 5))
       else:
         Query_cache_hits = '0'
    else:
       Query_cache_hits = 'NA'
  else:
    Query_cache_hits = '未启用Query Cache'
  print "Query cache hits ratio(%): " + Query_cache_hits

  if(Storage_engine == 'InnoDB'):
  # Innodb_buffer_read_hits = (1 - Innodb_buffer_pool_reads / Innodb_buffer_pool_read_requests) * 100%
    Innodb_buffer_read_hits = str(round((1 - Innodb_buffer_pool_reads/Innodb_buffer_pool_read_requests) * 100, 5))
    print "Innodb buffer read ratio(target 96% - 99%)(%): " + Innodb_buffer_read_hits
  
  # Thread_cache_hits = (1 - Threads_created / Connections) * 100%
  #Threads_created创建用来处理连接的线程数。如果Threads_created较大，你可能要增加thread_cache_size值。缓存访问率的计算方法Threads_created/Connections。
  if(Thread_cache_size <> 0):
	Thread_cache_hits = str(round((1-Threads_created / Connections) * 100, 5))
  else:
    Thread_cache_hits = '未启用Thread Cache'
  print "Thread cache hits(Should above 90%)(%): " + Thread_cache_hits
  
  #print "_____Slow Queries(Evil Queries)________________"
  print "Slow queries：" + str(Slow_queries) #查询时间超过 long_query_time秒的查询的个数
  print "Slow full join queries：" + str(Select_full_join) #没有使用索引的联接的数量。如果该值不为0,你应仔细检查表的索引，可以查慢日志。
  print "Select scan：" + str(round(Select_scan/Questions,5)) #对一个表进行完全扫描的联接的数量
  
  #Table_locks_immediate立即获得的表的锁的次数，绝大多数指的是myisam引擎，innodb发生dml时做DDL操作也会发生表锁。
  #Table_locks_waited不能立即获得的表的锁的次数。如果该值较高，并且有性能问题，你应首先优化查询，然后拆分表
  if (Table_locks_immediate <> 0):
	# MyISAM Lock Contention: (Table_locks_waited / Table_locks_immediate) * 100%
	if (Table_locks_waited <> 0):
	  lock_contention = str(round((Table_locks_waited / Table_locks_immediate) * 100, 5))
	else:
	  lock_contention = '0'
  else:
	lock_contention = '立即释放表锁为0'  
  print "MyISAM Lock Contention(<1% good, 1% warning, >3% you are currently dying)(%): " + lock_contention  

  #Innodb_row_lock_current_waits 当前等待行锁的行数。
  #Innodb_row_lock_time 从启动到现在，行锁定花费的总时间，单位毫秒。
  #Innodb_row_lock_time_avg 行锁定的平均时间，单位毫秒。
  #Innodb_row_lock_time_max 行锁定等待的最长时间，单位毫秒（一般建议设置为10秒）。这个值太大的话，可以考虑调低 innodb_lock_wait_timeout 值
  
  if(Storage_engine == 'MyISAM'):
    Innodb_row_lock_time_max = '引擎为MyISAM'	
  else:
    Innodb_row_lock_time_max = str(round(Innodb_row_lock_time_max/1000, 2))
  print "InnoDB row lock time max: (should < 10s)(s)" + Innodb_row_lock_time_max
  
  if('LATEST DETECTED DEADLOCK' in InnoDB_engine_status):
    InnoDB_DEAD_LOCK_status = '存在'
  else:
    InnoDB_DEAD_LOCK_status = '不存在'
  print "InnoDB DEAD LOCK status: " + InnoDB_DEAD_LOCK_status

  #print "_____Others________________"
  #Open_tables 当前正在用打开表空间文件，打开表的数量。如果当前1个表被并发10个线程访问，每个线程打开次数都算1.
  #Opened_tables 历史总共打开次数，如果Opened_tables较大，table_open_cache 值可能太小。
  Open_tables_Opened_tables_ratio = str(round((Open_tables/Opened_tables) * 100, 5))
  print "Open tables/Opened_tables ratio(should >=85%)(%): " + str(Open_tables) + "/" + str(Opened_tables) + "=" + Open_tables_Opened_tables_ratio
  
  if (Created_tmp_tables <> 0):
	Temp_tables_to_disk = '%.5f'%float(str(round((Created_tmp_disk_tables / (Created_tmp_disk_tables + Created_tmp_tables)) * 100, 5)))
  else:
	Temp_tables_to_disk = '未创建临时表'  
  print "Temp tables to Disk ratio(should <=10%)(%): " + Temp_tables_to_disk#高于10%的话,就需要注意,适当调高tmp_table_size,但是不能设置太大,因为它是每个session都会分配的,可能会导致OOM
	
  print "Binlog cache disk use(if not 0, add binlog_cache_size)：" + str( Binlog_cache_disk_use)
  print "Innodb log waits（if not 0, due to  [innodb log buffer] not enough space）：" + str(Innodb_log_waits)
  table_scan_ratio = str(round(Handler_read_rnd_next / Com_select, 5))
  print "table scan ratio（should < 4000）：" + table_scan_ratio + "\n"
  
  f = open("./mysql_monior_res.txt", 'w+')
  f_general = open("./mysql_monior_res_general.txt", 'a+')
  f_cache = open("./mysql_monior_res_cache.txt", 'a+')
  f_slow = open("./mysql_monior_res_slow.txt", 'a+')
  f_other = open("./mysql_monior_res_other.txt", 'a+')
  import datetime
  #获得当前时间
  now = datetime.datetime.now()  #这是时间数组格式
  #转换为指定的格式:
  otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
  
  if(float(80) <= float(rwr) <= float(150)):
    rwr = rwr
  else:
    rwr = "<font color='red'>" + rwr + "</font>"
	
  if(float(lock_contention)>float(1)):
    lock_contention = "<font color='red'>" + lock_contention + "</font>"
  else:
    lock_contention = lock_contention	
	
  if(float(Innodb_row_lock_time_max)>=float(10)):
    Innodb_row_lock_time_max = "<font color='red'>" + Innodb_row_lock_time_max + "</font>"
  else:
    Innodb_row_lock_time_max = Innodb_row_lock_time_max
	
  if(InnoDB_DEAD_LOCK_status == '存在'):
    InnoDB_DEAD_LOCK_status = "<font color='red'>" + InnoDB_DEAD_LOCK_status + "</font>"
  else:
    InnoDB_DEAD_LOCK_status = InnoDB_DEAD_LOCK_status
	
  if(float(Open_tables_Opened_tables_ratio)<float(85)):
    Open_tables_Opened_tables_ratio = "<font color='red'>" + Open_tables_Opened_tables_ratio + "</font>"
  else:
    Open_tables_Opened_tables_ratio = Open_tables_Opened_tables_ratio
	
  if(float(Temp_tables_to_disk)>float(10)):
    Temp_tables_to_disk = "<font color='red'>" + Temp_tables_to_disk + "</font>"
  else:
    Temp_tables_to_disk = Temp_tables_to_disk
	
  if(float(Binlog_cache_disk_use)>float(0)):
    Binlog_cache_disk_use = "<font color='red'>" + str(Binlog_cache_disk_use) + "</font>"
  else:
    Binlog_cache_disk_use = str(Binlog_cache_disk_use)
	
  if(float(Innodb_log_waits)>float(0)):
    Innodb_log_waits = "<font color='red'>" + str(Innodb_log_waits) + "</font>"
  else:
    Innodb_log_waits = str(Innodb_log_waits)
	
  if(float(table_scan_ratio)>=float(4000)):
    table_scan_ratio = "<font color='red'>" + table_scan_ratio + "</font>"
  else:
    table_scan_ratio = table_scan_ratio

  if(Storage_engine == 'MyISAM'):
    if(float(Key_buffer_read_hits)<float(99.3) or float(Key_buffer_write_hits)<float(99.3)):
      Key_buffer_hits = "<font color='red'>" + Key_buffer_read_hits + '_' + Key_buffer_write_hits + "</font>"
    else:
      Key_buffer_hits = Key_buffer_read_hits + '_' + Key_buffer_write_hits
  else:
    if(float(Innodb_buffer_read_hits)<float(96)):
      Innodb_buffer_read_hits = "<font color='red'>" + Innodb_buffer_read_hits + "</font>"
    else:
      Innodb_buffer_read_hits = Innodb_buffer_read_hits
	
  res = '%s, %s, %s, %s, %s' % ('Mysql引擎：' + Storage_engine,'慢查询状态：' + str(Slow_query_log),'慢查询时间阀：' + str(Slow_launch_time) + 's', '日志文件：' + str(Slow_query_log_file),'数据库已使用连接数/最大连接数：' + str(Max_used_connections) + '/' + str(Max_connections) + '=' + str(round((Max_used_connections/Max_connections) * 100, 5)) + '%')
  res_general = '%s, %s, %s, %s' % (otherStyleTime,QPS,TPS,rwr)
  res_slow = '%s, %s, %s, %s, %s, %s, %s' % (otherStyleTime,str(Slow_queries),str(Select_full_join),str(round(Select_scan/Questions,5)),lock_contention,Innodb_row_lock_time_max,InnoDB_DEAD_LOCK_status)
  res_other = '%s, %s, %s, %s, %s, %s' % (otherStyleTime,Open_tables_Opened_tables_ratio,Temp_tables_to_disk,Binlog_cache_disk_use,Innodb_log_waits,table_scan_ratio)	
  
  if(Storage_engine == 'MyISAM'):
    res_cache = '%s, %s, %s, %s' % (otherStyleTime,Key_buffer_hits,Query_cache_hits,Thread_cache_hits)
  else:
    res_cache = '%s, %s, %s, %s' % (otherStyleTime,Innodb_buffer_read_hits,Query_cache_hits,Thread_cache_hits)
	
  print >>f,res
  print >>f_general,res_general
  print >>f_cache,res_cache
  print >>f_slow,res_slow
  print >>f_other,res_other
  
  f.close()
  f_general.close()
  f_cache.close()
  f_slow.close()
  f_other.close()
  closeConn(conn)
