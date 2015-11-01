import fmbtandroid

def exe_():
    d = fmbtandroid.Device()
    d.enableVisualLog("htmlog")
    d.setBitmapPath("TestCase/MRD8/Graphic_113698")
    d.shell("am start -n  com.android.gallery3d/com.android.camera.CameraLauncher")
    d.refreshScreenshot()
    d.refreshView()
    d.tap((0.86, 0.93),)
    d.refreshScreenshot()
    time.sleep(1)
    d.tap((0.52, 0.31))
    d.refreshScreenshot()
    d.tap((0.51, 0.93))
    d.shell("am start -n com.android.gallery3d/.app.Gallery")
    d.refreshScreenshot()
    d.refreshScreenshot()
    d.tap((0.26, 0.24))
    d.tap((0.19, 0.22), hold=1.4)
    try:
        assert d.waitBitmap("selected picture.png"),"[Pic]no pic selected"
    except AssertionError:
        return "[Pic]no pic selected"
    d.refreshScreenshot()
    d.tap((0.93, 0.07))
    d.refreshScreenshot()
    time.sleep(10.6)
    d.refreshScreenshot()time.sleep(17.5)
    d.refreshScreenshot()
    d.tap((0.00, 0.44))
    d.tap((0.71, 0.46))
    d.refreshScreenshot()
    time.sleep(5)
    d.tap((0.69, 0.46))
    d.tap((0.92, 0.09))
    d.pressHome()
    d.refreshScreenshot()
    time.sleep(3)
    d.swipe((0.85, 0.72), "west", distance=1.00)
    time.sleep(3)
    d.refreshScreenshot()
    d.swipe((0.84, 0.38), "west", distance=0.69)
    try:
        assert d.waitBitmap("setting wallpaper.png"),"[failed]can't set wallpaper"
    except AssertionError:
        return "[failed]can't set wallpaper"
    else:
        return "Pass"
        


