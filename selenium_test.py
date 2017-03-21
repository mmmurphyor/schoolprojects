from bs4 import BeautifulSoup
#import requests
import os.path
import json
from selenium import webdriver
import time

company="Portland Startups"
htmlFile='temp/' + company + " html.txt"
baseUrl="https://pdxstartups.switchboardhq.com/"
url=htmlFile + baseUrl +"?page=1&post_search[categories]=offers,&post_search[sort]=created_at&post_search[activity]=any&post_search[location]=Portland,%20OR"

if os.path.exists(htmlFile):
    # read the raw data
    with open(htmlFile, 'r') as file:
        data = file.read()

else:
     # access the website
    #driver = webdriver.Firefox()
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)

    os.makedirs(os.path.dirname(htmlFile), exist_ok=True)
    data = driver.page_source
    with open(htmlFile, 'w') as file:
        file.write(str(data.encode('UTF-8')))
        #file.write(data)
        #print(driver.find_element_by_id("content").text)
        driver.close()

soup = BeautifulSoup(data, "html.parser")

jobs = []
#count = 0
start = soup.find('div', {"class" : "post-list-content"})
for link in start.find('a href'):
    #applicationLink = link.get('href')
    #applicationLink = baseurl + applicationLink
   # print (applicationLink)
    print(link)  ### this is just temporary to try and get the first bit out.I am getting nonetype error. 
		

