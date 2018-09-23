# coding: UTF-8

import requests
import bs4


class livfc():



    def auth(self):
        url = 'http:\\www.liverpoolfc.ru\viyti\voyti'
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
        print(r.text)



if __name__ == '__main__':
    livfc = livfc()
    livfc.auth







