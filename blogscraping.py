

import requests
from bs4 import BeautifulSoup

#integrate into csv 
import pandas as pd



url ="https://thegrowinginch.blogspot.com/"

#getting content 
r = requests.get(url)
htmlcontent = r.content 

#use library 
soup = BeautifulSoup(htmlcontent, 'html.parser')
#print(soup.prettify)

#traverse through html 
#what is the title for my blog ?
def transform(soup):
    header = soup.title
    print("The title for my blog is :" , header)
    #print(type(title))

    #get divs and inividual blogs 
    divs = soup.find_all('div', class_="post hentry uncustomized-post-template")
    #print(len(divs)) # 5 
    for item in divs:
        title = (item.find('h3', class_="post-title entry-title").text.replace("\n", ""))
        date = item.find('a', class_="timestamp-link").text.strip()
        comments = (item.find('a', class_="comment-link").text.replace("\n", ""))

        #print(title, date, comments)

        blog = {
            'title': title,
            'date' : date ,
            'comments' : comments}

        bloglist.append(blog)
    return 
    
bloglist =[]


transform(soup)
print(bloglist)
#df = pd.DataFrame(bloglist)
#print(df.head())
#df.to_csv('blogs.csv')




