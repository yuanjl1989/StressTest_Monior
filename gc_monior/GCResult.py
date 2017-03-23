#-*- coding: UTF-8 -*-
#!/usr/bin/python
__author__ = 'Yiming'

import os,sys,shutil
import linecache

from common import *
reload(sys)
sys.setdefaultencoding("utf-8")
from prettytable import PrettyTable  

#定义输入的日志路径
fpath = os.path.join(os.path.dirname(os.path.abspath("__file__")), "logs")
#定义文字输出的表格title
x = PrettyTable(["File", "YGC Valid", "YGC SUM", "YGC Frequency", "YGC Over >50ms", "FGC Valid", "FGC SUM", "FGC Frequency", "FGC Over >1s", "P/M Area Monitor"])

#输出成网页格式
def generate_tr(file, ygcv, ygc, ygcf, ygcot, fgcv, fgc, fgcf, fgcot, pmc):
    if (ygcv == 1 and fgcv == 0):
        if (float(ygcf) > float(0.5) and float(fgcf) > float(2)):  #如果大于0.5，表格输出时标红
            return '<tr><td align="left" width="150px" style="word-wrap:break-word;">%s</td><td style="color:red">无效</td><td>%s</td><td style="color:red">%s</td><td>%s</td><td style="color:green">有效</td><td>%s</td><td  style="color:red">%s</td><td>%s</td><td>%s</td></tr>'%(file, ygc, ygcf, ygcot, fgc, fgcf, fgcot, pmc)
        elif (float(ygcf) > float(0.5) and float(fgcf) < float(2)):  #如果大于0.5，表格输出时标红
            return '<tr><td align="left" width="150px" style="word-wrap:break-word;">%s</td><td style="color:red">无效</td><td>%s</td><td style="color:red">%s</td><td>%s</td><td style="color:green">有效</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'%(file, ygc, ygcf, ygcot, fgc, fgcf, fgcot, pmc)
        elif (float(ygcf) < float(0.5) and float(fgcf) > float(2)):  #如果大于0.5，表格输出时标红
            return '<tr><td align="left" width="150px" style="word-wrap:break-word;">%s</td><td style="color:red">无效</td><td>%s</td><td>%s</td><td>%s</td><td style="color:green">有效</td><td>%s</td><td  style="color:red">%s</td><td>%s</td><td>%s</td></tr>'%(file, ygc, ygcf, ygcot, fgc, fgcf, fgcot, pmc)
        elif (float(ygcf) < float(0.5) and float(fgcf) < float(2)):  #如果大于0.5，表格输出时标红
            return '<tr><td align="left" width="150px" style="word-wrap:break-word;">%s</td><td style="color:red">无效</td><td>%s</td><td>%s</td><td>%s</td><td style="color:green">有效</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'%(file, ygc, ygcf, ygcot, fgc, fgcf, fgcot, pmc)
    elif (ygcv == 1 and fgcv == 1):
        if (float(ygcf) > float(0.5) and float(fgcf) > float(2)):  #如果大于0.5，表格输出时标红
            return '<tr><td align="left" width="150px" style="word-wrap:break-word;">%s</td><td style="color:red">无效</td><td>%s</td><td style="color:red">%s</td><td>%s</td><td style="color:red">无效</td><td>%s</td><td  style="color:red">%s</td><td>%s</td><td>%s</td></tr>'%(file, ygc, ygcf, ygcot, fgc, fgcf, fgcot, pmc)
        elif (float(ygcf) > float(0.5) and float(fgcf) < float(2)):  #如果大于0.5，表格输出时标红
            return '<tr><td align="left" width="150px" style="word-wrap:break-word;">%s</td><td style="color:red">无效</td><td>%s</td><td style="color:red">%s</td><td>%s</td><td style="color:red">无效</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'%(file, ygc, ygcf, ygcot, fgc, fgcf, fgcot, pmc)
        elif (float(ygcf) < float(0.5) and float(fgcf) > float(2)):  #如果大于0.5，表格输出时标红
            return '<tr><td align="left" width="150px" style="word-wrap:break-word;">%s</td><td style="color:red">无效</td><td>%s</td><td>%s</td><td>%s</td><td style="color:red">无效</td><td>%s</td><td  style="color:red">%s</td><td>%s</td><td>%s</td></tr>'%(file, ygc, ygcf, ygcot, fgc, fgcf, fgcot, pmc)
        elif (float(ygcf) < float(0.5) and float(fgcf) < float(2)):  #如果大于0.5，表格输出时标红
            return '<tr><td align="left" width="150px" style="word-wrap:break-word;">%s</td><td style="color:red">无效</td><td>%s</td><td>%s</td><td>%s</td><td style="color:red">无效</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'%(file, ygc, ygcf, ygcot, fgc, fgcf, fgcot, pmc)
    elif (ygcv == 0 and fgcv == 0):
        if (float(ygcf) > float(0.5) and float(fgcf) > float(2)):  #如果大于0.5，表格输出时标红
            return '<tr><td align="left" width="150px" style="word-wrap:break-word;">%s</td><td style="color:green">有效</td><td>%s</td><td style="color:red">%s</td><td>%s</td><td style="color:green">有效</td><td>%s</td><td  style="color:red">%s</td><td>%s</td><td>%s</td></tr>'%(file, ygc, ygcf, ygcot, fgc, fgcf, fgcot, pmc)
        elif (float(ygcf) > float(0.5) and float(fgcf) < float(2)):  #如果大于0.5，表格输出时标红
            return '<tr><td align="left" width="150px" style="word-wrap:break-word;">%s</td><td style="color:green">有效</td><td>%s</td><td style="color:red">%s</td><td>%s</td><td style="color:green">有效</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'%(file, ygc, ygcf, ygcot, fgc, fgcf, fgcot, pmc)
        elif (float(ygcf) < float(0.5) and float(fgcf) > float(2)):  #如果大于0.5，表格输出时标红
            return '<tr><td align="left" width="150px" style="word-wrap:break-word;">%s</td><td style="color:green">有效</td><td>%s</td><td>%s</td><td>%s</td><td style="color:green">有效</td><td>%s</td><td  style="color:red">%s</td><td>%s</td><td>%s</td></tr>'%(file, ygc, ygcf, ygcot, fgc, fgcf, fgcot, pmc)
        elif (float(ygcf) < float(0.5) and float(fgcf) < float(2)):  #如果大于0.5，表格输出时标红
            return '<tr><td align="left" width="150px" style="word-wrap:break-word;">%s</td><td style="color:green">有效</td><td>%s</td><td>%s</td><td>%s</td><td style="color:green">有效</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'%(file, ygc, ygcf, ygcot, fgc, fgcf, fgcot, pmc)
        

