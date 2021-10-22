def parcing ():
    from bs4 import BeautifulSoup
    import requests
    import csv
    import os

    url = 'https://www.kinopoisk.ru/lists/series-top250/'
    headers = {'accept': '* / *',
               "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Safari/537.36"}
    count1 = 0

    while count1 != 5:

        print(count1 + 1, 'Итерация из 5')

        if count1 == 0:

            req = requests.get(url, headers)

            a = req.text

            with open("index.html", "w", encoding='utf-8') as file:
                file.write(a)

            with open("index.html", encoding="utf-8") as file:
                kin = file.read()

            name = ['name']
            year = ['year']
            country = ['country']
            genre = ['genre']
            rating = ['rating']
            count_rating = ['count_rating']

        elif count1 != 0:

            req = requests.get(url + f"?page={count1}&" + "tab=all", headers)

            a = req.text

            with open("index.html", "w", encoding='utf-8') as file:
                file.write(a)

            with open("index.html", encoding="utf-8") as file:
                kin = file.read()

            name = []
            year = []
            country = []
            genre = []
            rating = []
            count_rating = []

        soup = BeautifulSoup(kin, 'lxml')

        table = soup.find('div', class_= "selection-list").find_all('div', class_= "desktop-rating-selection-film-item")

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
        year = [i.split()[-1] for i in year]
        with open(f"data.csv", "a", encoding="utf-8") as file:
                   writer = csv.writer(file,delimiter=';',lineterminator='\n')
                   table1 = zip(name,year,country,genre,rating,count_rating)
                   for row in table1:
                       writer.writerow(row)
        count1 += 1
        if count1 == 5:
            print('Файл готов!')

parcing()