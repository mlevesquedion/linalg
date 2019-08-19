import itertools
import operator


def zip_with(f, a, b):
    return (f(ai, bi) for ai, bi in zip(a, b))


def dot_product(x, y):
    return zip_with(operator.mul, x, y)


def scalar_product(x, n):
    return dot_product(x, itertools.repeat(n))
