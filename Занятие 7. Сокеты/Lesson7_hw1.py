# dzpython   дз7
# со страницы школы https://cyber-ed.ru/ найти и
# сохранить картинку https://cyber-ed.ru/wp-content/uploads/2022/03/CyberEd_logo_black-1.png (ссылка дана для ознакомления с картинкой, ссылк унужно спарсить самостоятельно!)
# в виде файла .png

import requests


def finder(text: str):
    res = text.split('"><title>CyberEd - Образовательный центр по кибербезопасности</title>')[0].split('"')[-1]
    return res


res = requests.get('https://cyber-ed.ru')
if res.status_code == 200:
    s = res.text
    url = finder(s)

res = requests.get(url)
if res.status_code == 200:
    s = res.content
f = open('CyberEd_logo_black-1.png', 'wb')
f.write(s)
f.close()
