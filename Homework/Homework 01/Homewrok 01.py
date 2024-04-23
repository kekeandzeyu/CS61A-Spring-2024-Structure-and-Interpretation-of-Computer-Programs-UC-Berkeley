from operator import add, sub


def a_plus_abs_b(a, b):
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)


def two_of_three(i, j, k):
    return i * i + j * j + k * k - max(i, j, k) * max(i, j, k)


def largest_factor(n):
    for i in range(2, n - 1):
        if n % i == 0:
            return n // i


def hailstone(n):
    print(n)
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print(n)
        steps += 1
    return steps
