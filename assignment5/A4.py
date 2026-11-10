def sum_of_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

my_list = [10, 20, 30, 40, 50]
result = sum_of_list(my_list)
print("Total numbers in list:", result)