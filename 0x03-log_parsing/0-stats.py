#!/usr/bin/python3
""" Script that reads stdin line by line and computes metrics """

import sys


def print_statistics(status_code_counts, total_file_size):
    """ Prints information """
    print("File size: {:d}".format(total_file_size))
    for status_code, count in sorted(status_code_counts.items()):
        if count != 0:
            print("{}: {:d}".format(status_code, count))


def main():
    status_code_counts = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
    line_count = 0
    total_file_size = 0

    try:
        for line in sys.stdin:
            line_count += 1

            if line_count % 10 == 0:
                print_statistics(status_code_counts, total_file_size)

            split_line = line.split()

            try:
                file_size = int(split_line[-1])
                total_file_size += file_size
            except (ValueError, IndexError):
                pass

            try:
                status_code = split_line[-2]
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1
            except IndexError:
                pass

        print_statistics(status_code_counts, total_file_size)

    except KeyboardInterrupt:
        print_statistics(status_code_counts, total_file_size)
        raise


if __name__ == "__main__":
    main()
