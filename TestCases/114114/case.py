import fmbtandroid

# def exe_():
    d = fmbtandroid.Device()
    d.enableVisualLog("htmlLog")
    d.setBitmapPath("TestCase/MRD8/114114")
    d.pressPower(long='True')
    d.refreshScreenshot()
    d.refreshView()
    d.tapOcrText("Power off")