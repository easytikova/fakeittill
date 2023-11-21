### Функция: сложить два числа
def add_numbers(x, y):
    """
    :param x: первое число (int)
    :param y: второе число (int)
    :return: сумма чисел x и y (int)
    """
    result = x + y
    return result

sum_result = add_numbers(3, 5)
print(sum_result)

### Функция: токенизация
def tokenizator(text):
    """

    :text: текст для токенизации (str)

    """
    words = text.lower().split()
    return words

tokenized_text = tokenizator('This is a sample sentence')
print(tokenized_text)   # ['this', 'is', 'a', 'sample', 'sentence']

### Функция: удалить стоп-слова из текста
def clean_text(text):
    """

    :text: текст для удаления стоп-слов (str)

    """
    # задаем список стоп-слов
    stopwords = ["the", "a", "and"]
    return [word for word in text if word.lower() not in stopwords]

print(clean_text(tokenized_text))   # ['this', 'is', 'sample', 'sentence']

### Функция: создать частотный словарь (2 варианта)
def count_word_frequencies(text):
    """

    :text: текст (str)
    :freq_dict: частотный словарь токенов текста (dict)

    """
    words = clean_text(tokenizator(text))
    freq_dict = dict((word, words.count(word)) for word in words)
    return freq_dict

print(count_word_frequencies('This is a sample sentence. This is a sample phrase.'))
# {'this': 2, 'is': 2, 'sample': 2, 'sentence.': 1, 'phrase.': 1}

def count_word_frequencies_alt(text):
    """

    :text: текст (str)
    :freq_dict: частотный словарь токенов текста (dict)

    """
    words = clean_text(tokenizator(text))
    word_frequencies = {}
    for word in words:
        if word in word_frequencies:
            word_frequencies[word] += 1
        else:
            word_frequencies[word] = 1
    return word_frequencies


print(count_word_frequencies_alt('This is a sample sentence. This is a sample phrase.'))
# {'this': 2, 'is': 2, 'sample': 2, 'sentence.': 1, 'phrase.': 1}


square = lambda x: x**2
print(square(5)) #25


#def for_loop(iterable, body_func):
#    iterator = iter(iterable)
#    while True:
#        current_element = next(iterator)
#        body_func(current_element)

#def func(i):
#     print(i ** 2)
#for_loop([0, 1, 2], func)
### посмотреть решение

s = "privet"
it = iter(s)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

r = range(5)
it = iter(r)
print(next(it))
# ...

# Генератор списка
a = [i**2 for i in range(1,6)]
print(a)

# Выражения-генераторы
b = (i**2 for i in range(1,6))
print('first')
for i in b:
    print(i)
print('second')
for i in b:
    print(i)


     