import fmbtandroid
import time

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

result = exe_()
print result