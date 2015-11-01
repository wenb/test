#usr/bin/env python

import fmbtandroid
import time
def exe_():
    d = fmbtandroid.Device()
    d.enableVisualLog("htmllog")
    d.setBitmapPath("TestCases/MRD8/CWS_113629")
    d.shell("am start -n com.android.browser/.BrowserActivity")
    d.refreshScreenshot()
    d.refreshView()
    d.tap((0.24, 0.08))
    d.type("www.yahoo.com")
    d.tap((0.95, 0.96))
    d.refreshScreenshot()
    time.sleep(2)
    d.pressBack()
    try:
        assert d.waitBitmap("wlan-on.png"),"[wlan]failed"
    except AssertionError:
        return "[wlan]failed"
    else:
        return "Pass"
    

result = exe_()
print result
