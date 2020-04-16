from data import kw_keys, kw_val, separator, identity, value, general_array
from func import *
from meta import p_name, eng_abc

# --------------подготовка входного файла------------------#

file = open("text.txt", 'r', encoding="utf-8")  # открываем исходный файл в режиме чтения
wf = (file.read().split('\n'))  # массив из строк файла

words = []
for line in wf:  # вывод слов в строке
    if line:  # убираем пустые строки
        a = line.split(' ')
        words.append(a)
# ---------------------------------------------------------#

dprint("Входной текст в массивах: ", words)
# -----------проверка на маленькие буквы-------------------#
for string in words:
    for word in string:
        for symbol in word:
            if symbol.isupper():
                error('Ошибка 0: Найдена БОЛЬШАЯ буква. Так не пойдет! ' + word)
            elif symbol in eng_abc:
                error("Ошибка : Инородный символ в слове " + word)
# -------------------------------------------------------------#


# -------------поиск точки входа в программу----------#

final_arr = []
for word in words:  # определение точки входа в программу
    spw = 'программа'
    if (spw in word):
        final_arr.append(spw)
        start = words.index(word)
        try:
            p_name = word[word.index(spw) + 1]
            final_arr.append(p_name)  # добавляем название программы
            identity.append(p_name)
            start+=1
        except Exception:
            pass
        break
else:
    error("Ошибка 1: Не найдена точка входа!")
# -----------------------------------------------------------#
cut_array(words, start)  # обрезаем массив на start элементов слева
dprint("words после найденного ПРОГРАММА: ", words)
# ---------поиск строки начала--------------------

for word in words:
    dprint("Чекаем со строки" + str(word))
    sw = 'начало'
    if (sw in word):
        if len(word) == 1:
            final_arr.append(sw)
            start = words.index(word)
            break
        else:
            error("Не верная конструкция начала")
else:
    error('Ошибка 2: Не найден блок начала')
# ----------------------------------------------------------#
cut_array(words, start + 1)
# -----------работаем со словами в файле------------------#

for string in words:
    for word in string:
        parse(word, final_arr)
# ------------------------------------------------------#
dprint('Финальный массив:', final_arr)
dprint('Массив значеинй:', value)
dprint('Массив идентификаторов: ', identity)

# ------------формирование дескриптора-----------#

