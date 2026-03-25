def  reverse_string(text):
    return text[::-1]

x = input()
print(reverse_string(x))


def reverse_string(text):
    result =""
    for i in text:
        result = i + result
    return result 
