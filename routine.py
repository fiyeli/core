#!/usr/bin/env  python
import glob
import os
import time
from datetime import datetime

# Take a picture with the camera
os.system(os.getenv('FIYELI_CAMERA_SHOT'))

# Get the last image
list_of_images = glob.glob(os.getenv('FIYELI_IMAGES') + "/*")
latest_image = max(list_of_images, key=os.path.getctime)

# Get the timestamp and the associated day from the image name
path_len = len(os.getenv('FIYELI_IMAGES')) + 1
timestamp = latest_image[:-4]
timestamp = timestamp[path_len:]
day = datetime.fromtimestamp(float(timestamp)).strftime("%Y-%m-%d")

# Feeding the AI with the image to know how many person are in
res = os.system(os.getenv('FIYELI_AI_RUN') + latest_image)

# Writing the result in the right CSV file
with open(os.getenv('FIYELI_DATA') + "/" + day + ".csv", "a") as myFile:
    myFile.write(timestamp + ";" + str(res) + "\n")
time.sleep(1)

# Delete processed image
os.remove(latest_image)
