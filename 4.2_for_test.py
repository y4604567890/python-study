a = range(5);
for i in range(len(a)):
    print(i ** 2)

# A try statement’s else clause runs when no exception occurs,
# and a loop’s else clause runs when no break occurs.
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
