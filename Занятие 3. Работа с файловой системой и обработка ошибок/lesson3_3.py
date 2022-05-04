
s = "мама мыла раму"
d = {}
for letter in s:
    if letter in d:
        d[letter] += 1
    else:
        d[letter] = 1

print(d)
