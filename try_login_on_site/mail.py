import requests

url = 'https://e.mail.ru/login?from=portal'
s = requests.session()
r = s.get(url, verify=False)
act_token = r.cookies['act']
url2 = 'https://mail.ru/'


data = {
    'login' : 'alligatoro%40mail.ru',
    'password' : '37951qwedAnn',
#    'saveauth' : '1',
#    'new_auth_form' : '1',
#    'FromAccount' : 'opener%3Dmail.login%26allow_external%3D1',
#    'page' : 'https%3A%2F%2Fe.mail.ru%2Fmessages%2Finbox%3Fback%3D1%26back%3D1%26from%3Dmail.login',
    'act' : act_token,
#    'back' : '1',
#    'Domain' : 'mail.ru'
}

auth = s.post(url, data=data)

d = requests.get(url2, verify=False)
print(d.status_code)

print(d.text)


