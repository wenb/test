#usr/bin/env python
import fmbtandroid

#def exe_():
    d = fmbtandroid.Device()
    d.wake()
    d.refreshScreenshot()
    d.swipe((0.50, 0.81), "east", distance=0.90)
    d.shell("com.android.gallery3d/com.android.camera.CameraLauncher")
    d.
    
    


    

