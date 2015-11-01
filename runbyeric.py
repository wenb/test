#!/usr/bin/env python

import os,time,traceback
import csv
from xml.etree import ElementTree

def add_csv_result(FileName,CaseName,CaseResult):
	f=csv.writer(file(FileName,'ab'))
	f.writerow([CaseName,CaseResult])



cases = []
start_time = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))
result_dir = "/home/chenwen/testautomation/Result"+start_time


tcRoot = ElementTree.parse("/home/chenwen/testautomation/testcases.xml")
cn = tcRoot.findall("case")
for i in cn:
	cases.append(i.text)
caseList = list(set(cases))
caseList.sort(key=cases.index)
title = ['CaseNames','Verify_result']
resultcsv = result_dir+start_time+".csv"
csv_results = open(resultcsv,"wb")
f_csv = csv.writer(csv_results)
f_csv.writerow(title)
#f_csv.close()


for caseName in caseList:
	print caseName
	case_result_dir = result_dir+"/"+caseName
	os.popen("mkdir -p %s"%(case_result_dir))
	try:
		os.sys.path.append('/home/chenwen/testautomation/TestCases/')
		a = __import__('%s.case' %caseName)
		reload(a.case)
	except ImportError, e:
		print "can't find case:", caseName
		continue
	f = open(case_result_dir+"/"+caseName+".txt","aw")
	try:
		result = a.case.exe()
		print result
		if type(result) ==str:
			add_csv_result(resultcsv,caseName,result)		
	except Exception, e:
		print Exception, ':',e
		traceback.print_exc(file=f)
		f.flush()
		f.close()
	else:
		f.writer("No expection Rise\n")
		f.close()	
	finally:
		f.close()
	os.popen("adb pull /mnt/sdcard/log %s/logs_adb"%(result_dir))
	os.popen("adb pull /logs %s/crashLogs"%(result_dir))

