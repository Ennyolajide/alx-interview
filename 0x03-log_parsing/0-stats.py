#!/usr/bin/python3
import sys

def parse_line(line):
    # Sample input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
    parts = line.split()
    if len(parts) != 10 or not parts[8].isdigit():
        return None
    status_code = int(parts[8])
    file_size = int(parts[9])
    return status_code, file_size

def print_statistics(total_size, status_code_counts):
    print("Total file size:", total_size)
    for status_code in sorted(status_code_counts.keys()):
        print(f"{status_code}: {status_code_counts[status_code]}")

def main():
    total_size = 0
    status_code_counts = {}

    try:
        line_count = 0
        for line in sys.stdin:
            line_count += 1
            parsed_line = parse_line(line)
            if parsed_line is None:
                continue

            status_code, file_size = parsed_line
            total_size += file_size

            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            else:
                status_code_counts[status_code] = 1

            if line_count % 10 == 0:
                print_statistics(total_size, status_code_counts)

    except KeyboardInterrupt:
        print_statistics(total_size, status_code_counts)
        sys.exit(0)

if __name__ == "__main__":
    main()

