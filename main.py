#шаблон
#import requests as req
#from bs4 import BeautifulSoup as bs

# class Name:
#     def __init__(self,url):
#         self.url = url
#         self.header = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
#         }
#         self.soup=None
#     def auditSite(self):
#         response = req.get(self.url,headers=self.header)
#         if response.status_code == 200:
#             self.soup = bs(response.text,'html.parser')
#         else:
#             print("Не вдалося підключитися до сайту")
#     def getInfo(self):
#         pass
#     def showInfo(self):
#         pass
# url="посилання"
# obj=Name(url)
# obj.auditSite()
# site=obj.getInfo()
# if site:
#     obj.showInfo()
# else:
#     print("Жодної інформації не отримано")


# import requests as req
# from bs4 import BeautifulSoup as bs
#
# class Comfy:
#     def __init__(self,url):
#         self.url = url
#         self.header = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
#         }
#         self.soup=None
#     def auditSite(self):
#         response = req.get(self.url,headers=self.header)
#         if response.status_code == 200:
#             self.soup = bs(response.text,'html.parser')
#         else:
#             print("Не вдалося підключитися до сайту")
#     def getInfo(self):
#         laptop=[]
#         lap=self.soup.find_all('div',class_='products-catalog')
#         if not lap:
#             print('Помилка в пошуку')
#             return laptop
#         for i in laptop[0:4]:
#             name=i.find('a', class_='prdl-item__name ellipsis-2-lines')
#             nameError=name.text() if name else 'Відсутня назва'
#             price=i.find('div', class_='products-list-item-price__actions-price-current')
#             priceError=price.text() if price else 'Відсутня ціна'
#             laptop.append(
#                 {
#                     'Назва':nameError,
#                     'Ціна':priceError,
#                 }
#             )
#         return laptop
#
#
#     def showInfo(self, laptop):
#         print('№\t', 'НАЗВА', '\t'*2, 'ЦІНА', 't'*2)
#         print('-'*50)
#         for i in laptop:
#             print('\t',i['Назва'],'\t',i['Ціна'])
# url="https://comfy.ua/ua/black-friday/cat__120/?gad_source=1&gclid=Cj0KCQiAkJO8BhCGARIsAMkswyhJ-lMrSryvvEIyf_s3FPnjgF7ydctFE_R10Yj_zj9l231aRd-ZIeAaAmjrEALw_wcB"
# obj=Comfy(url)
# obj.auditSite()
# site=obj.getInfo()
# print("\tНайпопулярніші чотири ноутбуки\n")
# if site:
#     obj.showInfo()
# else:
#     print("Жодної інформації не отримано")


import requests as req
from bs4 import BeautifulSoup as bs

class Name:
    def __init__(self,url):
        self.url = url
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.soup=None
    def auditSite(self):
        response = req.get(self.url,headers=self.header)
        if response.status_code == 200:
            self.soup = bs(response.text,'html.parser')
        else:
            print("Не вдалося підключитися до сайту")
    def getInfo(self):
        coins[]
        listCoin=self.soup.find('tbody')
        if not listCoin:
            print('Помилка в пошуку')
            return coins
        info=listCoin.find_all('tr')[0:5]
        for i in info:
            name=i.find('td').get_text()
    def showInfo(self):
        pass
url="https://coinmarketcap.com/"
obj=Coin(url)
obj.auditSite()
site=obj.getInfo()
print('5 найпопулярніші криптомонети')
if site:
    obj.showInfo()
else:
    print("Жодної інформації не отримано")