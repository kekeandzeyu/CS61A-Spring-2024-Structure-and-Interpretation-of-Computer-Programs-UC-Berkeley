# Homework 01 Guide

## 1. A Plus Abs B

  The problem here is `f` in the code is not a variable; instead 
  it is a function. If you notice that, then this is simple.

```Python
from operator import add, sub


def a_plus_abs_b(a, b):
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)
```

## 2. Two of Three

  What we need to do is to add the square of them all and subtract 
  the square of the largest one.

```Python
def two_of_three(i, j, k):
    return i * i + j * j + k * k - max(i, j, k) * max(i, j, k)
```

## 3. Largest Factor

  I believe on average it can save a lot of time if we enumerate from 2 
  to `n // 2 + 1` than from `n // 2 + 1` to 2.

```Python
def largest_factor(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return n // i
    return 1
```

## 4. Hailstone 

  Remember that if `n == 1`, the function should return 1. Don't forget 
  to print out the whole steps!

```Python
def hailstone(n):
    print(n)
    steps = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print(n)
        steps += 1
    return steps
```

  

   

  
