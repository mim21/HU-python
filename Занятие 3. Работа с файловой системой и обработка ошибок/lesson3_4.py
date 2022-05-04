s = "мама мыла раму"
d = {}.fromkeys(s, 0)
for letter in s:
    d[letter] += 1

print(d)
