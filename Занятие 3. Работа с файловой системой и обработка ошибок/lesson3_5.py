s = "мама мыла раму"
d = {}
for letter in s:
    d[letter] = d.setdefault(letter, 0) + 1

print(d)
