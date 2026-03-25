def count_vowels(text):
    total = 0
    for i in text.lower():
        if i in 'aeiou':
            total += 1
    return total
 
 
print(count_vowels("HELLO"))
print(count_vowels("PYTHON"))