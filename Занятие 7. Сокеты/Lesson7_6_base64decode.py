import requests


def finder(text: str):
    res = text.split('placeholder="Result goes here..." spellcheck="false">')[1].split('</textarea>')[0]
    print(res)


params = {
    "input": "SGVsbG8gd29ybGQ=",
    "charset": "UTF-8"
}

res = requests.post("https://www.base64decode.org/", data=params)

if res.status_code == 200:
    s = res.text
    finder(s)

else:
    print('terrible error')
