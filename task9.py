""" Тройка Пифагора """

""" 
a < b < c
a^2 + b^2 = c^2
a + b + c = 1000
"""

def triangle_sides(p):
    a = 1
    while a*2 < p:
        b = 1
        while a+b < p:
            if (p-2*a) > 0 and (p-2*b) > 0 and (2*a+2*b-p) > 0:
                c = p - (a + b)
                if a < b < c:
                    yield a, b, c
            b += 1
        a += 1

for a, b, c in triangle_sides(1000):
    if a*a + b*b == c*c:
        print(a,b,c, a*b*c)

