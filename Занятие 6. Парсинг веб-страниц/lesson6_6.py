import os

# res = os.system('dir /b')
# print(res)
import subprocess

subprocess.call('dir /b', shell=True)

res = subprocess.check_output(['dir', '/b'], shell=True)
print(res.decode('utf-8'))

res = subprocess.check_output('ipconfig')
print(res.decode("cp866"))
