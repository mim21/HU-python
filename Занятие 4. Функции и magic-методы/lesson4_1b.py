f = open("foo.txt")  # rt
s = f.read(7)
s2 = f.read(5)
s3 = f.read()
s4 = f.read()
print(s)
print(s2)
print(s3)
pos = f.tell()
print(pos)
print("last", s4)
#===================
f.seek(5)
s5 = f.read()
print(s5)

# print(s.encode())
f.close()
