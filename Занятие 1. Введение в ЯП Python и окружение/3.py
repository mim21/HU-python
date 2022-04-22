# ** решите задачу для произвольного количества чисел внутри одного print(...) (использовать сортировку можно),
# здесь числа вводятся в один input через пробел, т.е. так: 1 44 55 22 12 32 0 77...

a = input('Enter your numbers (space separated): ')
b = a.split(' ')
# convert each element of the list b into int
results = list(map(int, b))
results.sort()
print(results)
