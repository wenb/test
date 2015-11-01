import os,sys
import xml.dom.minidom
from  xml.dom.minidom import Document
def search(folder, filter, allfile):
    folders = os.listdir(folder)
    for name in folders:
        curname = os.path.join(folder, name)
        isfile = os.path.isfile(curname)
        if isfile:
            ext = os.path.splitext(curname)[1]
            count = filter.count(ext)
            if count>0:
                cur = myfile()
                cur.name = curname
                allfile.append(cur)
        else:
            search(curname, filter, allfile)
    return allfile

class myfile:
    def __init__(self):
        self.name = ""

def generate(allfile, xml):
    doc = Document()
    root = doc.createElement("root")
    doc.appendChild(root)
    for myfile in allfile:
        file = doc.createElement("file")
        root.appendChild(file)
        name = doc.createElement("name")
        file.appendChild(name)
        namevalue = doc.createTextNode(myfile.name)
        name.appendChild(namevalue)
    print doc.toprettyxml(indent="")
    f = open(xml, 'a+')
    f.write(doc.toprettyxml(indent=""))
    f.close()

def GenerateXml(caseDir,fileName):

  impl = xml.dom.minidom.getDOMImplementation()
  dom = impl.createDocument(None, 'TestCases', None)
  root = dom.documentElement  
#  employee = dom.createElement('employee')
 # root.appendChild(employee)
  folders = os.listdir(caseDir)
  for i in folders:  
      case = dom.createElement('case')
      casename = dom.createTextNode(i)
      case.appendChild(casename)
      root.appendChild(case)
  
#  ageE=dom.createElement('age')
#  ageT=dom.createTextNode('30')
#  ageE.appendChild(ageT)
#  employee.appendChild(ageE)
  

  f= open('%s.xml'%fileName, 'w')
  dom.writexml(f, addindent='  ', newl='\n',encoding='utf-8')
  f.close()  

GenerateXml(sys.argv[1],sys.argv[2])



#if __name__ == '__main__':
  #  folder = "/home/cts_tester/fMBT/testCases/autoBZ/TestCases/Medfield/"
   # filter = [".html",".htm",".php"]
    #allfile = []
    #allfile = search(folder, filter, allfile)
   # leng = len(allfile)
#    print "found: " + str(leng) + " files"
 #   xml = "folder.xml"
 #   generate(allfile, xml)


