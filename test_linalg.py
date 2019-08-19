import linalg


def test_dot_product():
    x = [1, 2, 3]
    y = [4, 5, 6]
    expected = [1 * 4, 2 * 5, 3 * 6]
    assert list(linalg.dot_product(x, y)) == expected


def test_scalar_product():
    x = [1, 2, 3, 4]
    n = 5
    expected = [1 * 5, 2 * 5, 3 * 5, 4 * 5]
    assert list(linalg.scalar_product(x, n)) == expected
