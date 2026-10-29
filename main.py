from functions import sum_digits, average, normalize_text, select_numbers
def main():
    try:
        num_input = input("Введите целое число для суммы цифр: ")
        number = int(num_input)
        print(f"Сумма цифр: {sum_digits(number)}")
    except ValueError:
        print("Ошибка: нужно было ввести целое число.")

    print("-" * 20)

    numbers_input = input("Введите числа через пробел: ")
    numbers_list = [int(x) for x in numbers_input.split() if x]
    
    avg_result = average(numbers_list)
    if avg_result is None:
        print("Нет данных")
    else:
        print(f"Среднее арифметическое: {avg_result}")

    print("-" * 20)

    text_input = input("Введите произвольный текст: ")
    print(f"Нормализованный текст: '{normalize_text(text_input)}'")

    print("-" * 20)

    if numbers_list:
        try:
            threshold_input = input("Введите порог для отбора чисел (неотрицательное целое): ")
            threshold = int(threshold_input)
            if threshold < 0:
                 print("Порог должен быть неотрицательным. Используем 0.")
                 threshold = 0
                 
            selected = select_numbers(numbers_list, threshold)
            print(f"Числа, модуль которых больше {threshold}: {selected}")
        except ValueError:
            print("Ошибка: порог должен быть целым числом.")
    else:
        print("Список чисел пуст, нечего фильтровать.")


if name == "main":
    main()
