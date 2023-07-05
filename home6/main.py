def enterTask():
    str = int(input("Enter number of task (30 or 32 or 0 to exit): "))
    if str == 30:
        task30()
    elif str == 32:
        task32()
    elif str == 0:
        return
    else:
        print("It is wrong number!")
        enterTask()
    print("\n")
    enterTask()

# Задача 30:  Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для получения
# n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15


def task30():
    print("start task30")
    first = 7
    diff = 2
    length = 5
    for i in range(length):
        print(first + i * diff, end=' ')
    print()
    print("end task30")


# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е.
# не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]


def task32():
    print("start task32")
    list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2,
              10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
    list_2 = []
    min = int(input("enter min range: "))
    max = int(input("enter max range: "))
    for i in range(len(list_1)):
        if list_1[i] >= min and list_1[i] <= max:
            list_2.append(i)
    print(list_2)
    print("end task32")


enterTask()
