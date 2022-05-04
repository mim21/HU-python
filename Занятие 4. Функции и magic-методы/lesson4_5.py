file = open('baz.txt', 'w')

ps = ['one hkjhk', 'two lkjijl', '3', 'end']
# file.write('foo')
# file.write('baz')

for line in ps:
    file.write(f'{line} \n')
file.writelines(ps)
file.write('\n'.join(ps))
file.close()

