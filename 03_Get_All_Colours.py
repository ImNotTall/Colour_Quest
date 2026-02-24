import csv
import random

file = open("00_colour_list_hex_v3.csv", "r")
all_colours = list(csv.reader(file, delimiter=","))
file.close()

all_colours.pop(0)
print(all_colours)