# со звездочкой*: дан список - удалите все одинаковые элементы, если они больше 0

a = [2, 56, 2, -3, 500]
uniq_list = []
for i in a:
    if i not in uniq_list:
        uniq_list.append(i)
print(uniq_list)

