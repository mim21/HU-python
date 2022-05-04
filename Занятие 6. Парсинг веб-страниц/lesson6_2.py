# sp = ['1', '2', '4', '5', '6', '7', '8', '9', '0']
sp = ["vasya", "Peter", "masha", "olya", "yan", "Gektor"]
sp2 = ["a","b","c","d"]

# s = 0
# for item in sp:
#     s += int(item)
def f(v,v2):
    return v.capitalize()+v2


# res = map(lambda x: x.capitalize(), sp)
res = map(f, sp, sp2)
print(sp)
print(list(res))