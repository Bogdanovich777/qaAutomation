import subprocess

s = 'adb devices'

f = subprocess.Popen(s, shell=True)

f.communicate(s)



#-s shell input 505 505