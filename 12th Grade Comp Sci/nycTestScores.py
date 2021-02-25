import folium
import pandas as pd 

#Read in the test scores
testScores = pd.read_csv('DistrictMath.csv')
#Grab only 2016 data
score2016 = testScores[testScores.Year == 2016]
#Focus on 8th grade
scores8th2016 = score2016[testScores.Grade == "8"]


# Create a map
schoolMap = folium.Map(location = [40.75, -74.125])

# Create a layer, shaded by test scores:
schoolMap.choropleth(geo_data = "schoolDistricts.json", 
                    fill_color = 'YlGn', fill_opacity = 0.5, 
                    line_opacity = 0.5, 
                    threshold_scale = [100,200,300,400], 
                    data = scores8th2016,
                    key_on = 'feature.properties.SchoolDist',
                    columns = ['District', 'Mean Scale Score']
                    )

schoolMap.save(outfile = 'testScores.html')






'''
To get the 'schoolDistricts.json' file:
--Go to the OPEN DATA NYC PLANNING via link below
--You have to scroll down to the: School, Police, Health & Fire
--Then right click on the geoJSON globe and save the file as a .json file

https://www1.nyc.gov/site/planning/data-maps/open-data/districts-download-metadata.page



To get the DistrictMath.csv file:
-- Go to NYC Dept of ED via link below
-- Download the DISTRICT file (it will be an Excel sheet)
-- Then in the Excell sheet you can fo to FILE -> SAVE AS 
-- Then save the page you want as a .csv file

https://infohub.nyced.org/reports-and-policies/citywide-information-and-data/test-results





Here is a link to some other examples and uses of folium:

https://python-visualization.github.io/folium/quickstart.html







'''
