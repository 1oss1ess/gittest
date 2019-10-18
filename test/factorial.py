def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num


def fibonacci(n):
    result = []
    a, b = 1, 1
    while n >= 1:
        result.append(a)
        a, b = b, a + b
        n -= 1
    return result
