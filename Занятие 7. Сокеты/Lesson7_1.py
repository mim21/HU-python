try:
    a = 123
    b = input("b=")
    b = int(b)
    c = a / b
    print(c)
except Exception as e:
    print(e)
finally:
    print("finally")
print('end')
