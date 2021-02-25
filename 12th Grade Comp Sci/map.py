# This is the library we will use to make make the maps
import folium

'''
Here is a template for how to create a map. 

*Notice that some of the variables are undefined and this will not run as is
'''



# Create a map
myMap = folium.Map()

# Make markers:
newMark = folium.Marker([lat, lon], popup = name, color =)  # name will pop up when you hover over it on the map

# Add to the map
newMark.add_to(myMap)

# Can customize map with starting location, zoom level and bkgrd map ("tiles")
myMap = folium.Map(location = [40.810900, -73.956054], zoom_start = 10, tiles = 'Stamen Watercolor')

# Here is a website for how to use different tiles for the map:
# https://python-graph-gallery.com/288-map-background-with-folium/

# # Create the .html file.  Feel free to change the name of the file, but leave the .html part of the file name
myMap.save(outfile = 'tempMAP.html')




'''
Using the code above, write your own code below to create a map of any where you want.
It could be your home, your friends house, a place you really want to visit, etc



Extension: Try to put several markers on the map with different names and locations
Try making a terrain map, a street map, or any style you want
'''

# YOUR CODE GOES HERE
