"""
Data Visualization Project

Parse data from an ugly CSV or Excel file, and render it in
JSON-like form, visualize in graphs, and plot as a map.

Part III: Take the data we parsed earlier and create a different format
for rendering a map. Here, we parse through each line item of the
CSV file and create a geojson object, to be collected into one geojson
file for uploading to gist.github.com.


Copyright (c) 2013 E. Lynn Root
Distributed under the zlib png license. See LICENSE for details.

Extending it further for learning Data Visualization
Ravi Mandliya

"""

import parse
import geojson
import parse as p

def create_map(data_file):
    """Create a GeoJSON file
    Returns a GeoJSON file that can be rendered in GitHub Gist at gist.github.com.

    """
    #Define type of GeoJSON we're creating
    geo_map = {"type":"FeatureCollection"}

    #An empty list to collect each point on graph
    item_list = []

    #Iterate over data to create a GeoJSON document
    for index,line in enumerate(data_file):
        #Skip 0 coordinates
        if line['X'] == "0" or line["Y"] == "0":
            continue
        #set up a new dictionary for each iteration
        data = {}

        #Assign line items to appropriate GeoJSON fields
        data['type'] = 'Feature'
        data['id'] = index
        data['properties'] = {'title':line['Category'],
                              'description':line['Descript'],
                              'date':line['Date']}
        data['geometry'] = {'type':'Point',
                            'coordinates':(line['X'], line['Y'])}
        #add data to our item_list
        item_list.append(data)

    #for each point in our item_list, we add the point in our
    #dictionary, setdefault creates a key called 'features' that
    #has a value type of empty list. With each iteration, we
    #are appending our point to that list.

    for point in item_list:
        geo_map.setdefault('features',[]).append(point)

    #Now that all data is parsed in GeoJSON, write to a file so we can upload it to gist.github.com

    with open('file_sf.geojson','w') as f:
        f.write(geojson.dumps(geo_map))

def main():
    data = p.parse(p.DATA_FILE, ",")
    return create_map(data)

if __name__=='__main__':
    main()




