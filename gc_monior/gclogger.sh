if [ -z "${1}" ];then
	sTime=1
	cNum=3600
	echo "以1秒间隔记录，总计3600次，持续1小时。"
else
	sTime=${1}
	cNum=${2}
	echo "以"${1}"秒间隔记录，总计"${2}"次，持续"$((${1}*${2}))"秒。"
fi


cnt=0
lastip=$(ifconfig eth0 | grep "inet addr" | awk '{ print $2}' | awk -F: '{print $2}'|awk -F. '{print $4}')
date=$(date "+%Y%m%d_%H%M%S")
gc_cnt=$(ls|grep gc_*.log|wc -l)

if (($gc_cnt > 0));
then
  echo "正在压缩历史日志"
  zip -r gc.zip gc*.log
  echo "正在删除历史日志"
  rm -rf gc*.log
fi

while (($cnt < $cNum))
do
  while read locations;
  do
    jid=$(ps -ef|grep $locations|grep -v grep|awk '{print $2}')
    jstat -gcutil $jid >> gc_$lastip"_"$locations"_"$date.log
    echo "第" $[$cnt+1] "次记录，路径为:" $locations "，进程ID为:" $jid
  done < locations.csv
  let "cnt++"
  sleep $sTime
done
