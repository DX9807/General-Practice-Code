from bs4 import BeautifulSoup as soup
import pandas as pd
import matplotlib.pyplot as plt
from urllib.request import urlopen as ureq
import mysql.connector as join
import sys

print("""
      ==================================================
      ||              Movie 250                       ||               
      ==================================================
      1.Print out the top ten movies with highest rating.
      2.Print out the ten movies with lowest rating.
      3.Print out the Graphical view.
      4.Print out the movies of comedy genre.
      5.Print out the movies of action genre.
      6.Print out the movie with highest number of votes.
      7.Print out the movie with highest gross.
      8.Print out the movies with romantic genre.
      
      """)

mydb=join.connect(host='localhost',user='root',database='sample',passwd='subodh9807')
mycursor=mydb.cursor()

"""sql_table= (
    "CREATE TABLE IF NOT EXISTS Moviez ("
    "  `mov_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `release_year` varchar NOT NULL,"
    "  `mov_name` varchar(100) NOT NULL,"
    "  `genre` varchar(16) NOT NULL,"
    "  `rating` DECIMAL(2,2) NOT NULL,"
    "  `votes` INT(10) NOT NULL,"
    "  'gross' DECIMAL(4,2) NOT NULL,"
    "  'director' VARCHAR(40) NOT NULL,"
    "  PRIMARY KEY (`mov_no`)"
    ") ENGINE=InnoDB")"""


myUrl='https://www.imdb.com/search/title?groups=top_250&sort=user_rating'
html_data=ureq(myUrl)
read_html=html_data.read()
html_data.close()

page_soup=soup(read_html,'html.parser')
#html_doc=print(page_soup.prettify())


my_container=page_soup.find_all('div',{'class':'lister-item-content'})
#for string in page_soup.stripped_strings:
#   print(string)
#container=my_container[0]
"""mov_name=container.find_all('a')
print(mov_name[0].text)
year=container.find_all('span',{'class':'lister-item-year text-muted unbold'})
print(year[0].text)
rating=container.find_all('span',{'class':'global-sprite rating-star imdb-rating'})
print(rating[0].text)
gross=container.find_all('span',{'name':"nv"})
print(gross[0].text)
genre=container.find_all('span',class_='genre')
print(genre[0].text)
director=container.find_all('p',{'class':''})
print(director[0].text)
no_votes=container.find_all('span',{'name':'nv','data-value':'2080112'})
print(no_votes[0].text)
"""

#print(len(my_container))




#def moviegasm():
    
      
      
      
