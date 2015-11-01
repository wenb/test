import os,sys
import xml.dom.minidom
from  xml.dom.minidom import Document


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

  f= open('%s.xml'%fileName, 'w')
  dom.writexml(f, addindent='  ', newl='\n',encoding='utf-8')
  f.close()  
  
if __name__ == '__main__':
  GenerateXml(sys.argv[1],sys.argv[2])