# Solution to problem 2.
# Goal is to find the power of the fewest amount of cubes per color to make each game possible. Then sum the powers.
# Looking at examples is easy to conclude that finding the max amount of cubes per color in each game is the answer.

import os

# Getting document with data.
file_path = os.path.join(os.path.dirname(__file__), r"Inputs\prob2_input.txt")

# Variable to store powers of minimum num of cubes.
powers = []


# Using a nex text decoder function.
def text_decoder(file):
    global powers
    for line in file:
        # vars to store the amount of cubes per draw.
        red_cubes = []
        green_cubes = []
        blue_cubes = []
        game, cubes_num = line.split(":")
        for draw in cubes_num.split(";"):
            for cubes in draw.split(","):
                count, color = cubes.split()
                # Conditions to include the cubes in a set.
                if "red" in color and count.isdigit():
                    red_cubes.append(int(count))
                if "green" in color and count.isdigit():
                    green_cubes.append(int(count))
                if "blue" in color and count.isdigit():
                    blue_cubes.append(int(count))

        # Min number to make game possible for each cube color.
        min_red_cubes = max(red_cubes)
        min_green_cubes = max(green_cubes)
        min_blue_cubes = max(blue_cubes)

        # Calculating the power for each game and appending to list with powers.
        power = min_red_cubes * min_green_cubes * min_blue_cubes
        powers.append(power)

    return powers


# Opening file and applying function.
with open(file_path, mode="r") as file:
    text_decoder(file)
    # Summing the powers of all games.
    print(sum(powers))
