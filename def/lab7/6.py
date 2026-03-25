def sum_even(nums):
    sum = 0
    for i in nums:
        if i % 2 == 0:
            sum += i
    return sum 

print(sum_even([1, 2, 3, 4, 5, 6]))  # 12
print(sum_even([1, 3, 5]))  

# def count_words(words):
#     cnt = 0
#     for i in words:
#         if i == " ":
#             cnt += 1
#     return(cnt + 1)


# def count_words(words):
#     return len(words.split())