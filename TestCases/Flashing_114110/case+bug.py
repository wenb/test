import fmbtandroid
import time
import xmlrpclib
import os

def exe_():
   d = fmbtandroid.Device()
   d.enableVisualLog("htmllog")
   d.setBitmapPath("TestCases/MRD8/Flashing_114110")
   d.shell("am start -n com.android.settings/.DateTimeSettingsSetupWizard")
   d.refreshScreenshot()
   d.refreshView()
   d.tap((0.87, 0.09))
   d.reboot()
   time.sleep(15)
   d.swipe((0.51, 0.80), "east", distance=0.92)
   d.shell("am start -n com.android.settings/.DateTimeSettingsSetupWizard")
   d.tap((0.87, 0.09))
   d.refreshScreenshot()
   try:
       assert d.waitBitmap("automatic-time.png"),"[Time]fail:automatic-time"
   except AssertionError:
       return "[Time]fail:automatic-time"
   else:
       return "Pass"

	   
def autobz(Result):
	proxy = xmlrpclib.ServerProxy("http://buildslave03-sh-cts-bd.sh.intel.com/bugzilla/xmlrpc.cgi")
	server = proxy.User.login({'login':'eric.feng@intel.com','password':'123456','restrict_login':'True'})
	if result == "Pass":
		print result
	else:
		proxy.Bug.create({'Bugzilla_login':'eric.feng@intel.com','Bugzilla_password':'123456','product':'TestProduct',\
          'component':'TestComponent','summary':'[Time]fail:automatic-time1','version':'unspecified',\
          'description':'fail:automatic-time','op_sys':'linux','platform':'PC'})

