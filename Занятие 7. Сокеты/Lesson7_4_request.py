import requests


# headers = {
#     "UserAgent": "Mozilla"
# }
params = {
    "text": "python",
    "lr": "213"
}
#                    https://yandex.ru?text=python&lr=213
res = requests.get("https://yandex.ru", params=params)
# res = requests.get("https://yandex.ru")
print(res)
print(res.text)






