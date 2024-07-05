# Назовем счастливыми те числа, сумма квадратов цифр которого, в результате ряда преобразований,
# превратятся в единицу.
# 7 : 7^2 = 49 : 4^2 + 9^2 = 97 : 9^2 + 7^2 = 130 : 1^2 + 3^2 + 0^2 = 10 : 1^2 + 0^2 = 1.
def sum_of_square_digits(digit):# вспомогательная функция, которая принимает число и возвращает квадрат его цифр
    result = 0
    while digit > 0:# пока число больше 0
        last = digit % 10
        result = result + (last * last)
        digit = digit // 10
    return result
def while_happy_number(digit):
    for _ in range(10):
        digit = sum_of_square_digits(digit)
        if digit ==1:
            return True
    return False
print(while_happy_number(7))
# 1)Возьмем любое положительное число;
# 2)Разделим число на цифры;
# 3)Возведем каждую цифру в квадрат и сложим результаты;
# 4)Повторим предыдущий шаг для полученной суммы;
# 5)Повторим этот процесс, пока либо не получим число 1, либо число, которое уже ранее встречалось в процессе.
def is_happy_number(num):
    def get_next(num): # Вычисляет следующее число в последовательности по описанному алгоритму.
        total_sum = 0
        while num > 0: # пока число больше 0
            num, figure = divmod (num, 10)
            total_sum += figure ** 2
        return total_sum
    seen = set()
    for _ in range(10): # ограничение в 10 итераций.
        if num == 1:
            return True
        num = get_next(num)
        if num in seen:
            return False
        seen.add(num)# добавление элементов в множество.
    return False
num = 19
result = is_happy_number(num)
if result:
    print(f"{num} is a happy number")
else:
    print(f"{num} is not a happy number")

# Число считается счастливым, если, начиная с этого числа и повторяя процесс замены числа суммой квадратов
# его цифр, в конце получаем 1. Если же цикл не приводит к 1 и зацикливается на других числах,
# то число не является счастливым.
# Для реализации функции is_wery_happy_number(), которая ограничивает количество итераций числом 10,
# можно следовать следующему алгоритму:
# Инициализировать переменную для хранения текущего числа.
# Повторять процесс суммирования квадратов цифр текущего числа.
# Проверять, получилось ли 1 или достигли ли мы 10 итераций.
# Возвращать True, если получено 1, и False в противном случае.
def is_wery_happy_number(n):
    def summ_of_squares(number): # Вспомогательная функция, которая принимает число (number)
                                 # и возвращает сумму квадратов его цифр.
        return sum(int(digit) ** 2 for digit in str(number))
         # сумма(целое число(цифра) возведена в степень 2 для каждой цифры в строке(number).
    for _ in range(10): # Цикл, который ограничивает количество итераций числом 10.
        # Нижнее подчеркивание _ используется как переменная-счетчик, которая не будет использоваться внутри
        # тела цикла. Нижний слэш вместо имени переменной.
        # В функции summ_of_squares() используется цикл for для отсчета итераций возведения в степень.
        n = summ_of_squares(n) # На каждой итерации обновляем значение n на сумму квадратов его цифр.
        # n - это наше число, которое мы проверяем, счастливое или нет.
        if n == 1: # Если на какой-то итерации получаем 1, возвращаем True.
            return True
    return False # Если по истечении 10 итераций 1 не получена, возвращаем False.
print(is_wery_happy_number(19))
print(is_wery_happy_number(2))
print(is_wery_happy_number(7))
print(is_wery_happy_number(1))
print(is_wery_happy_number(10))
print(is_wery_happy_number(1))