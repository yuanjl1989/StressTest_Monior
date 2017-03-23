# --------------------------------------------------------------------------+
#                 Generate AWR report and send mail automatically           |
#   Filename: autoawr_by_time.sh                                            |
#   Desc:                                                                   |
#       The script use to generate awr report by timeLength.                |                                 |  
#   Usage:                                                                  |
#       ./autoawr_by_time.sh [timeLength]                                   | 
#   Example:                                                                |
#       ./autoawr_by_time.sh 1
#   Author : Yuanjunlei                                                     | 
# --------------------------------------------------------------------------+
#
# -------------------------------
#  Set environment here 
# ------------------------------

if [ -f ~/.bash_profile ]; then
    . ~/.bash_profile
fi

# ------------------------------------------------------------
#  Check the parameter, if no specify,then use default value
# ------------------------------------------------------------
if [ -z "${1}" ];then
	timeLength='1800'
else
	timeLength=$((${1}*60))
fi
export timeLength
echo $timeLength

export ORACLE_SID='MBOLTP'
export MACHINE=`hostname`
export AWR_DIR=/home/oracle/oracle_monior/report/
RETENTION=31

if [ $MACHINE == 'newerpdb_190' ]; then
	version='11.2.0'
else
	version='10.2.0'
fi
export ORACLE_HOME=/u01/app/oracle/product/${version}/db_1

echo $ORACLE_SID

# --------------------------------------------------------------------
#  Check the directory for store awr report,if not exist, create it
# --------------------------------------------------------------------

if [ ! -d "${AWR_DIR}" ]; then
    mkdir -p ${AWR_DIR}
fi

# ----------------------------------------------
# check if the database is running, if not exit
# ----------------------------------------------

db_stat=`ps -ef | grep pmon_$ORACLE_SID | grep -v grep| cut -f3 -d_`
if [ -z "$db_stat" ]; then
    echo " $ORACLE_SID is not available on ${MACHINE} !!!"
    exit 1
fi;

# ---------------------------------------------
#  Generate the awr report
# ---------------------------------------------
rm -rf ${AWR_DIR}/*
$ORACLE_HOME/bin/sqlplus / as sysdba @./autoawr_by_time.sql $timeLength

status=$?
if [ $status != 0 ];then
    echo " $ORACLE_SID is not available on ${MACHINE} !!!"
    exit
fi

# ------------------------------------------------
# Removing files older than $RETENTION parameter 
# ------------------------------------------------

find ${AWR_DIR} -name "*awrrpt*" -mtime +$RETENTION -exec rm {} \;

exit

