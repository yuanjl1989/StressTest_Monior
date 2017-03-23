min=1
sTime=$1
cNum=$2

while [ $min -le $cNum ]
do
	echo '----------------Current Time：'`date '+%Y-%m-%d %H:%M:%S'`'--------Current Number：'$min'----------------'
	python mysql_monior.py
	if [ $min -lt $cNum ]; then
		sleep ${sTime}s
	fi
    min=`expr $min + 1`
done

file_input_1='mysql_monior_res_general.txt'
file_input_2='mysql_monior_res_cache.txt'
file_input_3='mysql_monior_res_slow.txt'
file_input_4='mysql_monior_res_other.txt'
file_output='report/mysql_monior_report.html'

td_str=''

if [ ! -d "report" ]; then
    mkdir -p "report"
fi

function create_html_head(){
    echo -e "<html>
        <body style='font-family: 微软雅黑;font-size: 15px;'>
		<style>
		table{border-collapse:collapse;font-size: 15px;}
		table th{border:1px solid;background-color:#E8E8E8;text-align:center; }
		table td{border:1px solid;text-align:center; }
		</style>
        <h1>MYSQL监控报告</h1>"
}

function create_table_head(){
    echo -e "<table border="1">"
}

function create_td(){
#    if [ -e ./"$1" ]; then
        #echo $1
        td_str=`echo $1 | awk 'BEGIN{FS=", "}''{i=1; while(i<=NF) {print "<td>"$i"</td>";i++}}'`
        #echo $td_str
#    fi
}

function create_li(){
#    if [ -e ./"$1" ]; then
        general_str=`echo $1 | awk 'BEGIN{FS=", "}''{i=1; while(i<=NF) {print "<li>"$i"</li>";i++}}'`
        echo $general_str
#    fi
}

function create_tr(){
    create_td "$1"
    echo -e "<tr>
        $td_str
    </tr>" >> $file_output
}

function create_table_end(){
    echo -e "</table>"
}

function create_html_end(){
    echo -e "</body></html>"
}


function create_html(){
    rm -rf $file_output
    touch $file_output

    create_html_head >> $file_output
	
    echo "<br/><li><b>一般信息</b></li><br/>"  >> $file_output
	
	echo `head -1 mysql_monior_res.txt` | awk 'BEGIN{FS=", "}''{i=1; while(i<=NF) {print "<span>"$i"</span><br/>";i++}}' >> $file_output
	rm -rf mysql_monior_res.txt
	
	echo "<br/><table><tr><th>取样时间</th><th>每秒Query量</th><th>每秒事务量</th><th>读写比率(%)</th></tr>"  >> $file_output	
    while read line
    do
        create_tr "$line" 
    done < $file_input_1
    create_table_end >> $file_output
	rm -rf $file_input_1
	echo "<ol type=a>
	<li>已使用连接数大于85%时，可考虑增大最大连接数</li>
	<li>读写比例过大或者过小时，皆需关注是否数据库读写存在问题</li>
	</ol>"  >> $file_output
	
	
    echo "<br/><li><b>缓存相关</b></li><br/><table><tr><th>取样时间</th><th>Buffer命中率(%)</th><th>Query Cache命中率(%)</th><th>Thread Cache命中率(%)</th></tr>"  >> $file_output
    while read line
    do
        create_tr "$line" 
    done < $file_input_2
    create_table_end >> $file_output
	rm -rf $file_input_2
	echo "<ol type=a>
	<li>MyISAM引擎：buffer命中率列显示为buffer读_写命中情况，预期值为99.3% - 99.9%，命中率较低，则可适当增大key_buffer_size的值</li>
	<li>InnoDB引擎：buffer命中率列显示为innodb_buffer_read_hits，预期值为96% - 99%，命中率较低，表明innodb类型表的读写存在问题</li>
	<li>对于一些用户数不高或一次性统计平台建议关闭查询缓存；若开启，Query Cache命中率越高越好</li>
	<li>Thread cache命中率能直接反应出系统参数thread_cache_size设置是否合理。命中率大于90%才算合理，该缓存强烈建议开启。</li>
	</ol>"	 >> $file_output

	echo "<br/><li><b>慢查询与锁信息</b></li><br/><table><tr><th>取样时间</th><th>慢查询</th><th>无主键联合查询</th><th>全表扫描/总查询量(%)</th><th>锁等待/立即释放(%)</th><th>Innodb行锁最大时间(s)</th><th>InnoDB死锁</th></tr>"  >> $file_output
    while read line
    do
        create_tr "$line" 
    done < $file_input_3
    create_table_end >> $file_output
	rm -rf $file_input_3
	echo "<ol type=a>
	<li>慢查询、无主键联合查询、全表扫描/总查询量持续增加，表明需要优化、缺乏必要的索引或其他问题，可通过慢查询日志进行调查</li>
	<li>锁等待/立即释放锁的比值应小于1%，超过该值时，则需重点关注</li>
	<li>Innodb行锁最大时间一般建议设置为10秒。这个值太大的话，可以考虑调低innodb_lock_wait_timeout值</li>
	<li>InnoDB死锁若为True，可通过show engine innodb status \G;调查具体原因</li>
	</ol>"  >> $file_output
	
	echo "<br/><li><b>其他监控</b></li><br/><table><tr><th>取样时间</th><th>当前打开表数量/总打开表数量(%)</th><th>临时表磁盘占比(%)</th><th>Binlog cache磁盘占比(%)</th><th>Innodb_log_waits量</th><th>表扫描率</th></tr>"  >> $file_output
    while read line
    do
        create_tr "$line" 
    done < $file_input_4
    create_table_end >> $file_output
	rm -rf $file_input_4
	echo "<ol type=a>
	<li>当前打开表数量/总打开表数量的比值不应低于85%，小于该值可考虑增大table_open_cache</li>
	<li>临时表磁盘占比的比例超过10%，则需考虑调大tmp_table_size参数，建议tmp_table_size与max_heap_table_size设置成一样；但设置过大可能会导致OOM</li>
	<li>Binlog cache磁盘占比若不为0，说明binlog_cache不够用，需适当增大</li>
	<li>innodb_log_waits直接反应innodb log buffer空间不足造成等待的次数，若不为0，可适当增大innodb_log_buffer_size的值</li>
	<li>表扫描率超过4000，说明进行了太多表扫描，很有可能索引没有建好，增加read_buffer_size值会有一些好处，但最好不要超过8MB</li>
	</ol>"  >> $file_output
	
    create_html_end >> $file_output
}

create_html