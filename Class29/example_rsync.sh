#!/bin/bash

## YOU MUST PUT YOUR OWN USER NAME IN THIS COMMAND
## do not use "mjoyce8"

## what this command means:
# rsync– fast, incremental file‐transfer program (uses SSH by default, like scp)
# -a– archive mode: copies directories recursively and preserves permissions, timestamps, symbolic links, group/owner, etc.
# -z– compress file data in transit (saves bandwidth)
# -v– verbose output (shows you which files are being transferred and a brief summary)
# -u– update; skip files that already exist locally and are newer than the remote copy
# -p– explicitly preserve permissions (already implied by a, but harmless duplication)
# mjoyce8@medicinebow.arcc.uwyo.edu: – your ARCC username and the host you’re pulling from
#/home/mjoyce8/1M_pre_ms_to_wd/LOGS/history.data – absolute path to the file (or directory) you want to copy on that host
# .– “place the file right here,” i.e., use the current working directory on your local machine as the destination

rsync -azvup mjoyce8@medicinebow.arcc.uwyo.edu:/home/mjoyce8/1M_pre_ms_to_wd/LOGS/history.data .
