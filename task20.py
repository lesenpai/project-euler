def fact(n):
    f = 1
    for i in range(1,n+1): 
        f = f * i 
    return f


s = str(fact(100))
n = 0
for c in s:
    n += int(c)
print(n)