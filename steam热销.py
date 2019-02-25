import re
import bs4
import requests
from bs4 import BeautifulSoup
import csv


#根据steam网页的命名规则
p =1

while p<100:
    url = "https://store.steampowered.com/search/?filter=globaltopsellers&page=" + str(p) + "&os=win"
    s = requests.session()
    res = s.get(url).text
    soup = BeautifulSoup(res, "html.parser")
    contents = soup.find(id="search_result_container").find_all('a')

    for content in contents:
        try:
            name = content.find(class_="title").string.strip()
            date = content.find("div", class_="col search_released responsive_secondrow").string.strip()
            price = content.find("div", class_="col search_price responsive_secondrow").string.strip()
            img_src = content.find("div", class_="col search_capsule").find('img').get("src")
            href = content.get("href")
            print(name, href, date, price, img_src)
        except:
            print("error")
    lst = [name, href, date, price, img_src]
    list_name = []
    list_href = []
    list_date = []
    list_price = []
    list_img_src = []
    p = p + 1
    i = 0
    j = 0
    while i < len(lst):
        list_name.insert(j, lst[i])
        list_href.insert(j, lst[i + 1])
        list_date.insert(j, lst[i + 2])
        list_price.insert(j, lst[i + 3])
        list_img_src.insert(j, lst[i + 4])
        i = i + 5
        j = j + 1
    with open('steam热销.csv', 'a',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['name', 'href', 'date', 'price', 'img_src'])
        for i in range(len(list_name)):
            writer.writerow([list_name[i], list_href[i], list_date[i], list_price[i], list_img_src[i]])

