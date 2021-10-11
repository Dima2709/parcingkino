from bs4 import BeautifulSoup
import requests
import csv
import os
#url = 'https://www.kinopoisk.ru/lists/series-top250/'

#req = requests.get(url)

#a = req.text

#with open ("index.html", "w", encoding='utf-8') as file:
#    file.write(a)

with open("index.html", encoding = "utf-8") as file:
    kin = file.read()

soup = BeautifulSoup(kin, 'lxml')

table = soup.find(class_= "selection-list").find_all(class_= "desktop-rating-selection-film-item")
name = ['name']
year = []
year1 = ['year']
country = ['country']
genre = ['genre']
rating = ['rating']
count_rating = ['count_rating']
for i in table:
    table1 = i.find_all(class_="selection-film-item-meta__name")
    name.append(table1[0].text)
for i in table:
    table1 = i.find_all(class_="selection-film-item-meta__original-name")
    year.append(table1[0].text)
for i in table:
    table1 = i.find_all(class_="rating__value rating__value_positive")
    rating.append(table1[0].text)
for i in table:
    table1 = i.find_all('p',class_="selection-film-item-meta__meta-additional")
    for j in table1:
        count = 0
        for t in j:
            if count % 2 == 0:
                country.append(t.text)
                count += 1
            elif count % 2 != 0:
                genre.append(t.text)
                count += 1
for i in table:
    table1 = i.find_all(class_="rating__count")
    count_rating.append(table1[0].text)
for i in year:
    year1.append(i.split()[-1])
with open(f"data.csv", "a", encoding="utf-8") as file:
           writer = csv.writer(file,delimiter=';',lineterminator='\n')
           table1 = zip(name,year1,country,genre,rating,count_rating)
           for row in table1:
               writer.writerow(row)

