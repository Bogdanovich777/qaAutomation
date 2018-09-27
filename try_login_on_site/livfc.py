# coding: UTF-8

import requests
import urllib.request
from bs4 import BeautifulSoup


# class livfc():


def auth():
    url = 'http://www.liverpoolfc.ru/viyti/voyti'
    session = requests.Session()
    params = {
        'username': 'All777',
        'passwd': '37951qwed',
        'submit': '%D0%92%D1%85%D0%BE%D0%B4',
        'option': 'com_user',
        'task': 'login',
        'return': 'aW5kZXgucGhw&d795097f221a9c09b0b59eb5bfc3e37a=1'

    }

    r = session.post(url, data=params)
    # print(r.text)


print('DONE!')


def get_html(url2):
    response = urllib.request.urlopen(url2)
    return response.read()


def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    button = soup.find('Предыдущий матч', '#left_mods > div > div:nth-child(1) > h3.notice')
    print(button)



def main():
    parse(get_html('http://www.liverpoolfc.ru'))


# livfc.auth
# main()
auth()
main()


# livfc = livfc()

# livfc.auth
# livfc.main()

