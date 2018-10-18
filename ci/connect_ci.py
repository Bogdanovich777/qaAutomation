import subprocess
import requests







f = open('D:/Melesta/QA/123.apk', 'wb')

number = input('Укажите № сборки: ')

asd = requests.get('https://artifactory.mgsn.it/mycafe-client-android/STAGE/release_v.2018.11/{0}/app-dualABI-release.apk'.format(number))


print(asd)


f.write(asd.content)

f.close()
