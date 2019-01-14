#!/usr/bin/env  python
import glob
import os
import time
from datetime import datetime

list_of_images = glob.glob("img/*")
latest_image = max(list_of_images, key=os.path.getctime)
timestamp = latest_image[:-4]
timestamp = timestamp[4:]
day = datetime.fromtimestamp(float(timestamp)).strftime("%Y-%m-%d")
with open("data/" + day + ".csv", "a") as myFile:
    res = os.system(os.getenv('FIYELI_AI_RUN') + latest_image)
    myFile.write(timestamp + ";" + str(res) + "\n")
time.sleep(1)
os.remove(latest_image)
