import math as m
                                          
def triangular_number(n):
    return int(0.5*n*(n+1))
                                          
def divisors(n) : 
    i = 1
    res = []
    while i <= m.sqrt(n): 
        if n % i == 0:   
            if n / i == i: 
                res.append(i)
            else: 
                res.extend([i, int(n/i)])
        i += 1
    return sorted(res)

print(list(divisors(40)))

target = 500
i = 3
while True:
    x = triangular_number(i)
    ps_len = len(divisors(x))
    print('i={} x={} ps_len={}'.format(i,x,ps_len))
    if ps_len > target:
        print(x)
        break
    i += 1