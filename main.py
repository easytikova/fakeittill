#print("Hello world!")

#a = 5+7
#b = a
#print(b)

#a = int(input())
#b = a
#b = a + 7
#print(b)

#a = [1, 2, 3, 4, "5"]
#first_element =  a[0]
#print(first_element)
#reat = a[1:]
#print(reat)
#first_element, *other_elements = a #the same but in one string
#print(first_element)
#print(other_elements)

##Поработаем с датой
#date = (2023, 9, 27) #картеж
#year, month, day = date
#print(year)

##date = [2023, 9, 27] #то же самое, но списком
#year, month, day = date
#print(month)

a = 89
b = 31.02
c = "dog"
d = [89, "dog", 31.02]
print(type(c))
print(type(d), type(a))

var1, var2, var3, var4 = 89, "dog", 31.02, [89, "dog", 31.02]
print(var4)
print(type(var1), type(var2), type(var3), type(var4))
var1 = str(var1)
print(type(var1))
var2 = list(var2)
print(type(var2))

['d', 'o', 'g']

1
2
3
word1, word2, word3 = "dog", "cat", ""
print(word1)
a = [0, 0, 0]
b = [1, 1, 1]
c = [2, 2, 2]
a, b, c = c, a, b
print(a)
print(b)
print(c)


### МНОЖЕСТВЕННОЕ ПРИСВАИВАНИЕ И СПЛИТ ###
full_name = ["John", "Doe"]
name, surname = full_name
print(name)
print(surname)

full_name = "John Doe" #множественное присваивание
name, surname = full_name.split() #разделяем строчку. Самый простой способ токенизации слов (слово - набор символов от пробела до пробела)
print(name)
print(surname)

numbers = "1, 2, 3"
print(numbers.split(","))
print(numbers.split(", ")) #лучше ВСЕГДА так, без пробела

team = "John, Maria, Mark"
print(team.split(", "))

test = "one+two+three"
test = test.split("+")
print(test)

test = " this is a sentence"
print(test.split(" "))
for i in test: #i - каждый элемент, in - по какой штуке проводим операци.
    print(i)

test = test.split(" ")
for i in test:
    print(i)


### СЧЁТЧИК ###
new = [1, 2, 3]#это типа счётчик, но это что-то непонятное
for i in new:
    print(new)

n = 0
for i in new:
    n = n + 1
    print(n)


### РАСПАКОВКА ###
data = ['John', 'Doe', 36]
*first, second = data
print(first)

#a = int(input())
#b = int(input())
#print(a + b)
#print(a - b)

#a, b = int(input()), int(input())
#print(a*b)
#print(a/b)

#a, b = int(input()), int(input())
#print(a**b)

#a = int(input())
#b = int(input())
#c = int(input())
#print((a+b+c)/3) #как написать прогу, которая бы считала любое число ппеременных

n = 15
n += 4
print(n)

x = 9
y = 17
print(x < y)