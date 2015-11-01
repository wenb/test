#/usr/bin/env python
import fmbtandroid

def exe_():
    d = fmbtandroid.Device()
    d.enableVisualLog("htmllog")
    d.setBitmapPath("TestCases/MRD8/Graphic_113620")
    d.shell("am start -n com.android.gallery3d/com.android.camera.CameraLauncher")
    d.refreshScreenshot()
    d.refreshView()
    try:
        assert d.waitBitmap("Camera-on.png"),"[Camera]failed"
    except AssertionError:
        return "[Camera]failed:no camera"
    else:
        return "Pass"
    d.pressBack()

result = exe_()
print result
