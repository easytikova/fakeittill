name = "John"
age = 30
# Удобности
print("Hello, %s. You are %d years old." % (name, age))
print("Hello, {}. You are {} years old." .format(name, age))

print(len("John"))
print("Hello, world".split())
print("Hello, world".replace("world", "buddy"))
print(name.upper())
print(name.lower())

print("Hello, world. You are amazing".count("a"))
print("Hello, world. You are amazing".count(" "))

# Конкатенация строк
first = "Hello, "
second = "world"
sum = first+second
print(sum)

# Нечетные числа от 1 до 50
for i in range (1, 50, 2):
    print(i)

# Считаем факториал
num = int(input())
factorial = 1
for i in range (1, num+1):
    factorial *= i
    print(factorial)

# Таблица умножения
num = int(input())
if num < 10:
    for i in range (1, 10):
     print(f"{num} * {i} = {num * i}")
else:
    print("Это тебе не надо")

# Решаем квадратное уравнение
