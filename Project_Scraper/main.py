import pandas as pd 
import requests as req
from bs4 import BeautifulSoup as bs

web = req.get('https://realpython.github.io/fake-jobs/')
soup = bs(web.content,'html.parser')

jobs = []

containers = soup.find_all('div',class_ = 'card-content')
for container in containers:
    title = container.find('h2',class_ ='title is-5').text.strip()
    company = container.find('h3',class_ = 'subtitle is-6 company').text.strip()
    location = container.find('p',class_ = 'location').text.strip()
    date_posted = container.find('p',class_ = 'is-small has-text-grey').find('time')['datetime']

    jobs.append({
        "Title": title,
        "Company" : company,
        "Location" : location,
        "Date Posted" : date_posted
    })

df = pd.DataFrame(jobs)

df[['City','State']] = df['Location'].str.split(', ', expand=True)
df.drop('Location',axis=1,inplace=True)
df['id'] = range(1,len(df)+1)
df = df[['id','Title','Company','City','State','Date Posted']]
df['Date Posted'] = pd.to_datetime(df['Date Posted'])

df.to_csv("jobs.csv",index=False)


print(df.head())