#打开一个文件作为网页输出对象
f = open(os.path.join(os.getcwd(),'gc_monior_report.html'),'w+')
f.write("<html><body><table class=\"gridtable\"><tr><th rowspan=\"2\">文件</th><th colspan=\"4\">Young GC</th><th colspan=\"4\">Full GC</th><th rowspan=\"2\">永久区变化</th></tr><tr><th>YGC监控有效性</th><th>YoungGC数</th><th>YoungGC频率</th><th>超时的YoungGC数</th><th>FGC监控有效性</th><th>FullGC数</th><th>FullGC频率</th><th>超时的FullGC数</th></tr>")
f.close()

#遍历log文件夹
for parent,dirnames,filenames in os.walk(fpath): 
    for filename in filenames:

        YGC_last = -1
        YGCT_last = -1
        FGC_last = -1
        FGCT_last = -1
        #YGCOT, FGCOT : GC happend times in one monitor period
        YGCOT = int(0)
        FGCOT = int(0)
        
        YGC = int(0)
        FGC = int(0)
        
        YGC_breach_flag = int(0) #在监控间隔时间内发生多次时记录标记位
        FGC_breach_flag = int(0)
        
        YGC_count = int(0)
        FGC_count = int(0)
        YGC_exceed = int(0)
        FGC_exceed = int(0)
        
        P_last = -1
        P_interval = float(0) #整个监控时段P的增长值
        P_change_flag = int(0) #flag if P changed.

        # Read specific line
        line = linecache.getline(os.path.join(parent,filename), 1)
        f = open(os.path.join(parent,filename),"r")
        
        # JVM 1.7 scenario, the No.4 is P, stands for Permenant 
        if (line.split()[4] == "P"):
            lines = f.readlines()
            total = len(lines)/2 #计算采样数
            totalhour = float(total)/float(3600)
            for line in lines:
                #Filter "S0" column
                if not line.startswith('  S0'):
                    #Read Young GC and Full GC record from line...
                    YGC = int(' '.join(line.split()).split(" ",10)[5])
                    FGC = int(' '.join(line.split()).split(" ",10)[7])
                    P = float(' '.join(line.split()).split(" ",10)[4])
                    #print YGC
                    #If YGC value changed, read YGCT value from line
                    if (YGC_last != -1):
                        #Read YGCT from line ...
                        YGCT = ' '.join(line.split()).split(" ",10)[6]
                        YGCOT = YGC - YGC_last
                        
                        #Check if YGC changed
                        if (YGCOT == int(1)):
                            YGCT_interval = float(YGCT) - float(YGCT_last)
                            #print YGCT_interval
                            #If YGCT interval > 50ms, then print. 
                            if (YGCT_interval > float(0.5)):
                                #print "No." + str(YGC_count) +" Young GC interval:" + str(YGCT_interval)
                                YGC_exceed = YGC_exceed + 1
                            YGC_count = YGC_count + 1
                            #print YGC_count
                            YGCT_last = YGCT
                            YGC_last = YGC
                        elif (YGCOT > int(1)):
                            #YGC_occurred_times_in_circle = YGC - YGC_last
                            YGC_count = YGC_count + YGCOT

                            #printYellow(u'YGC happened ' + str(YGCOT) + ' times in monitor period.\n')
                            YGC_breach_flag = 1
                            #print (u'\033[1;35m YGC happened " + str(YGCOT) + " times in monitor period. \033[0m!9')
                            YGCT_last = YGCT
                            YGC_last = YGC

                    if (YGC_last == -1):
                        YGC_last = YGC
                        YGCT_last= ' '.join(line.split()).split(" ",10)[6]
                        FGC_last =  FGC
                        FGCT_last =  ' '.join(line.split()).split(" ",10)[8]
                        P_last = P
                        
                    if (FGC_last != -1):
                        #print FGC_last
                        #Read GCT from line ...
                        FGCT =  ' '.join(line.split()).split(" ",10)[8]
                        FGCOT = FGC - FGC_last
                        if (FGCOT == (1)):
                            FGCT_interval = float(FGCT) - float(FGCT_last)
                            
                            #If FGCT interval > 1s, then print. 
                            if (FGCT_interval > float(1)):
                                #print "No." + str(FGC_count) +" Full GC interval:" + str(GCT_interval)
                                FGC_exceed = FGC_exceed + 1
                            FGC_count = FGC_count +1
                            FGCT_last = FGCT
                            FGC_last = FGC
                        elif (FGCOT > int(1)):
                            FGC_count = FGC_count + FGCOT
                            FGC_breach_flag = 1
                            #printYellow (u'FGC happened ' + str(FGCOT) + ' times in monitor period.\n')
                            FGCT_last = FGCT
                            FGC_last = FGC
                    if (P != -1):
                        if (P != P_last):
                            P_interval = P - P_last
                            P_change_flag = 1

            x.add_row([filename,YGC_breach_flag,str(YGC_count),str(float(YGC_count)/float(total)),str(YGC_exceed),FGC_breach_flag,str(FGC_count),str(float(FGC_count)/float(totalhour)),str(FGC_exceed),str(P_last)+"%->"+str(P)+"%"])
            f = open(os.path.join(os.getcwd(),'gc_monior_report.html'),'a+')
            f.write(generate_tr(filename,YGC_breach_flag,str(YGC_count),str(float(YGC_count)/float(total)),str(YGC_exceed),FGC_breach_flag,str(FGC_count),str(float(FGC_count)/float(totalhour)),str(FGC_exceed),str(P_last)+"%->"+str(P)+"%"))
            f.write('\n')
            f.close()
        elif (line.split()[4] == "M"):
            lines = f.readlines()
            total = len(lines)/2
            totalhour = float(total)/float(3600)
            for line in lines:
                #Filter "S0" column
                if not line.startswith('  S0'):
                    #Read Young GC and Full GC record from line...
                    YGC = int(' '.join(line.split()).split(" ",10)[6])
                    FGC = int(' '.join(line.split()).split(" ",10)[8])
                    P = float(' '.join(line.split()).split(" ",10)[4])
                    #print YGC
                    #If YGC value changed, read YGCT value from line
                    if (YGC_last != -1):
                        #Read YGCT from line ...
                        YGCT = ' '.join(line.split()).split(" ",10)[7]
                        YGCOT = YGC - YGC_last
                        
                        #Check if YGC changed
                        if (YGCOT == int(1)):
                            YGCT_interval = float(YGCT) - float(YGCT_last)
                            
                            #If YGCT interval > 50ms, then print. 
                            if (YGCT_interval > float(0.5)):
                                #print "No." + str(YGC_count) +" Young GC interval:" + str(YGCT_interval)
                                YGC_exceed = YGC_exceed + 1
                            YGC_count = YGC_count + 1
                            #print YGC_count
                            YGCT_last = YGCT
                            YGC_last = YGC
                        elif (YGCOT > int(1)):
                            #YGC_occurred_times_in_circle = YGC - YGC_last
                            YGC_count = YGC_count + YGCOT
                            YGC_breach_flag = 1
                            #printYellow(u'YGC happened ' + str(YGCOT) + ' times in monitor period.\n')
                            YGCT_last = YGCT
                            YGC_last = YGC

                    if (YGC_last == -1):
                        YGC_last = YGC
                        YGCT_last= ' '.join(line.split()).split(" ",10)[7]
                        FGC_last =  FGC
                        FGCT_last =  ' '.join(line.split()).split(" ",10)[9]
                        P_last = P
                    if (FGC_last != -1):
                        #Read GCT from line ...
                        FGCT =  ' '.join(line.split()).split(" ",10)[9]
                        
                        FGCOT = FGC - FGC_last
                        if (FGCOT == (1)):
                            FGCT_interval = float(FGCT) - float(FGCT_last)
                            
                            #If FGCT interval > 1s, then print. 
                            if (FGCT_interval > float(1)):
                                #print "No." + str(FGC_count) +" Full GC interval:" + str(FGCT_interval)
                                FGC_exceed = FGC_exceed + 1
                            FGC_count = FGC_count +1

                            FGCT_last = FGCT
                            FGC_last = FGC

                        elif (FGCOT > int(1)):
                            FGC_count = FGC_count + FGCOT
                            FGC_breach_flag = 1
                            #printYellow(u'FGC happened ' + str(FGCOT) + ' times in monitor period.\n')
                            FGCT_last = FGCT
                            FGC_last = FGC
                    if (P != -1):
                        if (P != P_last):
                            P_interval = P - P_last
                            P_change_flag = 1


            x.add_row([filename,YGC_breach_flag,str(YGC_count),str(float(YGC_count)/float(total)),str(YGC_exceed),FGC_breach_flag,str(FGC_count),str(float(FGC_count)/float(totalhour)),str(FGC_exceed),str(P_last)+"%->"+str(P)+"%"])
            f = open(os.path.join(os.getcwd(),'gc_monior_report.html'),'a+')
            f.write(generate_tr(filename,YGC_breach_flag,str(YGC_count),str(float(YGC_count)/float(total)),str(YGC_exceed),FGC_breach_flag,str(FGC_count),str(float(FGC_count)/float(totalhour)),str(FGC_exceed),str(P_last)+"%->"+str(P)+"%"))
            f.write('\n')
            f.close()
    f = open(os.path.join(os.getcwd(),'gc_monior_report.html'),'a+')
    f.write("</table></body></html><style type=\"text/css\">table.gridtable{font-family: verdana,arial,sans-serif;font-size:11px;color:#333333;border-width: 1px;border-color: #666666;border-collapse: collapse;}table.gridtable th {border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #dedede;}table.gridtable td {border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;}body{font-size:12px; line-height:24px;}.exp1{font: 32px/1.5 Tahoma,Helvetica,Arial,'黑体',sans-serif;text-align:center;}.exp2{font: 22px/1.5 Tahoma,Helvetica,Arial,'黑体',sans-serif;text-align:center;}.exp3{font: 18px/1.5 Tahoma,Helvetica,Arial,'黑体',sans-serif;text-align:left;}.exp4{font: 14px/1.5 Tahoma,Helvetica,Arial,'黑体',sans-serif;text-align:left;}.exp5{font-size:larger;}.exp6{font-size:smaller;}.exp7{font-size:50%;}.exp8{font-size:150%;}.ui.table {border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #dedede;}.ui.table th, .ui.table td {padding: 4px 3px 1px 3px;border-width: 1px 0;border-style: solid;text-align: center;}.ui.table th {font-weight: bold;}.ui.table.center th, .ui.table.center td {padding-right: 10px;text-align: center;}.ui.table.celled th, .ui.table.celled td {border-left-width: 1px;}.ui.table td.info, .ui.table td.success, .ui.table td.warning, .ui.table td.error {border-left-width: 2px;}.ui.table tfoot th, .ui.table tfoot{text-align: left;}.ui.table th, .ui.table td {border-color: #E7E7E7;}.ui.table th {background: #F2F2F2;}.ui.table tfoot th {background: #F7F7F7;}.ui.table td.info {border-left-color: #4D8796;background: #E6F4F9;}.ui.table td.success {border-left-color: #52A954;background: #DEFCD5;}.ui.table td.warning {border-left-color: #96904D;background: #F6F3D5;}.ui.table td.error {border-left-color: #A95252;background: #F1D7D7;}.ui.table.celled td.inner-table{ padding:0; }.ui.table.celled td.inner-table table{ border:none; width: 100%}.ui.table.celled td.inner-table td{ border-left:none; border-right:none; border-top:none; }.ui.table.celled td.inner-table tr:last-child td{ border:none; }</style>")
    f.write("<p>使用方式:<br>1.先看监控有效性，如果显示为无效，则说明GC发生频率大于采样频率，GC频率过高，可对JVM内存调优，如多个服务部署在同一台服务器上需进行拆分。<br>2.如果监控有效，则查看频率值是否高亮为红色，如是则说明GC频率过高，(YGC为<0.5次/秒，FGC为<2次/时。)<br>3.如以上都没有问题则查看超时的GC数，正常该数应为0，反之则说明有个别GC回收时间超过标准值(YGC<50ms,FGC<1s)。<br>4.最后观察永久区变化，正常应无变化，如有变化需多次压测观察值有下降(发生GC回收)。</p>")
    f.close()
    print " "
    print "Results: "
    print x
    print u"输出网页格式到同级目录，文件名为gc_monior_report.html，请查收！"