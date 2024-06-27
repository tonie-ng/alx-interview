#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Method that determines if a given data set
    represents a valid UTF-8 encoding.

    Parameters:
    data (list of int): A list of integers where
    each integer represents 1 byte of data.

    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.
    """
    remaining_bytes = 0

    byte_mask_1 = 1 << 7  # 10000000 in binary
    byte_mask_2 = 1 << 6  # 01000000 in binary

    for byte in data:
        leading_one_mask = 1 << 7  # 10000000 in binary

        if remaining_bytes == 0:
            while leading_one_mask & byte:
                remaining_bytes += 1
                leading_one_mask >>= 1

            if remaining_bytes == 0:
                continue

            if remaining_bytes == 1 or remaining_bytes > 4:
                return False

        else:
            if not (byte & byte_mask_1 and not (byte & byte_mask_2)):
                return False

        remaining_bytes -= 1

    return remaining_bytes == 0
