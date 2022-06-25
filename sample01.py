def double(number: int) -> int:
    """引数の2倍を返す関数"""
    return number * 2


def main():
    print(double(3))
    print(double.__doc__)
    print(__name__)


if __name__ == "__main__":
    main()

# defmainを設定しておくと、def main()はこのデータでのみ実行される
