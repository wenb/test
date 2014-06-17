import os, time,traceback
from xml.etree import ElementTree

cases = []
start_time = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))
result_dir = "./Result/"+start_time
#os.popen("mkdir -p %s"%(result_dir))


tcRoot = ElementTree.parse("./testCases.xml")
cn = tcRoot.findall("case")
for i in cn:
	cases.append(i.text)
caseList = list(set(cases))
caseList.sort(key=cases.index)



for caseName in caseList:

    case_result_dir= result_dir+"/"+caseName
    os.popen("mkdir -p %s"%(case_result_dir))
    try:
		#from caseName import case
		os.sys.path.append("TestCases/Medfield/")
		a = __import__('%s.case' %caseName)
		reload(a.case)
    except ImportError,e:
	#	print e
		print "Can not find case:  ",caseName
		continue 
# run test case

    f = open(case_result_dir+"/"+caseName+".txt","aw")
    try:
        result = a.case.exe_()
	print result
        if type(result)==str:
	    f.write(result+"\n")
            f.flush()
    except Exception,e:
	
	print Exception,':',e
	traceback.print_exc(file=f)
	f.flush()
	f.close()
    else:
    	f.write("No exception Raise\n")
	f.flush()
	f.close()	
    finally:
	f.close()
    

    os.popen("mv screenshots %s"%(case_result_dir))
    os.popen("mv *html* %s"%(case_result_dir))
os.popen("adb pull /mnt/sdcard/logs %s/logs_adb"%(result_dir))

os.popen("adb pull /logs %s/crashLogs"%(result_dir))
# collect result
#    shortDesc = result
 #   steps = "[steps:  ]"
  #  log = "[Log: ]"
   # list_info = [shortDesc,steps,log]
    
    
#    for i in range(list_info.__len__()):
 #  		f = open(caseName+".txt","aw")
  # 	 	f.write("%s\n" %list_info[i])
   # 		f.close()
