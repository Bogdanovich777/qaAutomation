import requests
from bs4 import BeautifulSoup


url = 'http://6.pogoda.by/' # url

r = requests.get(url)


with open('pogoda.html', 'wb') as file:
    file.write(r.text.encode('cp1251'))     #Сохранили страничку в виде HTML



file = open('pogoda.html', 'rb')
soup = BeautifulSoup(file, 'lxml')

pogoda_list = soup.find("table", attrs={"id":"forecast"})
#pogoda2 = soup.find_all('tr')[9]
file.close()

#print(pogoda_list)
with open('pogoda.html', 'wb') as file:
    file.write(pogoda_list.encode('cp1251'))

file = open('pogoda.html', 'rb')
soup_result = BeautifulSoup(file, 'lxml')
pogoda_s = soup_result.find('b')
file.close()

print(pogoda_s)

with open('pogoda_result.html', 'wb') as file:
    file.write(pogoda_s.encode('cp1251'))

#file = open('pogoda.html', 'rb')
#soup_result = BeautifulSoup(file, 'lxml')
#pogoda_s = soup_result.find_all('b')
#file.close()

#print(pogoda_s)


#new_file = open('123.html', 'rb')
#soup2 = BeautifulSoup(new_file, 'lxml')
#pogoda2 = soup.find_all('tr')[6]

#with open ('lit.html', 'wb') as new:
#    new.write(pogoda2.encode('cp1251'))
#    new.close()

#soup3 = BeautifulSoup(new, 'lxml')
#pogoda3 = soup







