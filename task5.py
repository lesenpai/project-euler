def is_total_divided(x, numbers):
    for n in numbers:
        if x % n != 0:
            return False
    return True

# НОК
def lcm(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)
    

x = 1

for n in range(1, 21):
    x = lcm(x, n)
    print('x =', x)

print(x)
