# dzpython   дз7

# * оформить как утилиту командной строки
# в качестве опции принимать имя файла с ключом -f и директорию сохранения с ключом -d
# пример запуска скрипта из консоли: dz.py -f image.png -d d:/images/loaded/
# без параметров запуска скрипт пусть сохраняет файл с названием как в ссылке, т.е. CyberEd_logo_black-1.png

import requests
import argparse


def args():
    parser = argparse.ArgumentParser('Img downloader')
    parser.add_argument('-f', '--file', required=False, help='file name')
    parser.add_argument('-d', '--directory', help='output folder')
    return parser.parse_args()


def finder(text: str):
    res = text.split('"><title>CyberEd - Образовательный центр по кибербезопасности</title>')[0].split('"')[-1]
    return res


res = requests.get('https://cyber-ed.ru')
if res.status_code == 200:
    s = res.text
    url = finder(s)

# file_name = 'CyberEd_logo_black-1.png'
# out_directory = 'C:/Users/user/AppData/Local/Temp/'

res = requests.get(url)
if res.status_code == 200:
    s = res.content

if __name__ == '__main__':
    options = args()

    if args().directory:
        f = open(f'{options.directory}/{options.file}', 'wb')
        f.write(s)
        f.close()
    elif args().file:
        f = open(f'{options.file}', 'wb')
        f.write(s)
        f.close()
    else:
        f = open(url.split('/')[-1], 'wb')
        f.write(s)
        f.close()
