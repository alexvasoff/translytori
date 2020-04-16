def cut_array(arr, n, side="right"):
    """Удаляет из массива N элементов с начала"""
    for _ in range(n):  # урезаем массив до блока начала
        if side == "right":
            arr.pop(0)
        elif side == "left":
            arr.pop()


arr = [1, 2, 3, 4, 5, 6, 7, 8]
cut_array(arr, 2, "left")
print(arr)