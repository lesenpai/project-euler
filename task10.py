# Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.

# Найдите сумму всех простых чисел меньше двух миллионов.

def is_prime(n) : 

    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

limit = 2_000_000
prime_sum = 0

for x in range(limit):
    if is_prime(x):
        prime_sum += x

print(prime_sum)
