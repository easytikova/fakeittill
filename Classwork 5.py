# Определить время года по месяцу
x = input()
x = x.lower() # приводим все к нижнему регистру
#if x == "январь" or x == "декабрь" or x == "февраль":
#    print("зима")
#elif x == "сентябрь" or x == "ноябрь" or x == "октябрь":
#    print("осень")
#elif x == "март" or x == "апрель" or x == "май":
#    print("весна")
#elif x == "июнь" or x == "июль" or x == "август":
#    print("лето")
#else:
#    print("Не время года")

#if x in ['декабрь', 'январь', 'февраль']:
#    print("зима")
#elif x in ['сентябрь', 'октябрь', 'ноябрь']:
#    print("осень")
#elif x in ['март', 'апрель', 'май']:
#    print("весна")
#elif x in ['июнь', 'июль', 'август']:
#    print("лето")
#else:
#    print("не месяц и не время года")

if x in ['декабрь', 'январь', 'февраль']:
    season = "зима"
elif x in ['сентябрь', 'октябрь', 'ноябрь']:
    season = "осень"
elif x in ['март', 'апрель', 'май']:
    season = "весна"
elif x in ['июнь', 'июль', 'август']:
    season = "лето"
else:
    season = "не месяц и не время года"

if season != "не месяц и не время года":
    print(f"Время года - {season}")
else:
    print("Ошибка")


if 5 > 10:
    print("True")
else:
    print("False")

if 10 > 5:
    print("True")

if 2 * 2 == (6 - 2):
    print("True")

if "word" == "world":
    print("True")

if "word" != "world":
    print("True")

x = int(input())
if x % 2 == 0:
    print("chetnoe")
else:
    print("nechetnoe")

# Может ли человек голосовать?
age = int(input("Insert your age: "))
if age >= 18:
    print("You can vote!")
else:
    print("You can't vote :(")

# Содержит ли строчка текст? Если да, сколько в неё символов?
text = str(input())
if len(text) == 0: # Лучше начинать с 0
    print("Empty")
else:
    print("Text length is ", len(text))

# Является ли год високосным?
x = int(input("The year of "))
if (x%4 == 0 and x%100 != 0) or x%400 == 0:
    print(x, " is intercalary")
#   print(f"(year) is intercalary")
else:
    print("is common")

x = int(input())
if x > 0:
    print("Positive number")
elif x == 0:
    print("Negative number")
else:
    print("Zero")

# Равенство треугольника
a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print("Равносторонний")
elif (a == b and b != c) or (a != b and b == c) or (b != c and c == a):
    print("Равнобедренный")
elif a != b and b != c:
    print("Разносторонний")

