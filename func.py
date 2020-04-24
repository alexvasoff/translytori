from data import *
from settings import _DEBUG, _DUPLICATE



def error(description):
    print(description)
    print("Программа прервана!")
    exit(0)


def cut_array(arr, n, side="left"):

    """
    Удаляет из массива N элементов с начала
    :param arr: изменяемый массив
    :param n: кол-во символов на срез
    :param side: с какой стороны двигаемся
    :return:
    """
    for _ in range(n):  # урезаем массив до блока начала
        if side == "left":
            arr.pop(0)
        elif side == "right":
            arr.pop()


def dprint(*str):
    if _DEBUG:
        print(*str)


def detection(symb):
    """
    Определяет тип лексемы
    :param symb: лексема
    :return:
    """
    try:
        int(symb)
        if _DUPLICATE:
            value.append(symb)
        else:
            if symb not in value:
                value.append(symb)
    except:
        if _DUPLICATE:
            identity.append(symb)
        else:
            if symb not in identity:
                identity.append(symb)


def parse(ch_word, final_arr):
    """
    Анализирует слово и решает его судьбу
    :param ch_word: слово для проверки
    :param final_arr: массив куда добавляется сырое слово
    :return:
    """
    unknow = ''
    while len(ch_word) > 0:
        dprint("Cмотрим слово:", ch_word)
        for el in general_array:
            if ch_word.startswith(el):
                if len(unknow) > 0:
                    final_arr.append(unknow)
                    detection(unknow)
                    unknow = ''
                dprint("Нашли нужный элемент: ", el)
                if len(ch_word) == len(el):
                    dprint("Слово унарно, добавляем его в массив! ", ch_word)
                    final_arr.append(ch_word)
                    ch_word = ch_word[len(el):]
                else:
                    if ch_word[len(el)] in separator or el in separator:
                        dprint("Элемент подходит, но слово имеет еще всякие штуки, добавляем в массив ", el)
                        final_arr.append(el)
                        ch_word = ch_word[len(el):]
                        dprint('Теперь мы отправляем на проверку новое слово: ', ch_word)
                    else:
                        unknow += ch_word[:len(el)]
                        ch_word = ch_word[len(el):]
                        # если необходимо недопускать син*** и тд, когда есть син(ключевое слово): error("Ошибка 3: что-то не так в слове: " + el)
                break
        else:
            unknow += ch_word[0]
            ch_word = ch_word[1:]
    if len(unknow) > 0:
        final_arr.append(unknow)
        detection(unknow)
