def digits(n):
    while n >= 10:
        yield n % 10
        n = n // 10
    yield n

def sum_of_digits_to_the_nth_power(n, last):
    return [i for i in range(2, last) if i == sum(d**5 for d in digits(i))]

def main():
    yep = sum_of_digits_to_the_nth_power(5, 100000000)
    print(yep)
    print(sum(yep))

main()