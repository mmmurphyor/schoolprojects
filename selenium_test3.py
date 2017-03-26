from bs4 import BeautifulSoup
#import requests
import os.path
import json
from selenium import webdriver
import time

company="Portland Startups"
location = "Portland, Oregon"
htmlFile='temp/' + company + " html.txt"
url="https://pdxstartups.switchboardhq.com/?page=3&post_search[categories]=asks,&post_search[sort]=created_at&post_search[activity]=any&post_search[location]=Portland,%20OR"

if os.path.exists(htmlFile):
  
    with open(htmlFile, 'r') as file:
        data = file.read()

else:
    path_to_chromedriver ="C:\Windows\chromedriver.exe"
    browser=webdriver.Chrome(executable_path=path_to_chromedriver)
    site=browser.get(url)
    driver.manage().timeouts().implicitlyWait(2000, TimeUnit.MILLISECONDS); 
    html=site.page_source
    os.makedirs(os.path.dirname(htmlFile), exist_ok=True)
    data = browser.page_source
    with open(htmlFile, 'w') as file:
        file.write(str(data.encode('UTF-8')))
        file.write(data)        
        browser.close()

soup = BeautifulSoup(data, "lxml")

jobs = []
for title in soup.find_all('h3'):     
   
    print(title)
    job_title = title.contents[0]
   
    job = {'ApplicationLink': url,
           'Company': company,
           'DatePosted': '',
           'Experience': '',
           'Hours': '',
           'JobID': '',
           'JobTitle': job_title,
           'LanguageUsed': '',
           'Location': '',
           'Salary': '',}
    

    jobs.append(job)

with open(company + '.txt', 'w') as file:
    json.dump(jobs, file)




   







   		

