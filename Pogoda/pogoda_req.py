import requests
from bs4 import BeautifulSoup
import lxml

url = 'http://pogoda.by/'

r = requests.get(url)


with open ('pogoda.html', 'wb') as file:
    file.write(r.text.encode('utf-8'))     #Сохранили страничку в виде HTML
    file.close()


file = open('pogoda.html', 'rb')
print(file)
soup = BeautifulSoup(file, 'lxml')

pogoda_list = soup.find_all("div", attrs={"id":"header"})
# pogoda_list = soup.select("table")

print(pogoda_list)
#with open ('123.html', 'wb') as new_file:
#    new_file.write(pogoda_list.encode('utf-8'))
#    new_file.close()






