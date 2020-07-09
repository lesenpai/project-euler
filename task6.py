def sum_of_squares(ns):
    sum_ = 0

    for n in ns:
        sum_ += n * n

    return sum_

def square_of_sum(ns):
    return sum(ns) ** 2

numbers = range(101)
print(square_of_sum(numbers) - sum_of_squares(numbers))