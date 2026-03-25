def find_max(numbers):
    max_num = numbers[0]
    for i in numbers:
        if i > max_num :
            max_num = i 
    return(max_num)

numbers = input()
print(find_max(numbers))