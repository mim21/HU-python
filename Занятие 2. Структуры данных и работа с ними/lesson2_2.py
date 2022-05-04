s = 'mama mila mamu'
i = 0
lenth = len(s)
index = -1

while index < 0 and i < lenth:
    letter = s[i]
    if letter == 'r':
        index = i
    i += 1

print('index =', index)
