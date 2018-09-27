# coding: UTF-8

import bs4
import urllib.request
import requests


with requests.session() as c:
    url = 'http://www.liverpoolfc.ru/viyti/voyti'
    USER = 'All777'
    PASS = '37951qwed'

    c.get(url)
    toke = c.cookies['1']

    login_data = dict (username = USER, password = PASS, Submit = 'Вход', option = 'com_user', task = 'login',  = toke)
    c.post(url, data= login_data)

    page = c.get('http://www.liverpoolfc.ru/forum/viewtopic.php?f=24&t=974')

    print(page.content)
