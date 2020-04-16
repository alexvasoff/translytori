from data import kw_keys, kw_val, separator, identity, value, general_array
from func import *
from meta import p_name, eng_abc, start_word, end_word

# --------------подготовка входного файла------------------#

file = open("text.txt", 'r', encoding="utf-8")  # открываем исходный файл в режиме чтения
wf = (file.read().split('\n'))  # массив из строк файла
words = []
for line in wf:  # вывод слов в строке
    if line:  # убираем пустые строки
        a = line.split(' ')
        for word in a:
            for symbol in word:
                if symbol.isupper():  # проверка на отсутвтвие больших букв
                    error("Ошибка 0: Найдена большая буква в слове " + word)
                if symbol in eng_abc:  # проверка на отсутствие англ символов
                    error("Ошибка : Инородный символ в слове " + word)
        words.append(a)

# ---------------------------------------------------------#
dprint("Входной текст в массивах: ", words)

# -------------поиск точки входа в программу----------#

final_arr = []
for word in words:  # определение точки входа в программу
    spw = start_word
    if (spw in word):
        final_arr.append(spw)
        start = words.index(word)
        try:
            p_name = word[word.index(spw) + 1]
            final_arr.append(p_name)  # добавляем название программы
            identity.append(p_name)
        except Exception:
            pass
        cut_array(words, start + 1)  # обрезаем массив на start элементов слева
        break
else:
    error("Ошибка 1: Не найдена точка входа! (слово 'программа')")
# -----------------------------------------------------------#
dprint("Название программы: ", p_name)
dprint("words после найденного ПРОГРАММА: ", words)
# ---------поиск строки начала и конец--------------------
sw = 'начало'
ew = end_word
for word in words:
    if (sw in word):
        if len(word) == 1:
            final_arr.append(sw)
            start = words.index(word)
            sw = ''
        else:
            error("Не верная конструкция начала")
    elif (ew in word):
        end = words.index(word) + 1
        ew = ''
        break
if sw == "" and ew == "":
    pass
else:
    error('Ошибка 2: Ошибка в блоке определения программы (начало || конец)')
# ----------------------------------------------------------#

cut_array(words, len(words) - end, "right" )
cut_array(words, start + 1)
dprint("Массив программного кода: " , words)

# -----------работаем со словами в файле------------------#
for string in words:
    for word in string:
        parse(word, final_arr)

# ------------------------------------------------------#
dprint('Финальный массив:', final_arr)
dprint('Массив значеинй:', value)
dprint('Массив идентификаторов: ', identity)

# ------------формирование дескриптора-----------#
