import os

# Getting document with data.
file_path = os.path.join(os.path.dirname(__file__), r"Inputs\prob1_input.txt")


# Problem 1 solution:
# Defining function to find calibration values and summing them up.
def calib_values(file):
    char1 = ""
    char2 = ""
    calib_values_list = list()
    total = 0
    for line in file:
        for char in list(line)[:]:
            if char.isdigit():
                char1 = str(char)
                break
        for char in list(line)[::-1]:
            if char.isdigit():
                char2 = str(char)
                break
        calib_values_list.append(char1 + char2)

    for value in calib_values_list:
        total += int(value)

    return total


# Opening file with data and applying function to find total of calibration numbers.
with open(file_path, mode="r") as file:
    print(calib_values(file))
