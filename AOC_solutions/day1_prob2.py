import os

# Getting document with data.
file_path = os.path.join(os.path.dirname(__file__), r"Inputs\prob1_input.txt")


# Problem 2 solution:
# Creating dict with number names as keys and digits as values.

number_names = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


# Creating improved function to find calibration values and summing them up.
def calib_values2(file):
    calib_values_list = list()
    total = 0
    for line in file:
        order = list()
        order2 = list()
        num_values = list()
        num_values2 = list()
        position_tracker = 0
        calibration_digit1 = ""
        calibration_digit2 = ""

        # finding the index position of numbers in str format.
        for number in number_names:
            if line.count(number) == 1:
                order.append(line.index(number))
                num_values.append(number_names[number])
            elif line.count(number) > 1:
                for _ in range(line.count(number)):
                    if number in line and line.index(number) not in order:
                        order.append(line.index(number))
                        num_values.append(number_names[number])
                        position_tracker_s = order[-1] + 1
                    elif number in line and line.index(number) in order:
                        order.append(line.index(number, position_tracker_s))
                        num_values.append(number_names[number])
                        position_tracker_s = order[-1] + 1

        # finding index position of numbers in int.
        for char in line[:]:
            if char.isdigit() and line.count(char) == 1:
                order2.append(line.index(char))
                num_values2.append(char)
            elif char.isdigit() and line.count(char) > 1:
                order2.append(line.index(char, position_tracker))
                num_values2.append(char)
                position_tracker = order2[-1] + 1

        # comparing index positions of nums in strings or nums in int.
        final_order = order + order2
        final_num_values = num_values + num_values2

        for p, v in zip(final_order, final_num_values):
            if p == min(final_order):
                calibration_digit1 = v
            elif p == max(final_order):
                calibration_digit2 = v

        if calibration_digit1 and calibration_digit2:
            calib_values_list.append(calibration_digit1 + calibration_digit2)
        elif calibration_digit1 and not calibration_digit2:
            calib_values_list.append(calibration_digit1 + calibration_digit1)
        elif not calibration_digit1 and calibration_digit2:
            calib_values_list.append(calibration_digit2 + calibration_digit2)

    print(calib_values_list, len(calib_values_list))

    for value in calib_values_list:
        total += int(value)

    return total


# Opening file with data and applying function to find total of calibration numbers.
with open(file_path, mode="r") as file:
    print(calib_values2(file))
