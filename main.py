from src.solution import get_duplicates
import argparse


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-fn', '--file_name', type=str, default="companies.csv",
                        help='Input name of csv file with data')

    args = parser.parse_args()
    pairs = get_duplicates(args.file_name)
    [print(i) for i in pairs]


if __name__ == '__main__':
    main()
