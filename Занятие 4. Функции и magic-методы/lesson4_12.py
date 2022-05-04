sp = ['Li', 'Vasya', 'Peter']
salary = [342.43, 11, -342]
# 10 - minimum symbols in string
# 15 - maximum symbols in string
# s = '%10.15s : %.2f'
# s = '%10.15s : %8.2f'
# s = '%10.15s : % .2f'
s = '%+10.15s : %+.2f'
# s = '%-10.15s : %+.2f'
for i in range(len(sp)):
    print(s % (sp[i], salary[i]))
