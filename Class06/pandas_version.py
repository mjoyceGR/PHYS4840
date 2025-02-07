import pandas as pd

filename = 'NGC6341.dat'

## Assuming the file is space-separated and has no header
## If the file has a different delimiter or a header, 
## adjust the parameters accordingly
df = pd.read_csv(filename, delim_whitespace=True, header=None)

## Extract the columns corresponding to
## F336W, F438W, and F814W magnitudes
blue = df[8]  	# Column 9 
green = df[14]  # Column 15 
red = df[26]  	# Column 27 

blue = blue.to_numpy()
green = green.to_numpy()
red = red.to_numpy()