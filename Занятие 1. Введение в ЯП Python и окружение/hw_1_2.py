# *пользователь вводит три числа
# для заданий выше сортировку и подобные функции не используем
a = int(input('enter number 1: '))
b = int(input('enter number 2: '))
c = int(input('enter number 3: '))

d = [a, b, c]

for i in range(len(d)):
    print(min(d))
    d.remove(min(d))
