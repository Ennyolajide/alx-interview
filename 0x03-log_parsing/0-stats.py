#!/usr/bin/python3
from collections import defaultdict
import signal
import sys

def print_statistics(stats):
    total_size = sum(stats["file_sizes"])
    print(f"Total file size: {total_size}")

    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    for code in status_codes:
        if code in stats["status_codes"]:
            print(f"{code}: {stats['status_codes'][code]}")

def signal_handler(signal, frame):
    print_statistics(stats)
    sys.exit(0)

def parse_line(line):
    try:
        parts = line.strip().split()
        ip_address = parts[0]
        status_code = int(parts[-3])
        file_size = int(parts[-1])
        return status_code, file_size
    except (IndexError, ValueError):
        return None, None

stats = {
    "status_codes": defaultdict(int),
    "file_sizes": []
}

line_count = 0

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        status_code, file_size = parse_line(line)
        if status_code is not None and file_size is not None:
            stats["status_codes"][status_code] += 1
            stats["file_sizes"].append(file_size)
            line_count += 1

        if line_count % 10 == 0:
            print_statistics(stats)

except KeyboardInterrupt:
    pass

print_statistics(stats)
