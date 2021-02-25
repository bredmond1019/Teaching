import numpy as np 
import pandas as pd 
from PIL import Image
from wordcloud import WordCloud, STOPWORDS

import matplotlib.pyplot as plt 

#This reads the csv file and stores it in the variable df
df = pd.read_csv("web_scrape_lion_copy.csv")

#This dislays the first 5 columns of the dataframe
print(df.head())

#This prints the first item in the dataframe, under the column: 'Info'
print(df["Info"][0])

#We want to joing all of the rows into one long string
#There are several wats that we can do this
#One method could be to loop through all the rows and add it to a string

text = ''

for i in range(len(df['Info'])):
    text += df['Info'][i]

print(text)



# This is a list comprehension for the above
#text = " ".join(df["Info"][i] for i in range(1, len(df['Info'])))

# exclude is a list of words that I don't want to show up in my wordcloud
exclude = ["population","adult","populations","people", "leopard" ,"individual", "National", "Park", "male", "one", "although", "may", "human", "individuals", "group", "usually", "often", "year"]

stopwords = list(STOPWORDS) + exclude

lion_mask = np.array(Image.open("/Users/angellabaigorria/Documents/AP_Computer_Science/Dog/Lion/Copy/lion5.png"))


transformed_lion_mask = np.ndarray((lion_mask.shape[0],lion_mask.shape[1]), np.int32)


def transform_format(val):
    if val == 0:
        return 255
    else:
        return val

for i in range(len(lion_mask)):
    transformed_lion_mask[i] = list(map(transform_format, lion_mask[i]))


wordcloud = WordCloud(stopwords = stopwords, background_color= "black", colormap="Blues", mask = transformed_lion_mask, contour_color="white").generate(text)





plt.imshow(wordcloud, interpolation = "bilinear")

plt.axis("off")

#This function makes you able to save the file and name it however you want
#Make sure you have .png at the end 
plt.savefig("lion_WORDCLOUD_image4.png")

plt.show()


