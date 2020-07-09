import math as m

def divisors(n): 
    i = 1
    res = []
    while i <= m.sqrt(n): 
        if n % i == 0:   
            if n / i == i: 
                res.append(i)
            else: 
                res.extend([i, int(n/i)])
        i += 1
    return sorted(res)[:-1]

limit = 10_000

total = 0
for a in range(limit):
    b = sum(divisors(a))
    if b > a: # wow info
        db = sum(divisors(b))
        if db == a:
            total += a+b
print(total)
