f = open("foo.txt")  # rt
sp = []
# for line in f:
#     print(line.strip())
#     sp.append(line.strip())

sp = [line.strip() for line in f]
print(sp)
f.close()
