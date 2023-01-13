# Задача 26:
# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

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

def get_result(a: int, b: int):
    if b == 0:
        return 1
    if b == 1:
        return a
    else:
        return a * get_result(a, b - 1)
print("Ответ:", end=" ")
print(get_result(first_num, second_num))



