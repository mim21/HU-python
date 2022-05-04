names = ["Masha",
         "vasya",
         "peter",
         "kolya",
         "olya", "Li", "navooohodonosor", "yan"]

a = map(lambda x: x.capitalize(), filter(lambda x: len(x) > 3, names))
# kohavit vmesto list
print(*a)
