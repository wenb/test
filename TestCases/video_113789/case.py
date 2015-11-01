import fmbtandroid
import time

#def exe_():
    d = fmbtandroid.Device()
    d.enableVisualLog("htmllog")
    d.setBitmap("TestCases/MRD8/video_113789")
    d.shell("am start -n com.android.gallery3d/com.android.camera.CameraLauncher")
    d.refreshScreenshot()
    d.refreshView()
    d.tap((0.13, 0.96))
    d.tap((0.17, 0.80))
    d.tap((0.52, 0.94))
    time.sleep(5)
    d.refreshScreenshot()
    d.tap((0.50, 0.93))
    time.sleep(14.5)
    d.refreshScreenshot()
    d.shell("am start -n com.android.gallery3d/.app.Gallery")
    d.refreshScreenshot()
    time.sleep(9.1)
    d.refreshScreenshot()
    d.tap((0.25, 0.24))
    try:
        assert d.waitBitmap("recorded video.png")."[video]Fail:record fail"
    except AssertionError:
        return "[video]Fail:record fail"
    else:
        return "Pass"




