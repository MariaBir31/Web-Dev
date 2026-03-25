x = input()

result = 0

for digits in x:
    result = result * 2 + int(digits)

print(result)