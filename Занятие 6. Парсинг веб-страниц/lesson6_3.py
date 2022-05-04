sp = [-1, 500, -2, 4, 5, 6, 7, -8, 9, 0, 433, -45]

res = filter(lambda x: x > 0, sp)
print(list(res))

res = map(lambda x:x*x, filter(lambda x:x>0, sp))
