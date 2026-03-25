def find_max(numbers):
    max_num = numbers[0]
    for i in numbers:
        if i > max_num:
            max_num = i
    return(max_num)


print(find_max([-1, -5, -3]))   
print(find_max([1, 5, 3, 9, 2]))
