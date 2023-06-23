import random


def enterTask():
    str = int(input("Enter number of task (16 or 18 or 20 or 0 to exit): "))
    if str == 16:
        task16()
    elif str == 18:
        task18()
    elif str == 20:
        task20()
    elif str == 0:
        return
    else:
        print("It is wrong number!")
        enterTask()
    print("\n")
    enterTask()
# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1
def task16():
    print("start task16")
    num = int(input("enter number of elements: "))
    list_num = [random.randint(1, 10) for i in range(num)]
    print(list_num)
    search_num = int(input("enter search number of list: "))
    count = 0
    for i in list_num:
        if i == search_num:
            count += 1
    print(f"{count} matches")
    print("end task16")
# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5
def task18():
    print("start task18")
    num = int(input("enter number of elements: "))
    list_num = [random.randint(1, 10) for i in range(num)]
    print(list_num)
    closest_number = int(input("enter number: "))
    min_element = abs(closest_number - list_num[0])
    index_list = 0
    for i in range(1, num):
        cur_element = abs(closest_number - list_num[i])
        if cur_element < min_element:
            min_element = cur_element
            index_list = i
    print(list_num[index_list]) 
    print("end task18")
# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
# Ввод:
# ноутбук
# Вывод:
# 12
def task20():
    print("start task20")

    list_letters = {1:"AEIOULNSTRАВЕИНОРСТ",
                2:"DGДКЛМПУ",
                3:"BCMPБГЁЬЯ",
                4:"FHVWYЙЫ",
                5:"KЖЗХЦЧ",
                8:"JXШЭЮ",
                10:"QZФЩЪ"}
    str = input("enter word: ").upper()
    sum_point = 0
    for i in str:
        for key, value in list_letters.items():
            if i in value:
                sum_point += key
    print(sum_point)
    print("end task20")
# 
# 
enterTask()
