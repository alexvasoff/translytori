from meta import start_word, end_word

# объявим словарь ключевых слов:
key_word_dict = {"пока": "while", "для": "for", "диапазон": "range", "пропуск": "pass", "прервать": "break",
                 "целое": "int", "строка": "str", "символ": "char", "дробь": "float", "флаг": "bool",
                 "если": "if", "иначе": "else",
                 start_word: "program", "начало": "begin", end_word: "end",
                 "массив": "array", "добавить": "append", "индекс": "index", "сорт": "sort", "очитс": "clear",
                 "син": "sin", "кос": "cos", "танг": "tg", "эксп": "exp"}

# объявим массив разделителей:
separator = [";", "+", "-", "/", "*", ":", "=", ".", "[", "]", '{', '}', "(", ")"]

identity = []  # объявление массива идентификации (названий переменных и тд)
value = []  # объявление массива значений, которые принимают переменные (идентификаторы)

kw_keys = list(key_word_dict.keys())  # массив ключей ключевых слов
kw_val = list(key_word_dict.values())  # массив значений ключевых слов

general_array = kw_keys + separator + identity
