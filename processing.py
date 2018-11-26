#!/usr/bin/env  python
import glob
import os
import time
from datetime import datetime

list_of_files = glob.glob("img/*") # * means all if need specificic format thyen *.csv
latest_file = max(list_of_files, key=os.path.getctime)
timestamp = latest_file[:-4]
timestamp = timestamp[4:]
day = datetime.fromtimestamp(float(timestamp)).strftime("%Y-%m-%d")
with open("data/" + day + ".csv", "a") as myFile:
    myFile.write(timestamp + ";0\n")
time.sleep(1)
os.remove(latest_file)