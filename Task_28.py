# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def get_check_console(text=""):
    result = -1
    while result < 0:
        try:
            result = int(input(text))
            if result < 0:
                print("Нужно число >= 0")
            else:
                break
        except ValueError:
            print("Пожалуйста введите число!")
    return result

first_num = get_check_console("Введите число А: ")
second_num = get_check_console("Введите число B: ")

def Summa(a: int, b: int):

    if b == 0:
        return a
    else:
        return Summa(a + 1, b - 1)

print("Результат:", end=" ")
print(Summa(first_num, second_num))
