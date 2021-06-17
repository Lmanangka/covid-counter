import requests
from bs4 import BeautifulSoup

class Covid(object):
    def __init__(self):
        self.country=input('Country: ')
        for i in range(0, len(self.country), 1):
            if (self.country[i] == ' '):
                self.country = self.country.replace(self.country[i], '-')
        self.url='https://www.worldometers.info/coronavirus/country/%s'%self.country
        self.header={'User-Agent':'BOT'}
        self.resp=requests.get(self.url,headers=self.header)

    def count(self):
        if self.resp.status_code==200:
            print('Success!\n')
        else:
            print('An error has occured',self.resp_code)
        self.soup=BeautifulSoup(self.resp.text,'html.parser')
        self.country=self.soup.find_all('h1')[0].text
        self.last_update=self.soup.find('div',{'style':'font-size:13px; color:#999; text-align:center'},{'Last updated:'})
        self.cases=self.soup.find_all('h1')[1].text
        self.deaths=self.soup.find_all('h1')[2].text
        self.recovered=self.soup.find_all('h1')[3].text
        self.count_cases=self.soup.find_all('div',{'class':'maincounter-number'})[0]
        self.count_deaths=self.soup.find_all('div',{'class':'maincounter-number'})[1]
        self.count_recovered=self.soup.find_all('div',{'class':'maincounter-number'})[2]

        print(self.country)
        print(self.last_update.string)
        print(self.cases,self.count_cases.select_one('span').text)
        print(self.deaths,self.count_deaths.select_one('span').text)
        print(self.recovered,self.count_recovered.select_one('span').text,'\n')

if __name__=='__main__':
    covid=Covid()
    covid.count()
