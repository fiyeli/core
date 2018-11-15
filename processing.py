#!/usr/bin/env  python
import glob
import os

list_of_files = glob.glob("~/img/*") # * means all if need specificic format thyen *.csv
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)
sleep(1)
os.remove(latest_file)