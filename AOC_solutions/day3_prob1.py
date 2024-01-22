# Problem 3 solution.
# Goal is to extract from input any number that is adjacent to a symbol in any direction (top, down, left, right and diagonal).

import os
import re

# Getting document with data.
file_path = os.path.join(os.path.dirname(__file__), r"Inputs\prob3_input.txt")

# Defining function to find out which numbers are adjacent to a symbol.


def find_valid_nums(file):
    valid_nums = []
    chars_index = []
    lines = []
    position_tracker = 0
    pattern_toright = re.compile(r"[0-9]+[\-$*|(),{}@=+/&%#\\]")
    pattern_toleft = re.compile(r"[\-$*|(),{}@=+/&%#\\]+[0-9]+")
    find_spec_char = re.compile(r"[\-$*|(),{}@=+/&%#\\]")

    # Checking right.
    right_matches = pattern_toright.findall(file.read())

    # Checking left.
    file.seek(0)  # Pointer to the first line.
    left_matches = pattern_toleft.findall(file.read())

    # Checking top.
    file.seek(0)
    for line in file.readlines():
        # For position of  special char store that position in a list.
        for pos, char in enumerate(line):
            if find_spec_char.findall(char):
                chars_index.append(pos)

        # I need to check line by line the position of the digits, and then based on the position, see if the special characters have a position in a previous
        # line in the same position. Vice versa is with down characters.

    # Checking down.

    # Checking left diagonal.

    # Checking right diagonal.
    print(chars_index)
    return right_matches + left_matches


# Summing valid numbers.

# Opening input file.
with open(file_path, mode="r") as file:
    print(find_valid_nums(file))
