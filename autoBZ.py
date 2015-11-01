#/usr/bin/env python

import sys
import xmlrpclib
sys.path.append("..")

def autobz(Result,Product,Component,Summary,Version,Description,Op_sys,Platform):
	proxy = xmlrpclib.ServerProxy("http://buildslave03-sh-cts-bd.sh.intel.com/bugzilla/xmlrpc.cgi")
	server = proxy.User.login({'login':'eric.feng@intel.com','password':'123456','restrict_login':'True'})
	if Result == "Pass":
    	print result
	else:
    	proxy.Bug.create({'Bugzilla_login':'eric.feng@intel.com','Bugzilla_password':'123456',\
    		'product':'Product','component':'Component','summary':'Summary',\
    		'version':'Version','description':'Description','op_sys':'Op_sys','platform':'Platform'})
    	print Result

	