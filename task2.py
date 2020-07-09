""" Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. 
Начиная с 1 и 2, первые 10 элементов будут:

                    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона. """

""" 
sum = 0
limit = 4_000_000
def fib()...#X
n = 0

while True:
    if not fib(n) > limit:
        sum += fib(n)
    else:
        break
    n++

print('sum =', sum)
 """
def fibonacci(n): 
    a = 1
    b = 2
    if n <= 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(2, n + 1): 
            c = a + b 
            a = b 
            b = c 
        return b

limit = 4_000_000
sum = 0
n = 0

while True:
    fib = fibonacci(n)
    if fib % 2 == 0:
        if not fib > limit:
            sum += fib
        else:
            break
    n += 1

print('sum =', sum)
# print(fibonacci(0))
# print(fibonacci(1))
# print(fibonacci(2))
# print(fibonacci(3))


