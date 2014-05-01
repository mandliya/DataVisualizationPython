"""
Sample data visualization project

This project is developed by Lynn Root

   parse data from an ugly CSV or Excel file, and render it in
   JSON, save to a database, and visualize in graph form.

   Part I: Taking data from a CSV/Excel file, and return it into a format
   that is easier for Python to play with.

   Copyright (c) 2013 E. Lynn Root
   Distributed under the zlib png license. See LICENSE for details.


As license allows me to adapt the project for my use, I will enhance it further for learning more.
"""

import csv

DATA_FILE = "../data/sample_sfpd_incident_all.csv"


def parse(raw_file, delimiter):
    """Function to parse raw CSV data to add it to JSON like data structure for further processing"""

    #opening the file
    opened_file = open(raw_file)

    #get the CSV data from file
    csv_data = csv.reader(opened_file, delimiter=delimiter)

    #get the header fields, first line of file should be header
    fields = csv_data.next()

    #create a empty list for parsed data
    parsed_data = []

    #get all the data row wise in the parsed data in JSON dict based format
    for entry in csv_data:
        parsed_data.append(dict(zip(fields, entry)))

    opened_file.close()

    return parsed_data

def main():
    new_data = parse(DATA_FILE, ",")
    print new_data

if __name__=="__main__":
    main()

