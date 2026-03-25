def sum_odd(nums):
    total = 0
    for i in nums:
        if i % 2 != 0:
            total += i
    return total

print(sum_odd([1, 2, 3, 4, 5]))
print(sum_odd([2, 4, 6]))