import re
import requests
from bs4 import BeautifulSoup


class parceListInOut:
    def __init__(self, typeCity):
        self.typeCity = typeCity

    def writeFile(self):

        request = requests.get('https://города-россия.рф')
        soup = BeautifulSoup(request.text, 'lxml')
        find_li = soup.findAll('a')
        links = []
        links2 = []  # линки на города по категориям
        for link in find_li:
            links.append(link)
            w = link.get('href')
            if 'cities.php?name' in str(w):
                links2.append('https://города-россия.рф' + str(w))

        for i in links2:
            if 'малые' in i:
                small = i
            if 'средние' in i:
                medium = i
            if 'большие' in i:
                big = i
            if 'крупные' in i:
                large = i
            if 'крупнейшие' in i:
                largest = i
            if 'миллионеры' in i:
                millioners = i
            else:
                print('Нет совпадений')

        if self.typeCity == 'small':
            www = small
        if self.typeCity == 'medium':
            www = medium
        if self.typeCity == 'big':
            www = big
        if self.typeCity == 'large':
            www = large
        if self.typeCity == 'largest':
            www = largest
        if self.typeCity == 'millioners':
            www = millioners

        request2 = requests.get(www)
        soup2 = BeautifulSoup(request2.text, 'lxml')
        find_li2 = soup2.findAll('li')
        slovar2 = {}
        for i in find_li2:
            citi = str(i.find('strong')).rstrip()
            area = str(i.find('span')).rstrip()
            tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
            no_tags_citi = tag_re.sub('', citi)
            no_tags_area = tag_re.sub('', area)
            if no_tags_citi == 'None':
                no_tags_citi = ''
            else:
                slovar2.update({no_tags_citi: no_tags_area})

        with open('test.txt', 'w', newline='') as file:
            for key, value in slovar2.items():
                writer = file.writelines(key + ',' + value + '\n')

    def readFile(self):
        with open('test.txt', 'r') as file:
            fs = file.readlines()
            sl = {}
            for i in fs:
                data = i.strip().split(',')
                sl.update({data[0]: data[1]})
            return sl

# st = parceListInOut('https://города-россия.рф')
# st.writeFile()
# print(st.readFile())
