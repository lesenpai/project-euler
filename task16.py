""" 
2^15 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.

Какова сумма цифр числа 2^1000?
"""

n = 2**1_000
s = str(n)
sum_ = 0
for i in s:
    sum_ += int(i)
print(sum_)