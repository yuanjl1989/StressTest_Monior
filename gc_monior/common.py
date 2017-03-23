__author__ = 'Yiming'

#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,sys,shutil

##---------------------Common file---------------------
def ReadFileAsList(strFile):
	file=open(strFile,"r")
	listLine=file.readlines()
	file.close()
	return listLine