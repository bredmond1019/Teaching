from bs4 import BeautifulSoup
import requests
from csv import writer

'''Accessing the website'''
# This is where we put the website that we want to scrape from
website_url = "https://en.wikipedia.org/wiki/Dog"

# This uses the requests method to access the website URL
response = requests.get(website_url)
# This will raise a status error if the website is unaccessable
# this is useful so we know that the website isn't working rather than our code not working 
response.raise_for_status()

# This gets all of the html from the website and parses the information
wiki = BeautifulSoup(response.text, "html.parser")




'''Reading through the file'''
# Here we create our own csv file
with open('web_scrape_wiki.csv', 'w', encoding="utf-8") as csv_file:
    csv_writer = writer(csv_file) # Turns our data into strings and writes it
    csv_writer.writerow(['Info']) # Creates a row called 'Info' that will act as our header


    for i in wiki.select('p'):  # Iterates through each section that has a <p> in the html
        csv_writer.writerow([i.getText()]) # Get ONLY the text from the html and writes it in a row






