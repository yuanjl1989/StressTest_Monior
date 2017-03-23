echo "开始清空gcanalyzer/logs内容"
path=$(cd `dirname $0`;pwd)
cd $path
rm -rf logs/*
echo "清空操作已完成"
echo "开始从各压测环境中拉取gc log文件"
scp -r 10.101.1.114:/home/stress/gc_*.log /home/stress/gcanalyzer/logs/
scp -r 10.101.1.116:/home/stress/gc_*.log /home/stress/gcanalyzer/logs/
#scp -r 10.101.1.84:/home/stress/gclogger/gc_*.log /home/stress/gcanalyzer/logs/
echo "拉取操作已完成"
echo "开始分析日志文件并生成html报告"
python GCResult.py
echo "报告已生成，文件路径为："$path"/gc_monior_report.html"