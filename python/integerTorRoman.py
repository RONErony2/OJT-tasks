# 25. Write a program to convert integers to Roman numbers.

def int_to_Roman(num):
    roman_data = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X',40:'LX', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M', 4000: 'M̅V̅', 5000: 'V̅', 9000: 'M̅X̅', 10000: 'X̅',}
    base = 1
    result = ""
    while num > 0:
        n = num%(10*base)
        num -= n
        res = ""
        if n != 0:
            while n not in roman_data:
                res += roman_data[base]
                n -= base
            res = roman_data[n] + res
        result = res + result
        base *= 10
    return result

num = int(input("Enter the integer : "))
print(int_to_Roman(num))