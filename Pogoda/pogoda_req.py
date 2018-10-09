import requests
from bs4 import BeautifulSoup


url = 'http://6.pogoda.by/'

r = requests.get(url)


with open ('pogoda.html', 'wb') as file:
    file.write(r.text.encode('cp1251'))     #Сохранили страничку в виде HTML
    file.close()


file = open('pogoda.html', 'rb')
soup = BeautifulSoup(file, 'lxml')

pogoda_list = soup.find("table", attrs={"id":"forecast"})
pogoda2 = soup.find_all('tr')[9]


#print(pogoda_list)
with open ('pogoda.html', 'wb') as file:
    file.write(pogoda2.encode('cp1251'))
    file.close()

file = open('pogoda.html', 'rb')
pogoda3 = soup.find('tr')

print(pogoda3)




#with open ('pogoda.html', 'wb') as file:
#    file.write(pogoda3.encode('cp1251'))
#    file.close()
#new_file = open('123.html', 'rb')
#soup2 = BeautifulSoup(new_file, 'lxml')
#pogoda2 = soup.find_all('tr')[6]

#with open ('lit.html', 'wb') as new:
#    new.write(pogoda2.encode('cp1251'))
#    new.close()

#soup3 = BeautifulSoup(new, 'lxml')
#pogoda3 = soup







