import json
import csv
import re

import requests
from bs4 import BeautifulSoup
import json, urllib

class parceListArea:
    def __init__(self, typeCity):
        self.typeCity = typeCity
        # super().__init__()
        # self.pathUrlToClassArea()
        # self.citiSmall()

    def printUrl(self):
        print(self.typeCity)

    def pathUrlToClassArea(self):

        # url = self.url
        try:
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
        except:
            return 'Сайт не отвечает'
        # print(links2)
        # print(type(links2))
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
        try:
            if self.typeCity == 'small':

                request2 = requests.get(small)
                soup2 = BeautifulSoup(request2.text, 'lxml')
                find_li2 = soup2.findAll('li')
                slovar2 = {}
                for i in find_li2:
                    citi = str(i.find('strong')).rstrip()
                    # citi_test = str(citi.('Канаш')).rstrip()
                    area = str(i.find('span')).rstrip()
                    # tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
                    tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
                    no_tags_citi = tag_re.sub('', citi)
                    no_tags_area = tag_re.sub('', area)
                    if no_tags_citi == 'None':
                        no_tags_citi = ''
                    else:
                        slovar2.update({no_tags_citi: no_tags_area})
                    # print(no_tags_area)
                return slovar2
        except:
            return 'сайт не отвечает'

        if self.typeCity == 'medium':
            try:
                request2 = requests.get(medium)
                soup2 = BeautifulSoup(request2.text, 'lxml')
                find_li2 = soup2.findAll('li')
                slovar2 = {}
                for i in find_li2:
                    citi = str(i.find('strong')).rstrip()
                    # citi_test = str(citi.('Канаш')).rstrip()
                    area = str(i.find('span')).rstrip()
                    # tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
                    tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
                    no_tags_citi = tag_re.sub('', citi)
                    no_tags_area = tag_re.sub('', area)
                    if no_tags_citi == 'None':
                        no_tags_citi = ''
                    else:
                        slovar2.update({no_tags_citi: no_tags_area})
                    # print(no_tags_area)
                return slovar2
            except:
                return 'Сайт не отвечает'

        if self.typeCity == 'big':
            try:
                request2 = requests.get(big)
                soup2 = BeautifulSoup(request2.text, 'lxml')
                find_li2 = soup2.findAll('li')
                slovar2 = {}
                for i in find_li2:
                    citi = str(i.find('strong')).rstrip()
                    # citi_test = str(citi.('Канаш')).rstrip()
                    area = str(i.find('span')).rstrip()
                    # tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
                    tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
                    no_tags_citi = tag_re.sub('', citi)
                    no_tags_area = tag_re.sub('', area)
                    if no_tags_citi == 'None':
                        no_tags_citi = ''
                    else:
                        slovar2.update({no_tags_citi: no_tags_area})
                    # print(no_tags_area)
                return slovar2
            except:
                return 'Сайт не отвечает'

        if self.typeCity == 'large':
            try:
                request2 = requests.get(large)
                soup2 = BeautifulSoup(request2.text, 'lxml')
                find_li2 = soup2.findAll('li')
                slovar2 = {}
                for i in find_li2:
                    citi = str(i.find('strong')).rstrip()
                    # citi_test = str(citi.('Канаш')).rstrip()
                    area = str(i.find('span')).rstrip()
                    # tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
                    tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
                    no_tags_citi = tag_re.sub('', citi)
                    no_tags_area = tag_re.sub('', area)
                    if no_tags_citi == 'None':
                        no_tags_citi = ''
                    else:
                        slovar2.update({no_tags_citi: no_tags_area})
                    # print(no_tags_area)
                return slovar2
            except:
                return 'Сайт не отвечает'

        if self.typeCity == 'largest':
            try:
                request2 = requests.get(largest)
                soup2 = BeautifulSoup(request2.text, 'lxml')
                find_li2 = soup2.findAll('li')
                slovar2 = {}
                for i in find_li2:
                    citi = str(i.find('strong')).rstrip()
                    # citi_test = str(citi.('Канаш')).rstrip()
                    area = str(i.find('span')).rstrip()
                    # tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
                    tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
                    no_tags_citi = tag_re.sub('', citi)
                    no_tags_area = tag_re.sub('', area)
                    if no_tags_citi == 'None':
                        no_tags_citi = ''
                    else:
                        slovar2.update({no_tags_citi: no_tags_area})
                    # print(no_tags_area)
                return slovar2
            except:
                return 'Сайт не отвечает'

        if self.typeCity == 'millioners':
            try:
                request2 = requests.get(millioners)
                soup2 = BeautifulSoup(request2.text, 'lxml')
                find_li2 = soup2.findAll('li')
                slovar2 = {}
                for i in find_li2:
                    citi = str(i.find('strong')).rstrip()
                    # citi_test = str(citi.('Канаш')).rstrip()
                    area = str(i.find('span')).rstrip()
                    # tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
                    tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
                    no_tags_citi = tag_re.sub('', citi)
                    no_tags_area = tag_re.sub('', area)
                    if no_tags_citi == 'None':
                        no_tags_citi = ''
                    else:
                        slovar2.update({no_tags_citi: no_tags_area})
                    # print(no_tags_area)
                return slovar2
            except:
                return 'Сайт не отвечает'

# st = parceListArea('small')
# # st.printUrl()
# print(st.pathUrlToClassArea())

