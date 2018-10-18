import subprocess
import requests





url = 'https://artifactory.mgsn.it/webapp/#/builds/mycafe-client-android-git'

path = input(' пиши тут: ')

sss = requests.request("GET", 'https://artifactory.mgsn.it/webapp/#/builds/mycafe-client-android-git/{0}'.format(path))
rer = sss.url
print(rer)




f = open('D:/Melesta/QA/123.apk', 'wb')

number = input('Укажите № сборки: ')

asd = requests.get('https://artifactory.mgsn.it/mycafe-client-android/STAGE/release_v.2018.11/{0}/app-dualABI-release.apk'.format(number))


print(asd)


f.write(asd.content)

f.close()
