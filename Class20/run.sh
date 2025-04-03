#!/bin/bash

#python3.8 double_pendulum.py
#python3.8 plot_double_pendulum_data.py
#eog motions.png

python3.8 perturbed_pendulum.py
echo "simulation has been run"

## this will generate a video of the simulation with the name specified in generate_video.py
## it will generate this video based on the data file provided in generate_video.py
python3.8 generate_video.py 
echo "video generated from simluation"

vlc double_pendulum_simulation.mp4