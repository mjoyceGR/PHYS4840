#!/bin/bash

## YOU MUST PUT YOUR OWN USER NAME IN THIS COMMAND
## do not use "mjoyce8"

## what this command means:
## scp -- secure copy
## -r  -- recursive (everything in the directory and its subdirectories)
## your ARCC login followed by the location of the file
## the "." dot means "put the file right here, where I currently am in my directory structure"

scp -r mjoyce8@medicinebow.arcc.uwyo.edu:/home/mjoyce8/1M_pre_ms_to_wd/LOGS/history.data .



