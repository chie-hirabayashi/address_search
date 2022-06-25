"""
郵便番号7桁(0287111)を入力したら
岩手県八幡平市大更が出力される

python app.py
郵便番号<ハイフン無し>は？ 0287111
岩手県八幡平市大更
"""
from search_address import search_address


def main():
    # pos_code = input("郵便番号<ハイフン無し>は？")
    pos_code = "0287111"

    address = search_address(pos_code)

    print(address)


if __name__ == "__main__":
    main()
