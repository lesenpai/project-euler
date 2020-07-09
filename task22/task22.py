import os

def alphabetSize(s: str):
    s=s.lower()
    n = 0
    for c in s:
        n += ord(c) - 96
    return n


if __name__ == "__main__":
    DIR = os.path.basename(os.path.dirname(__file__))
    with open(f'{DIR}\\names.txt', 'r') as file:
        data = file.read()
    data = data.replace('"', '')
    lst = data.split(',')
    lst.sort()

    for i in range(len(lst)):
        lst[i] = (i+1) * alphabetSize(lst[i])

    print(sum(lst))