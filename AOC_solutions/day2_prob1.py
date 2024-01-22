# Solution to problem 1.
# Goal is to find out how many games are possible with three sets of cubes.
# We have 12 red cubes, 13 green cubes and 14 blue cubes.
# Conditions are record each game ID.
# Three rounds per game.
# No game can be equal if we are to find how many games are possible.
# We only need to know from the inputs if the following conditions are met.
# less or equal than 12 red, 13 green and 14 blue. Total sum of cubes per set can't be more than 39.

import os

# Getting document with data.
file_path = os.path.join(os.path.dirname(__file__), r"Inputs\prob2_input.txt")

# List to store IDs of possible games.
possible_games_IDs = []


# Creating function to extract amount of cubes per set in each game.
def text_decoder(file):
    global possible_games_IDs
    valid_game = True  # Default condition until otherwise.
    # Iterating through each line.
    for line in file:
        valid_game = True
        game, cubes_num = line.split(":")
        for draw in cubes_num.split(";"):
            for cubes in draw.split(","):
                count, color = cubes.split()
                if "red" in color and int(count) > 12:
                    valid_game = False
                if "green" in color and int(count) > 13:
                    valid_game = False
                if "blue" in color and int(count) > 14:
                    valid_game = False

        if valid_game == True:
            _, ID = game.split()
            possible_games_IDs.append(int(ID))

    return possible_games_IDs


# Opening input file and applying function.
with open(file_path, mode="r") as file:
    print(text_decoder(file))
    # Summing the IDs of possible games.
    print(sum(possible_games_IDs))
