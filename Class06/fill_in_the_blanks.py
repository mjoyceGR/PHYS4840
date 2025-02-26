
## np.where() returns an ARRAY OF INDICES that satisfy the prescribed condition
## in the line below, we are finding all indices where the "red" array is > 5
quality_cut_red = np.where(red > 5)

## the quality cut we really want, however, is to exclude all of those
## entries that have been assigned a value of "-99" in the data file
## What would that look like?

## we can use np.where() with multiple conditions, like so:
quality_cut = np.where( (red   > ...)  &\
					    (...   > ...)  &\
					    (...) )

## set a figure size
fig, ax = plt.subplots( figsize=(<width> , <height>) )


## instead of plotting the "raw" color and magnitude values,
## we can use the arrays of indices from np.where() to plot only the good data
accceptable_colors = color[quality_cut]
acceptable_Rband = magnitude[...]

plt.plot(..., ... )

## we can make choices that are more appropriate for our problem using keyword arguments in plt.plot
## some examples are:
plt.plot(... , ... , marker = ..., color ='', markersize = ..., alpha= ... )
## navitage to 
##     https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
## for a dictionary of options

## because astronomers are terrible, the magnitude system is reversed
## smaller numbers indicate brighter stars, so should be at the top of your plot
## this command inverts the y-axis
plt.gca().invert_yaxis()

## label your axes
plt.xlabel("What are we plotting?", fontsize=...)
plt.ylabel(..., fontsize=...)

plt.title(..., fontsize=...)

## we can enforce plot limits
plt.xlim(... , ...)

## RECALL that we have inverted the y-axis above...



