"""
Sample Data Visualization Project
Parse data from an ugly CSV or Excel file, and render it in
JSON, save to a database, and visualize in graph form.

   Part II: Take the data we just parsed and visualize using popular Python math libraries

Copyright (c) 2013 E. Lynn Root
 Distributed under the zlib png license. See LICENSE for details.

Since License allows me to adapt project, I will enhance this project further.
"""


from collections import Counter

import csv
import parse
import matplotlib.pyplot as plt
import numpy.numarray as na

DATA_FILE = "../data/sample_sfpd_incident_all.csv"

def visualize_days():
    """Visualize data by day of week"""
    data_file = parse.parse(DATA_FILE, ",")

    #Counter returns a dict where it sums total values for each key.
    #In our case here, the keys are DaysOfWeek, and the values are
    #and values are count of incidents

    counter = Counter(item["DayOfWeek"] for item in data_file)

    #Separate out the counter in order to order it correctly when     plotting

    data_list = [
                    counter["Monday"],
                    counter["Tuesday"],
                    counter["Wednesday"],
                    counter["Thursday"],
                    counter["Friday"],
                    counter["Saturday"],
                    counter["Sunday"],
            ]
    day_tuple = tuple(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])

    #Assign the data to the plot
    plt.plot(data_list)

    #Assign lables to the plot from day_tuple
    plt.xticks(range(len(day_tuple)), day_tuple)

    #show plot
    plt.show()

    #Save the graph!
    plt.savefig("Days.png")

    #close figure
    plt.clf()

def visualize_type():
        """Visualize data by category in a bar graph"""

        # grab our parsed data
        parsed_data = parse.parse(DATA_FILE, ",")

        # make a new variable, 'counter', from iterating through each line
        # of data in the parsed data, and count how many incidents happen
        # by category

        counter = Counter(item["Category"] for item in parsed_data)


        # Set the labels which are based on the keys of our counter.
        # Since order doesn't matter, we can just used counter.keys()
        labels = tuple(counter.keys())

        # Set exactly where the labels hit the x-axis
        xlocations =  na.array(range(len(labels))) + 0.5

        # Width of each bar that will be plotted
        width = 0.5

        # Assign data to a bar plot (similar to plt.plot()!)
        plt.bar(xlocations, counter.values(), width=width)

        # Assign labels and tick location to x-axis
        plt.xticks(xlocations + width/2, labels, rotation=90)

        #Increase bottom side to adjust labels
        plt.subplots_adjust(bottom=0.4)

        #Mkae the overall graph/figure large
        plt.rcParams['figure.figsize'] = 12, 8

        #show the graph
        plt.show()

        #save the graph
        plt.savefig("Type.png")

        #close figure
        plt.clf()



def main():
    visualize_days()
    visualize_type()

if __name__ == "__main__":
    main()


