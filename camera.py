#!/usr/bin/env  python
from picamera import PiCamera
import time

camera = PiCamera()

camera.start_preview()
camera.capture("img/" + str(int(time.time())) + ".jpg")
camera.stop_preview() 