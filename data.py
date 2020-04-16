from meta import start_word, end_word
# объявим словарь ключевых слов:
key_word_dict = {"пока": "while", "для": "for", "целое": "int", "строка": "str", "символ": "char", "дробь": "float",
                 "флаг": "bool", "иначе": "else", "если": "if", "начало": "begin", "конец": "end",
                 start_word: "program", end_word:"end",
                 "от": "xxx", "диапозон": "range", "массив": "array", "добавить": "append", "синус": "sin", "косинус": "cos", "тангенс": "tg", "экспонента": "exp"}

# объявим массив разделителей:
separator = [";", "+", "-", "/", "*", ":", "=", ".", "[", "]", '{', '}', "(", ")"]

identity = []  # объявление массива идентификации (названий переменных и тд)
value = []  # объявление массива значений, которые принимают переменные (идентификаторы)

kw_keys = list(key_word_dict.keys())  # массив ключей ключевых слов
kw_val = list(key_word_dict.values())  # массив значений ключевых слов

general_array = kw_keys + separator + identity
