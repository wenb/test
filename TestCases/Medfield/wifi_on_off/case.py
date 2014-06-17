import fmbtandroid
import os
def exe_():
    
	os.system("adb kill-server")
	os.system("adb devices")
	d = fmbtandroid.Device()
	d.enableVisualLog("htmllog")
        d.setBitmapPath("TestCases/Medfield/wifi_on_off")
	d.shell("am start -n com.android.settings/.Settings")  
	d.refreshScreenshot()      
	d.refreshView()
	d.tapText("Wi-Fi")
	d.refreshScreenshot()	
	if(d.waitBitmap("wifi-off.png")):
		d.tapBitmap("wifi-off.png")
		try:
			assert d.waitBitmap("wifi-on.png"), "[Wi-Fi]Fail:wifi on/off" 
		except AssertError:
			return "[Wi-Fi]Fail:wifi on/off"
		else:
			return "PASS"


	elif(d.waitBitmap("wifi-on.png")):
    		d.tapBitmap("wifi-on.png")
		try:
			assert d.waitBitmap("wifi-off.png"), "[Wi-Fi]Fail:wifi on/off" 
		except AssertError:
			return "[Wi-Fi]Fail:wifi on/off"
		else:
			return "PASS"	
	
	
#result = exe_()
#print result
#l = result+"\n"
#print [l,"abc"+"\n","123"]
