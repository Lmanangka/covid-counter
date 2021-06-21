'''
Created : 21/06/2021
Author  : Leo Manangka
'''
import requests
from bs4 import BeautifulSoup

class Covid:
    '''class covid'''

    def __init__(self):
        self.country=input('Country: ')
        for i in range(0, len(self.country), 1):
            if self.country[i] == ' ':
                self.country = self.country.replace(self.country[i], '-')
        self.url='https://www.worldometers.info/coronavirus/country/%s'%self.country
        self.header={'User-Agent':'BOT'}
        self.resp=requests.get(self.url,headers=self.header)
        self.soup=BeautifulSoup(self.resp.text,'html.parser')

    def count(self):
        '''collecting data from web'''

        if self.resp.status_code==200:
            print('Success!\n')
        else:
            print('An error has occured',self.resp.status_code)

        country=self.soup.find_all('h1')[0].text
        last_update=self.soup.find('div',\
                {'style':'font-size:13px; color:#999; text-align:center'},\
                {'Last updated:'})
        cases=self.soup.find_all('h1')[1].text
        deaths=self.soup.find_all('h1')[2].text
        recovered=self.soup.find_all('h1')[3].text
        count_cases=self.soup.find_all('div',{'class':'maincounter-number'})[0]
        count_deaths=self.soup.find_all('div',{'class':'maincounter-number'})[1]
        count_recovered=self.soup.find_all('div',{'class':'maincounter-number'})[2]

        print(country)
        print(last_update.text)
        print(cases,count_cases.select_one('span').text)
        print(deaths,count_deaths.select_one('span').text)
        print(recovered,count_recovered.select_one('span').text,'\n')

if __name__=='__main__':
    covid=Covid()
    covid.count()
