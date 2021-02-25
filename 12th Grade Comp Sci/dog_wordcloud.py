import numpy as np
import pandas as pd
from PIL import Image
from wordcloud import WordCloud, STOPWORDS

import matplotlib.pyplot as plt

# This reads the csv file and stores it in the variable df
df = pd.read_csv("web_scrape_wiki.csv")

# This displays the first 5 columns of the dataframe 
print(df.head())

# This prints the first item in the dataframe, under the column: 'Info'
print(df["Info"][3])

# We want to join all of the rows into one long string
# There are several ways that we can do this
# One method could be to loop through all the rows and add it to a string

text = ''

for i in range(len(df['Info'])):
    text += df['Info'][i]



# Another method would be to use the join function
# text = " ".join(df["Info"][i] for i in range(1, len(df['Info'])))



# Create stopword list. This is a predetermined set of words such as: the, and, it, etc.
stopwords = list(STOPWORDS) + ["human", "breed", "study", "humans", "breeds"]


'''Generate a Word Cloud'''
# Generate a word cloud image
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)


# Display the generated image:
# The matplotlib way:
plt.imshow(wordcloud, interpolation="bilinear")
# interpolation = "bilinear" is to make the displayed image appear more smoothly.

# This turns off the axes
plt.axis("off")

# This displays the image
plt.show()


# This creates a file on our local machine to the specified directory

wordcloud.to_file("c:/Users/student/Documents/dog_cloud.png")



