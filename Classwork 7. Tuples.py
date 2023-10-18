# Кортеж - неприкасаемый тип данны, в отличие от списков
sample = (0, "dog", {0: "dog"})
sample = 0, "dog", {0: "dog"},
print(sample)

sample_dict = {0: "dog", 1: "cat"}
print(type(sample_dict))
sample_dict[0]
sample_dict[1]
dict = dict()
dict[0] = "dog"
dict[1] = "cat"

### СЛОВАРИ ###
a = [0, 1, 2]
for i in a:
    print(i)

a = 'strings'
for i in a:
    print(i)

# со словарями не сработает!
a = {"key": 90, "key0": 99}
for i in a:
    print(i)
# выведуться только ключи. Значения - нет. Для этого:
for key, value in a.items():
    print(key, value)

for value in a.values():
    print(value)

### МНОЖЕСТВА ###
a = {0, 0, 0, 1}
print(a)

a.add(8) # добавить элемент
print(a)

a = frozenset(a) # замораживаем множество
print(a)
a.add('bird')  # ща будет ошибка
print(a)

