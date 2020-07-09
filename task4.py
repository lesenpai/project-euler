""" Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. 
Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

Найдите самый большой палиндром, полученный умножением двух трехзначных чисел. """

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]
    
max_palindrome = -1

for a in range(100, 999):
    for b in range(100, 999):
        x = a * b
        if is_palindrome(x) and x > max_palindrome:
            max_palindrome = x

print(max_palindrome)

