import argparse

from gendiff.engine import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configurationfiles and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f", "--format", help="set format of output", default="stylish"
    )

    args = parser.parse_args()

    try:
        diff = generate_diff(args.first_file, args.second_file, args.format)
        print(diff)
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
