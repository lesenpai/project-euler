digits = {
    0: 'zero', 
    1: 'one', 
    2: 'two',
    3: 'three', 
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven', 
    8: 'eight', 
    9: 'nine' 
}

n11to19 = {
    11: 'eleven', 
    12: 'twelve',
    13: 'thirteen', 
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen', 
    18: 'eighteen', 
    19: 'nineteen'
}

decs = {
    10: 'ten', 
    20: 'twenty', 
    30: 'thirty', 
    40: 'forty',
    50: 'fifty', 
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety', 
}


def num_to_word(n: int):
    if n < 10:
        return digits[n]
    if n < 100 and n % 10 == 0:
        return decs[n]
    if n < 20:
        return n11to19[n]
    if n < 100: # a-b
        s = str(n)
        return decs[int(s[0]+'0')] + '-' + digits[int(s[1])]
    if n < 1000 and n % 100 == 0:
        s = str(n)
        return digits[int(s[0])] + ' hundred'
    if 100 < n < 1000:
        s = str(n)
        return digits[int(s[0])] + ' hundred and ' + num_to_word(int(s[-2:]))
    if n == 1000:
        return 'one thousand'

l = 0
for n in range(1, 1001):
    print(n, '=', num_to_word(n))
    l += len(num_to_word(n).translate(str.maketrans({' ': '', '-': ''})))
print(l)