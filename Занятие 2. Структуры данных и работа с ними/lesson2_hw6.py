#dzpython2 ===================================== дз2 ================
# ** сделайте задание * в одну строку внутри print(<весь код здесь>)
# ВО ВСЕХ ЗАДАНИЯХ ВЫШЕ ФУНКЦИИ max и SORT ИСПОЛЬЗОВАТЬ НЕЛЬЗЯ

s = 'abhcdefg'
max_char = s[0]

# result = (s[i + 1] for i in range(len(s) - 1) if max_char < s[i + 1])
result = (s[i] for i in range(len(s) - 1) if s[i] > max_char)

print(list(result))


