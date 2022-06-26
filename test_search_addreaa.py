import unittest
from search_address import search_address



class MyTestCase(unittest.TestCase):
    def test_郵便番号から住所を取得できる_0287111(self):
        pos_code = "0287111"
        address = search_address(pos_code)

        expect = "岩手県八幡平市大更"

        self.assertEqual(expect, address)

    def test_郵便番号から住所を取得できる_0292501(self):
        pos_code = "0292501"
        address = search_address(pos_code)

        expect = "岩手県気仙郡住田町上有住"

        self.assertEqual(expect, address)


if __name__ == "__main__":
    unittest.main()
