def count_vowels(sentence):
    total = 0
    for i in sentence:
        if i in 'aeuio':
            total += 1
    return total 

print(count_vowels("Hello world"))
print(count_vowels("Python"))