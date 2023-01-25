import time


def factorial(n):
    res = 1

    while n > 1:
        res *= n
        n -= 1
    return res


def factorial_r(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


def run():
    n = 500000
    comienzo = time.time()
    factorial(n)
    final = time.time()
    print("Esc1: ", final - comienzo)

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print("Esc2: ", final - comienzo)


if __name__ == '__main__':
    run()
