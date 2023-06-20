from random import randint


def enterTask():
    str = int(input("Enter number of task (10 or 12 or 14 or 0 to exit): "))
    if str == 10:
        task10()
    elif str == 12:
        task12()
    elif str == 14:
        task14()
    elif str == 0:
        return
    else:
        print("It is wrong number!")
        enterTask()
    print("\n")
    enterTask()


# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2


def task10():
    n = int(input("Enter number of coins: "))
    a = 0
    b = 0
    for i in range(n):
        temp = (randint(0, 1))
        print(temp, end=' ')
        if temp == 0:
            a += 1
        else:
            b += 1
    if a > b:
        print(f"{b}")
    else:
        print(f"{a}")


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3


def task12():
    sum = int(input("Enter sum of number: "))
    mul = int(input("Enter mult of number: "))
    flag = False

    for i in range(sum + 1):
        if flag:
            break
        for j in range(mul + 1):
            if i*j >= 1000:
                print("out of range")
                flag = True
                break
            elif sum == i + j and mul == i * j:
                print(f"first number: {i}, second number: {j}")
                flag = True
                break


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.
# 10 -> 1 2 4 8


def task14():
    num = int(input("Enter number: "))
    count = 1
    while count <= num:
        print(count, end=' ')
        count *= 2


enterTask()
