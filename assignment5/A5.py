def remove_uneven(numbers):
    new_list = []
    for number in numbers:
        if number % 2 == 0:
            new_list.append(number)
    return new_list

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cut_down_list = remove_uneven(original_list)

print("Original list:", original_list)
print("Cut down list:", cut_down_list)