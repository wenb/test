#/usr/bin/env python
import fmbtandroid
import time

def exe_():
    d = fmbtandroid.Device()
    d.enableVisualLog("htmllog")
    d.setBitmapPath("TestCases/MRD8/Android_12877675/")
    d.shell("am start -n com.android.music/.MusicBrowserActivity")
    d.tap((0.92, 0.94))
    d.pressHome()
    d.shell("am start -n com.android.camera/.CameraBrowserActivity")
    time.sleep(2)
    d.shell("am start -n com.android.browser/.BrowserActivity")
    d.refreshScreenshot()
    d.tap((0.43, 0.07))
    d.type("www.yahoo.com")
    d.tap((0.96, 0.95))
    d.pressBack()
    d.shell("am start -n com.android.music/.MusicBrowserActivity")
    d.tap((0.92, 0.94))
    d.tap((0.50, 0.90))
    d.refreshScreenshot()
    d.pressBack()
    try:
        assert d.waitBitmap("music-pause.png"),"[APP Switch]failed"
    except AssertionError:
        return "[APP Switch]failed"
    else:
        return "Pass"

result = exe_()
print result



