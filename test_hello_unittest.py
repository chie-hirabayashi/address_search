import unittest


def add(x, y):
    return x + y


def subtraction(x, y):
    return x - y


class MyTestCase(unittest.TestCase):
    def test_2つの整数の和が計算できる(self):
        self.assertEqual(7, add(3, 4))

    def test_2つの整数の差が計算できる(self):
        self.assertEqual(1, subtraction(4, 3))


if __name__ == "__main__":
    unittest.main()
