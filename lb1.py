from data import kw_keys, kw_val, separator, identity, value, general_array
from func import *
from meta import p_name, eng_abc, start_word, end_word

# --------------подготовка входного файла------------------#

file = open("text.txt", 'r', encoding="utf-8")  # открываем исходный файл в режиме чтения
wf = (file.read().split('\n'))  # массив из строк файла
lens = []
for line in wf:  # вывод слов в строке
    if line:  # убираем пустые строки
        a = line.split(' ')
        for word in a:
            for symbol in word:
                if symbol.isupper():  # проверка на отсутвтвие больших букв
                    error("Ошибка 0: Найдена большая буква в слове " + word)
                if symbol in eng_abc:  # проверка на отсутствие англ символов
                    error("Ошибка : Инородный символ в слове " + word)
        lens.append(a)

# ---------------------------------------------------------#
dprint("Входной текст в массивах: ", lens)

# -------------поиск точки входа в программу----------#

final_arr = []
for string in lens:  # определение точки входа в программу
    spw = start_word
    if (spw in string):
        final_arr.append(spw)
        start = lens.index(string)
        if (len(string)) > 2:
            error("Ошибка: Название программы указывается без пробела!")
        try:
            p_name = string[string.index(spw) + 1]
            final_arr.append(p_name)  # добавляем название программы
            identity.append(p_name)
        except Exception:
            pass
        cut_array(lens, start + 1)  # обрезаем массив на start элементов слева
        break
else:
    error("Ошибка 1: Не найдена точка входа! (слово 'программа')")
# -----------------------------------------------------------#
dprint("Название программы: ", p_name)
dprint("lens после найденного ПРОГРАММА: ", lens)
# ---------поиск строки начала и конец--------------------
sw = 'начало'
ew = end_word
for word in lens:
    if (sw in word):
        if len(word) == 1:
            final_arr.append(sw)
            start = lens.index(word)
            sw = ''
        else:
            error("Не верная конструкция начала")
    elif (ew in word):
        end = lens.index(word) + 1
        ew = ''
        break
if sw == "" and ew == "":
    pass
else:
    error('Ошибка 2: Ошибка в блоке определения программы (начало || конец)')
# ----------------------------------------------------------#

cut_array(lens, len(lens) - end, "right" )
cut_array(lens, start + 1)
dprint("Массив программного кода: " , lens)

# -----------работаем со словами в файле------------------#
for string in lens:
    for word in string:
        parse(word, final_arr)

# ------------------------------------------------------#
dprint('Финальный массив:', final_arr)
dprint('Массив значеинй:', value)
dprint('Массив идентификаторов: ', identity)

# ------------формирование дескриптора-----------#
print("Значимая структура входного кода:", final_arr)
print("Ключевые слова:", kw_keys)
print("Разделители:", separator)
print("Идентификаторы:", identity)
print("Константы:", value)
print("Формируем дескриптор:")
disc = []
for el in final_arr:
    if el in kw_keys:
        position = "кл. слово"
        id = kw_keys.index(el)
    elif el in separator:
        position = "разд."
        id = separator.index(el)
    elif el in identity:
        position = "идент."
        id = identity.index(el)
    elif el in value:
        position = 'конст.'
        id = value.index(el)
    else:
        error("Секретная ошибка, если она появилась, то все...")
    disc.append([position, id])
print(disc)
