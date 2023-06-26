"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*nums):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [num ** 2 for num in nums]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(nums, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    match filter_type:
        case 'odd':
            return [num for num in nums if num % 2 != 0]
        case 'even':
            return [num for num in nums if num % 2 == 0]
        case 'prime':
            filtered_nums = []
            for num in nums:
                if num > 1:
                    counter = 0

                    for divider in range(2, num // 2+1):
                        if num % divider == 0:
                            counter += 1

                    if not counter:
                        filtered_nums.append(num)

            return filtered_nums
