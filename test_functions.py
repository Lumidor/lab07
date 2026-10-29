from functions import average, normalize_text, sum_digits, select_numbers
assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""
control_list = [-5, 0, 2, 5]
threshold = 2
assert select_numbers(control_list, threshold) == [-5, 5]
assert select_numbers([], threshold) == []
assert select_numbers([2, -2, 3, -3], 2) == [3, -3]
assert select_numbers([5, 5, -5, 1], 2) == [5, 5, -5]
original_list = [-5, 0, 2, 5]
original_copy = original_list.copy()
select_numbers(original_list, 2)
assert original_list == original_copy
assert select_numbers([], 0) == []
actual_avg = average([1, 2])
expected_avg = 1.5
assert abs(actual_avg - expected_avg) < 1e-9
print("Все проверки пройдены успешно!")
