#! ./venv/bin/python
import requests
import sys
import argparse


# import optparse
# aGVsbG8gZnJvbSBoYWNrZXJV


def finder(text: str):
    res = text.split('placeholder="Result goes here..." spellcheck="false">')[1].split('</textarea>')[0]
    print(res)


def args():
    parser = argparse.ArgumentParser("script to decode base64 string")
    parser.add_argument("-s", "--string", required=True, help="base64 string to decode to")
    parser.add_argument("-f", "--fake", help="fake field to say hello")
    parser.add_argument("-d", type=int)

    return parser.parse_args()

if __name__ == '__main__':

    # args = sys.argv  # base64_req.py
    options = args()
    params = {
        "input": f"{options.string}",
        "charset": "UTF-8"
    }

    res = requests.post("https://www.base64decode.org/", data=params)
    if res.status_code == 200:
        s = res.text
        finder(s)

    else:
        print("tarrible error")
    if options.fake:
        print("fake", options.fake)
    else:
        print("fake not set")
    if options.d:
        print(options.d)
