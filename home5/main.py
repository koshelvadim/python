def enterTask():
    str = int(input("Enter number of task (26 or 28 or 0 to exit): "))
    if str == 26:
        task26()
    elif str == 28:
        task28()
    elif str == 0:
        return
    else:
        print("It is wrong number!")
        enterTask()
    print("\n")
    enterTask()

# Задача 26:  Напишите программу, которая на вход
# принимает два числа A и B, и возводит число А в
# целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def task26():
    print("start task26")
    a = int(input("Enter number A: "))
    b = int(input("Enter number B: "))

    def getPow(a, b):
        if b == 0:
            return 1
        else:
            return a * getPow(a, b -1)
    
    print(getPow(a, b))
    print("end task26")

# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
# *Пример:*
# 2 2
# 4
def task28():
    print("start task28")
    a = int(input("Enter number A: "))
    b = int(input("Enter number B: "))

    def getSum(a, b):
        if a == 0:
            return b
        else:
            return getSum(a - 1, b + 1)

    print(getSum(a, b))
    print("end task26")

enterTask()
