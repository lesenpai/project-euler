import locale as lc
import time

lc.setlocale(lc.LC_ALL, 'en')

def collatz_len(i):
    seq = []
    while i != 1:
        if i%2==0:
            i/=2
        else:
            i=3*i+1
        seq.append(i)
    return len(seq) + 1

buf={}
def collatz_len_decor(i):
    i_orig = i
    counter = 1
    while i != 1:
        if i%2==0:
            if i in buf:
                counter += buf[i]-1
                break
            else:
                i/=2
        else:
            if i in buf:
                counter += buf[i]-1
                break
            else:
                i=3*i+1
        counter += 1
    buf[i_orig] = counter
    return counter

# for x in [13,10,20]:
#     print(collatz_len(x))    
# print()
# for x in [13,10,20]:
#     print(collatz_len_decor(x))

limit = 1_000_000
max_len = 0
number = None
no_decor_time = None
with_decor_time = None

# time_start = time.time()
# for x in range(1, limit):
#     cur_len = collatz_len(x)
#     # print('[no-decor] x={:,}'.format(x), ' len=', cur_len, sep='')
#     if cur_len > max_len:
#         max_len = cur_len
#         number = x

# # print('no decor:'.ljust(16) + 'n={} len={} time={}'.format(number, max_len, time.time() - time_start))
# no_decor_time = time.time() - time_start

# max_len = 0
time_start = time.time()
for x in range(1, limit):
    cur_len = collatz_len_decor(x)
    # print('[decor] x={:,}'.format(x), ' len=', cur_len, sep='')
    if cur_len > max_len:
        max_len = cur_len
        number = x

# print('decor:'.ljust(16) + 'n={} len={} time={}'.format(number, max_len, time.time() - time_start))
with_decor_time = time.time() - time_start

print('max_len={} number={}'.format(max_len, number))
# print('no decor time:', no_decor_time)
print('[decor] time:   ', with_decor_time)