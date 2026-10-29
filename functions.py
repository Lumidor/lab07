def sum_digits(number):
    """Возвращает сумму цифр модуля числа."""
    number = abs(number)
    total = 0
    while number > 0:
        total += number % 10
        number = number // 10
    return total

def average(numbers):
    """Возвращает среднее арифметическое списка или None, если список пуст."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

def normalize_text(text):
    """Приводит строку к нижнему регистру, убирает лишние пробелы по краям и между словами."""
    words = text.split()
    return " ".join(words).lower()

def select_numbers(numbers, threshold):
    """
    Возвращает новый список чисел, модуль которых больше порога (Вариант 3).
    Сохраняет порядок и повторы.
    """
    return [num for num in numbers if abs(num) > threshold]
