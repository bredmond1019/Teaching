'''
How to pull Data from the NYC Open Data Website
'''

# Go to NYC Open Data Website
# Search for Motor Vehicle Crashes
# Click on VIEW DATA
# Use the FILTER option
# click ADD A NEW FILTER CONDITION for the following two conditions
    # Crash date IS BETWEEN:  (use a two week period)
    # Crash time IS BLANK (then check off NOT BLANK)
# Close the filter window
# Click on EXPORT
# DOWNLOAD as CSV    (**NOT CSV FOR EXCEL** will cause issues)

# Go to your downloads folder and put the new downloaded file into the current folder you are working in



'''
Now lets make a map of the motor vehicle crashes
'''

import pandas as pd
import folium

# Getting file
collisions = pd.read_csv('MVCrashes.csv')

# Setting up the map:
mapCollisions = folium.Map(location=[40.810900, -73.956054], tiles="Cartodb Positron", zoom_start=11)

# This line will show you all of the latitudes that have collisions
print(collisions["LATITUDE"])

# Looping through the file to see all the columns
for column in collisions.columns:
    print(column)



# This is how you can loop through the data and assign each row to a variable
for index, row in collisions.iterrows():
    lat = row["LATITUDE"]
    lon = row["LONGITUDE"]
    popname = row["CRASH TIME"]


    # YOUR CODE GOES HERE


'''
Try using the code above to make a map of all of the crashes 



After creating your map, 
Be prepared to answer the following questions:

1. Which area has the most crashes, if any?
2. Which area has the least?
3. Why do you think this is?


'''










'''
EXTENSIONS:

1)  Try to make a map that has different colors based one or more of the following criteria, be creative:
        -- Time of the incident
        -- Neighborhood/Borough
        -- Type of incident
        -- Street Name
        -- Number of People Killed/Injured




2) Go to NYC Open Data and look up your own data and make an interesting map using that data
