def square(x):
    return x * x


def cube(x):
    return x * x * x


def power(x, y):
    return x**y


def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)


if __name__ == "__main__":
    pass
