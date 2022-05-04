f = open('foo.txt')
s = f.read(7)
s2 = f.read(5)
s3 = f.read()
s4 = f.read()
print(s)
print(s.encode())
print(s2)
print(s3)
f.close()
# сдвиг позиции
# f.seek(5)
print('last', s4)

