import urllib.request

res = urllib.request.urlopen('https://yandex.ru')
response = res.read()
print(response.decode)
