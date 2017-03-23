#DATE 2017-2-23
#AUTHOR lijun (lijun11@METERSBONWE.COM)

command -v sar >/dev/null 2>&1 || { echo >&2 "I require sar but it's not installed.  Aborting."; exit 1; }

strfilename=""

if [ ! -d "report" ]; then
    mkdir -p "report"
fi

function recordwoparameters()
{
  cnt=0
  lastip=$(ifconfig eth0 | grep "inet addr" | awk '{ print $2}' | awk -F: '{print $2}'|awk -F. '{print $4}')
  date=$(date "+%Y%m%d_%H%M%S")
  gc_cnt=$(ls report/tps*.log|wc -l)

  #zip and delete old tps log file
  if [ $gc_cnt -gt 0 ];
  then
    #do nothingdd
    echo "正在压缩历史日志"
    zip -r tps.zip report/tps*.log
    echo "正在删除历史日志"
    rm -rf report/tps*.log
  fi

  #retrieve tps process and output jvm gc log
  export LC_TIME="POSIX"
  strfilename=tps_$lastip"_"$date.log
  sar -b $1 $2 >> report/$strfilename
#  tac $strfilename| sed 1d | tac  | awk '{print $2}'
  sed '1,3d' report/$strfilename > report/tps_temp.log
  tac report/tps_temp.log| sed 1d | tac  | awk '{print $1,$2}' > report/$strfilename
  rm -f report/tps_temp.log
}

if test -z $2
then
  #  echo "tps.sh 缺少文件操作数"
  #  echo "用法： tps.sh 记录总数 每次记录间隔时间"
  #  echo "举个栗子：tps.sh 1 10"
  #  echo "说明：以1秒间隔总共记录10次"
  echo "以1秒间隔记录，总计60次，持续1分钟。"
  recordwoparameters 1 60
else
  recordwoparameters $1 $2
fi

exit 0

