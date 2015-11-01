import fmbtandroid
import time
def exe():
    d = fmbtandroid.Device()
    d.enableVisualLog("htmllog")
    d.setBitmapPath("TestCases/MRD8/Audio_113650")
    d.shell("am start -n com.android.music/.MusicBrowserActivity")
    d.refreshScreenshot()
    d.refreshView()
    d.tap((0.90, 0.95))
    d.pressVolumeDown()
    d.refreshScreenshot()
    d.pressVolumeUp()
    d.refreshScreenshot()
    time.sleep(3)
    d.tap((0.48, 0.88))
    try:
        assert d.waitBitmap("Music-pause.png"),"[Audio]Fail:no playing"
    except AssertionError:
        return "[Audio]Fail:no playing"
    else:
        return "PASS"

result = exe()
print result
    
    
