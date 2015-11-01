#!/usr/bin/env python

import fmbtandroid

#def exe_():
    d = fmbtandroid.Device()
    d.enableVisualLog("htmllog")
    d.setBitmapPath("TestCases/MRD8/Flashing_113847")
    d.pressPower(long='True')
    d.refreshScreenshot()
    d.refreshView()
    try:
        assert waitBitmap("Power off.png"),"[Flashing]failed:power off"
    except AssertionError:
        return "[Flashing]failed:power off"
    else:
        return "Pass"

        