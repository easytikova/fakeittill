# А. Индекс массы тела: программа принимает на вход вес пользователя в килограммах и рост в сантиметрах.
#    Посчитать индекс массы тела пользователя, записать его в переменную и вывести на экран.
weight = int(input())
height = int(input())
bmi = weight/((height/100)**2)
bmi = round(bmi, 1)
print(bmi)
if bmi > 18.5:
    if 18.5 <= bmi <= 24.9:
        print("Normal body weight")
    elif 25.0 <= bmi <= 29.9:
        print("Excess body weight")
    elif 30.0 <= bmi <= 34.5:
        print("Obesity, 1st degree")
    elif 35.0 <= bmi <= 39.9:
        print("Obesity, 2st degree")
    elif bmi >= 40.0:
        print("Obesity, 3rd degree")
else:
    print("Underweight")


# Б. Площадь прямоугольника: программа принимает на вход длину и ширину прямоугольника.
#    Посчитать площадь прямоугольника и вывести на экран.
lenght = int(input())
width = int(input())
s = lenght*width
print(s)


# В. Конвертер температур: программа принимает на вход температуру в градусах по Фаренгейту
#    и переводит значение в градусы по Цельсию.
f = float(input())
c = (f-32)/1.8
print(c)