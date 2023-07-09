import argparse


def get_args():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", help="path to initial file")
    parser.add_argument("second_file", help="path to another file")
    parser.add_argument("-f", "--format",
                        help="output format, default='stylish'",
                        default='stylish'
                        )

    return parser.parse_args()
