!#/usr/bin/bash

python3.8 double_pendulum.py
#python3.8 perturbed_pendulum.py
#python3.8 plot_double_pendulum_data.py
#eog motions.png

## this will generate a video of the simulation with the name specified in generate_video.py
## it will generate this video based on the data file provided in generate_video.py
python3.8 generate_video.py 

vlc double_pendulum_simulation.mp4