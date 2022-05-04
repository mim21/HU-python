f = open("foo.txt")  # rt
s1 = f.readline()
s2 = f.readline()
s3 = f.readline()

# strip \b of print (and spaces if any)
print(s1.strip())
print(s2)
print(s3)

