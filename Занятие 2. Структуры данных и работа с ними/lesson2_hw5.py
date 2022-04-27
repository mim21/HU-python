#dzpython2 ===================================== дз2 ================
# * найдите вторую "большую" букву в строке. Для строки "abhcdefg" ответ - "g"
# ВО ВСЕХ ЗАДАНИЯХ ВЫШЕ ФУНКЦИИ max и SORT ИСПОЛЬЗОВАТЬ НЕЛЬЗЯ

s = 'abhcdefg'
max_char = s[0]

for i in range(len(s) - 1):
    if max_char < s[i + 1]:
        max_char = s[i + 1]

s = s.replace(max_char, '')

max_char = s[0]
for i in range(len(s) - 1):
    if max_char < s[i + 1]:
        max_char = s[i + 1]
print(max_char)



