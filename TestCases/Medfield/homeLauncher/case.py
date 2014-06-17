import fmbtandroid
import os
def exe_():
	os.system("adb kill-server")
	os.system("adb devices")
	d = fmbtandroid.Device()
	d.pressHome()
	d.setBitmapPath("TestCases/Medfield/homeLauncher/")
	d.refreshScreenshot()
	try:
    		assert d.waitBitmap("home-icon.png"),"Fail: xxxxxxxfail."
	except AssertionError:
		return "[AutoUITest]xxxxxxfail."
	else:
		return "pass"		
#result = exe_()
#print result
#l = result+"\n"
#print [l,"abc"+"\n","123"]
