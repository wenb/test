#!/usr/bin/env python

import fmbtandroid

#def exe():
    d = fmbtandroid.Device()
    d.enableVisualLog("htmlLog")
    d.setBitmapPath("TestCases/MRD8/Audio_11070425")
    d.pressSearch()
    d.refreshScreenshot()
    d.tap((0.90, 0.09))

