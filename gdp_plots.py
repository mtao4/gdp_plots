# this script reads in continent files and plot 

import pandas
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt
# enable command line argument
import sys
#print(sys.argv[1])

import glob # getting a list of files

def parse_arguments():
    """ This function parses the user's command line arguments and returns the appropriate list of files

       Input:
	===============
	  Nothing
       Returns:
	===============
          filename_list: list of filenames(list)
    """
    # reads in the arguments as -a or filename  
    # check number of arguments, if not correct, print message and exit the program
    if len(sys.argv)<2:
        # no arguments supplied
        print('Not enough arguments have been provided')
        print('Usage: python gdp_plots.py <filename>')
        print('Options: -a: ploy all gdp data in current directory')
        exit() # exit the program


    if sys.argv[1]=='-a':
        filename_list = glob.glob('*gdp*.csv')
        # check file list is not empty
        if len(filename_list)==0:
            print('No files found in current directory')
            exit()
    else:
        filename_list = sys.argv[1:]
    return filename_list

def create_plots(filename_list):
    """ This function plots all files in the list using Pandas Matplotlib. Each data file is its own plot

       Input:
        ===============
          filename_list: a list of strings of filenames to plot
       Returns:
        ===============
          Nothing
    """
    for filename in filename_list:
        # read data into a pandas dataframe and transpose
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

# calling all functions
def main():
    """ This function parses the user's command line arguments and returns the appropri$

       Input:
        ===============
          Nothing
       Returns:
        ===============
          filename_list: list of filenames(list)
    """
    filename_list = parse_arguments()
    create_plots(filename_list)

main()
