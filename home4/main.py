def enterTask():
    str = int(input("Enter number of task (22 or 24 or 0 to exit): "))
    if str == 22:
        task22()
    elif str == 24:
        task24()
    elif str == 0:
        return
    else:
        print("It is wrong number!")
        enterTask()
    print("\n")
    enterTask()

# Задача 22: Даны два неупорядоченных набора целых чисел
# (может быть, с повторениями). Выдать без повторений
# в порядке возрастания все те числа, которые
# встречаются в обоих наборах. Пользователь вводит 2 числа.
# n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит
# сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12


def task22():
    print("start task22")
    array_1 = []
    array_2 = []
    n = int(input("enter col elements of array_1: "))
    m = int(input("enter col elements of array_2: "))

    def FillArray(array, num, name):
        while num > 0:
            el = input(f"enter element of {name}: ")
            array.append(el)
            num -= 1

    FillArray(array_1, n, "array_1")
    FillArray(array_2, m, "array_2")

    array_1_set = set(array_1)
    array_2_set = set(array_2)
    print(" ".join(array_1_set))
    print(" ".join(array_2_set))

    # пересечение множеств
    print(" ".join(array_1_set & array_2_set))

    print("end task22")


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по
# окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растет N кустов. Эти кусты обладают разной
# урожайностью, поэтому ко времени сбора на них выросло различное
# число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического
# сбора черники. Эта система состоит из управляющего модуля
# и нескольких собирающих модулей. Собирающий модуль за один
# заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа
# ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

# 4 -> 1 2 3 4
# 9


def task24():
    import random
    print("start task24")
    bush = int(input("enter col bush: "))
    list = [random.randint(1, 10) for i in range(bush)]
    print(*list)

    sum = 0
    result = []

    for i in range(0, len(list)):
        if (i == len(list) - 1):
            sum = list[i] + list[i-1] + list[0]
            result.append(sum)
        else:
            sum = list[i] + list[i-1] + list[i+1]
            result.append(sum)

    result.sort()
    print(result[-1])
    print("end task24")


enterTask()
