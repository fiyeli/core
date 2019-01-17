# Fiyeli Core module

## Description
This is the core module of Fiyeli.
It contains a Python script that calls a Camera module and an AI module to take a picture, count the number of persons that appear on the picture and store the data into a CSV file.

## Specification
The script doesn't take any input and doesn't produce an output.\
Execute with the command :
```
python routine.py
```
After execution, a CSV file named `<year>-<month>-<day>.csv` has been created (if not already existing) in the core data directory, and the line `<timestamp>;<number of persons>` has been added.\
The core data directory must be stored in a `FIYELI_DATA` environment variable.
The picture is then removed.

## Other modules specification

### Camera
Must generate a 1024x768 jpg file named `<timestamp>.jpg` into the core image directory.\
This core image directory needs to be stored in a `FIYELI_IMAGES` environment variable.\
The complete command to take the picture and store it in the correct directory needs to be stored in a `FIYELI_CAMERA_SHOT` environment variable.

### AI
Must take a 1024x768 jpg file as input and return an int which correspond to the number of persons that are on the picture.\
The complete command to execute the person detector program needs to be stored in a `FIYELI_AI_RUN` environment variable, and the picture used as input needs to be the last argument to the command (the picture will be appended to the command by our core script).