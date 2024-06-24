#!/usr/bin/python3
"""reads stdin line by line and computes metrics:"""
import sys


def print_msg(dict_sc, total_file_size):
    """
    prints file size and status codes with non-zero counts.
    """
    print(f"File size: {total_file_size}")
    for key, val in sorted(dict_sc.items()):
        if val != 0:
            print(f"{key}: {val}")


def main():
    "main function"
    total_file_size = 0
    counter = 0
    dict_sc = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }

    try:
        for line in sys.stdin:
            parsed_line = line.split()
            parsed_line = parsed_line[::-1]

            if len(parsed_line) > 2:
                counter += 1

                if counter <= 10:
                    total_file_size += int(parsed_line[0])
                    code = parsed_line[1]

                    if code in dict_sc:
                        dict_sc[code] += 1

                if counter == 10:
                    print_msg(dict_sc, total_file_size)
                    counter = 0

    finally:
        print_msg(dict_sc, total_file_size)


if __name__ == "__main__":
    main()
