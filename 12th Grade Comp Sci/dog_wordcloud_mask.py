import numpy as np
import pandas as pd
from PIL import Image
from wordcloud import WordCloud, STOPWORDS

import matplotlib.pyplot as plt


# This reads the csv file and stores it in the variable df
df = pd.read_csv("web_scrape_wiki.csv")

# Makes all of the text into one long string
text = " ".join(df["Info"][i] for i in range(1, len(df['Info'])))

# Create stopword list. This is a predetermined set of words such as: the, and, it, etc.
stopwords = list(STOPWORDS) + ["human", "breed", "study", "humans", "breeds"]





'''Using a dog 'mask' to encapsulate a wordcloud '''

# Use a png file as a mask for the word cloud  
dog_mask = np.array(Image.open(
    "c:/Users/bredm/Documents/Python/Python in the City/dog.png"))  # You will need to change this directory to where the image is located


# Let's take a look at what exactly the dog mask is
print(dog_mask)

# We should see that it is an array with a bunch of zeroes 
# [[0 0 0 ... 0 0 0]
#  [0 0 0 ... 0 0 0]
#  [0 0 0 ... 0 0 0]]

# These zeroes are supposed to represent the white space
# In python, the value of 0 is nothing in terms of color intensity.
# We need 255 for white or 1 for black.
# The rest of the colors are inbetween

# So we can create a function to help us transform the values:
def transform_format(val):
    if val == 0:
        return 255
    return val



# This makes a dummy version of a matrix the same size as the dog_mask array
transformed_dog_mask = np.ndarray((dog_mask.shape[0], dog_mask.shape[1]), np.int32)

# Here we change each value of the above array to match those of the original dog mask
for i in range(len(dog_mask)):
    transformed_dog_mask[i] = list(map(transform_format, dog_mask[i]))


# This creates the wordcloud with the dog mask image and the given parameters
wc = WordCloud(background_color="white", max_words=1000, mask=transformed_dog_mask,
               stopwords=set(stopwords), contour_width=3, contour_color='white')

# This actually generates the word cloud
wc.generate(text)


# Controls the size of the figure
plt.figure(figsize=[20, 10])

# Tells matplotlib what to show
plt.imshow(wc, interpolation="bilinear")

# Turns off axes -- we don't need them since its not a graph
plt.axis('off')

# Show the wordcloud
plt.show()

# Save the word cloud to a file
wc.to_file("c:/Users/student/Documents/dog_cloud.png")
