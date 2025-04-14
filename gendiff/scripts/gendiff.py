import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument('-f', '--format', help="set format of output")
    args = parser.parse_args()

    # Пока просто проверка
    print(f"Comparing {args.first_file} and {args.second_file}")

if __name__ == "__main__":
    main()