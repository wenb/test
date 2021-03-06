import fmbtandroid
import time

def exe_():
    d = fmbtandroid.Device()
    d.enableVisualLog("htmlLog")
    d.setBitmapPath("TestCase/MRD8/Camera_1.3059443E7")
    d.shell("am start -n com.android.gallery3d/com.android.camera.CameraLauncher")
    d.refreshScreenshot()
    d.refreshView()
    d.tap((0.53, 0.93))
    try:
        assert d.waitBitmap("pic-taken.png"),"[Graphic]fail:no pic taken"
    except AssertionError:
        return "[Graphic]fail:no pic taken"
    d.shell("am start -n com.android.gallery3d/.app.Gallery")
    d.refreshScreenshot()
    d.tap((0.27, 0.24))
    time.sleep(2)
    d.tap((0.20, 0.24))
    d.refreshScreenshot()
    try:
        assert d.waitBitmap("pic grid view.png"),"[Graphic]fail:gallery not opened"
     except AssertionError:
        return "[Graphic]fail:gallery not opened"
    else:
        return "Pass"

result = exe_()
print result
