import re
import requests
from bs4 import BeautifulSoup


class parceListArea:
    def __init__(self, typeCity):
        self.typeCity = typeCity

    def printUrl(self):
        print(self.typeCity)

    def pathUrlToClassArea(self):
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
                    # print(slovar2)
            return slovar2
        except:
            return 'сайт не отвечает'

# st = parceListArea('small')
# # st.printUrl()
# print(st.pathUrlToClassArea())
