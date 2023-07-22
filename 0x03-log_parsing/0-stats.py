#!/usr/bin/python3

import sys


def print_statistics(status_code_counts, total_file_size):
    """Prints the statistics"""
    print("File size:", total_file_size)
    for status_code, count in sorted(status_code_counts.items()):
        if count != 0:
            print(f"{status_code}: {count}")


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
total_file_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1

        if line_count % 10 == 0:
            print_statistics(status_code_counts, total_file_size)

        parsed_line = line.strip().split()

        if len(parsed_line) == 7:
            try:
                status_code = int(parsed_line[-2])
                file_size = int(parsed_line[-1])
                total_file_size += file_size

                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1
            except ValueError:
                pass

except KeyboardInterrupt:
    print_statistics(status_code_counts, total_file_size)
    sys.exit(0)

print_statistics(status_code_counts, total_file_size)
