# "Счастливым" называют билет с номером, в котором сумма первой половины цифр равна сумме
# второй половины цифр. Номера могут быть произвольной длины. Единственное условие — количество цифр всегда четно,
# например: 33 или 2341.
# Билет с номером 385916 — счастливый, так как 3 + 8 + 5 == 9 + 1 + 6.
# Билет с номером 231002 не является счастливым, так как 2 + 3 + 1 != 0 + 0 + 2.

# Реализуйте функцию is_happy_ticket(), проверяющую является ли номер счастливым (номер — всегда строка).
# Функция должна возвращать True, если билет счастливый, или False, если нет.
ticket = '329654'# задаем переменную и ее значение
def is_happy_ticket(ticket):# задаем функцию, в которой значение переменной
    return any(sum(map(int, ticket[i:])) == sum(map(int, ticket[:i] )) for i in range(len(ticket)))
    # возвращаем: any(iterable) - проверяет, есть ли хотя бы один истинный элемент в итерируемом объекте.
    # Если хотя бы один элемент равен True, функция any() возвращает True.
    # sum() позволяет сложить числа из списка или переданных, как аргумент функции (ticket).
    # map() - для применения функции к каждому элементу итерируемого объекта: список, кортеж, словарь
    # и возврата нового итератора для полученных результатов.
    # int, ticket - int преобразует строку в числовое значение.
    # цикл for складывает сумму чисел в длине len() билета, для каждой половины ранее указанной суммы.
    # range диапазон от длины списка len(ticket).
print(is_happy_ticket(ticket))

# нужно проверить, что длина строки четная, разделить строку на две половины, подсчитать сумму каждой половины,
# посчитать сумму каждой половины. Сравнить суммы двух половин и вернуть True or False.
def is_lucky_ticket(ticket:str):
    if len(ticket)%2 != 0:# Проверяем, что длина строки четная. Если не делится на 2 без остатка !=0,
        return False      # то значение нечетное, False.
    half_length = len(ticket)//2 # Разделяем строку по длине на две половины(используем целочисленное деление
    first_half = ticket[:half_length] # на 2(//2) для нахождения половины строки).
    second_half = ticket[half_length:]
    sum_first_half = sum(int(digit) for digit in first_half)# Подсчитаем сумму цифр каждой половины: преобразуем
    sum_second_half = sum(int(digit) for digit in second_half)# каждую цифру в int  и суммируем их.
    return sum_first_half == sum_second_half# Сравниваем суммы первой и второй половины цифр.
print(is_lucky_ticket('555555'))
print(is_lucky_ticket('555675'))
print(is_lucky_ticket('5555'))
print(is_lucky_ticket('35555554'))
