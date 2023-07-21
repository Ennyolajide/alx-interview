#!/usr/bin/python3

import sys

def print_statistics(status_code_counts, total_file_size):
    print("File size:", total_file_size)
    for status_code, count in sorted(status_code_counts.items()):
        if count != 0:
            print(f"{status_code}: {count}")

def main():
    total_file_size = 0
    status_code_counts = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }

    try:
        counter = 0
        for line in sys.stdin:
            parsed_line = line.split()
            if len(parsed_line) >= 10:
                counter += 1

                total_file_size += int(parsed_line[-1])  # file size
                code = int(parsed_line[-2])  # status code

                if code in status_code_counts:
                    status_code_counts[code] += 1

                if counter == 10:
                    print_statistics(status_code_counts, total_file_size)
                    counter = 0

    except KeyboardInterrupt:
        print_statistics(status_code_counts, total_file_size)
        sys.exit(0)

if __name__ == "__main__":
    main()
