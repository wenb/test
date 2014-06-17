import fmbtandroid
import os
def exe_():
    
	os.system("adb kill-server")
	os.system("adb devices")
	d = fmbtandroid.Device()
	d.shell("am start -n com.android.settings/.Settings")  
	d.refreshScreenshot()      
	d.swipe((.5,.8),"north") 
	d.refreshScreenshot()
	d.refreshView()
	d.tapText("Developer options")
	d.refreshScreenshot()
	d.refreshView()
	d.tapText("Stay awake")
    
		
	
#result = exe_()
#print result
#l = result+"\n"
#print [l,"abc"+"\n","123"]
