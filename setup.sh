#!/usr/bin/env bash
# Adding env var
# Fiyeli directories
SCRIPT_PATH=$(readlink -f "$0")
export FIYELI_CORE=$(dirname "$SCRIPT_PATH")
echo "export FIYELI_CORE=$(dirname "$SCRIPT_PATH")" >> ~/.bashrc

export FIYELI_CAMERA="$FIYELI_CORE/../camera"
echo "export FIYELI_CAMERA=\"$FIYELI_CORE/../camera\"" >> ~/.bashrc

export FIYELI_AI="$FIYELI_CORE/../ai"
echo "export FIYELI_AI=\"$FIYELI_CORE/../Fiyeli-Darknet-NNPACK\"" >> ~/.bashrc

export FIYELI_API="$FIYELI_CORE/../api"
echo "export FIYELI_API=\"$FIYELI_CORE/../api\"" >> ~/.bashrc

# Camera module
export FIYELI_CAMERA_SHOT="$FIYELI_CAMERA/camera.py"
echo "export FIYELI_CAMERA_SHOT=\"$FIYELI_CAMERA/camera.py\"" >> ~/.bashrc

# AI module
export FIYELI_AI_RUN="$FIYELI_AI/darknet detector person "
echo "export FIYELI_AI_RUN=\"$FIYELI_AI/darknet detector person \"" >> ~/.bashrc
