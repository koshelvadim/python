def enterTask():
    str = int(input("Enter number of task (2 or 4 or 6 or 8 or 0 to exit): "))
    if str == 2:
        task2()
    elif str == 4:
        task4()
    elif str == 6:
        task6()
    elif str == 8:
        task8()
    elif str == 0:
        return
    else:
        print("It is wrong number!")
        enterTask()
    enterTask()


# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)


def task2():
    print("Task2")
    number = input("Enter three - digit number: ")
    if len(number) == 3:
        sum = 0
        for i in number:
            sum += int(i)
        print(sum)
    else:
        print("Wrong number!")
        task2()


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10


def task4():
    print("Task4")
    number = int(input("Enter numbre %6 :"))
    if number % 6 == 0:
        print(f"Serg: {int(number / 6)}")
        print(f"Kate: {int(number / 6 * 4)}")
        print(f"Petr: {int(number / 6)}")
    else:
        print("Wrong number!")
        task4()


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no


def task6():
    print("Task6")
    str = input("Enter six - digit of ticket: ")
    if (len(str) == 6):
        sum1 = 0
        sum2 = 0
        for i in range(len(str) // 2):
            sum1 += int(str[i])
        for i in range(len(str) // 2, len(str)):
            sum2 += int(str[i])
        if (sum1 == sum2):
            print("YES")
        else:
            print("NO")
    else:
        print("Wrong number!")
        task6()

# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no


def task8():
    print("Task8")
    l = int(input("Enter l: "))
    h = int(input("Enter h: "))
    print(f"Chocolate is: {l}X{h}")
    z = int(input("Enter number of slices: "))

    def checkSlices(l, h, z):
        if l * h > z:
            return True
        else:
            return False

    if checkSlices:
        if l % z == 0 or h % z == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("Slice > Chocolate")


enterTask()
