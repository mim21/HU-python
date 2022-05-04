# read bytes
f = open('1.png', 'rb')
byt = f.read()
print(byt)
f.close()
# write bytes
r = open('result.txt', 'wb')
r.write(byt)
r.close()
