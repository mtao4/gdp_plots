import pandas
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt
# enable command line argument
import sys
print(sys.argv[1])

# load data and transpose so that country names are
# the columns and their gdp data becomes the rows

# read data into a pandas dataframe and transpose
filename_list = sys.argv[1:] # take up all arguments after the pythonfile

# Usage:
# python gdp_plots.py *.csv

for filename in filename_list:
    data = pandas.read_csv(filename, index_col = 'country').T

    # create a plot the transposed data
    ax = data.plot(title=filename)

    # axes labels
    ax.set_xlabel('year')
    ax.set_ylabel('GDP per capita')

    # set axes ticks
    ax.set_xticks(range(len(data.index))) # create ticks based on the data
    ax.set_xticklabels(data.index,rotation=45)

    # display the plot
    plt.show()
