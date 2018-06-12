
#My task is to write a webpage scraper in python

#I've chosen to create a scraper that will scrape r/combatfootage's posts for a day and pull any that mention 'ATGM'

#To do this, I'll scrape the username, source, and permalink for any permalink that contains 'ATGM'

from bs4 import BeautifulSoup
import requests
import os, os.path, csv

listingurl = 'https://www.reddit.com/r/CombatFootage/'

response = requests.get(listingurl)
soup = BeautifulSoup(response.text, 'html.parser')

post_list = soup.find(class_="title may-blank outbound")

print(post_list)

