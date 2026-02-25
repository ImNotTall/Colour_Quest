import csv
import random

def round_ans(val):

    var_rounded = (val * 2 + 1) // 2
    raw_rounded = "{:.0f}".format(var_rounded)
    return int(raw_rounded)

file = open("00_colour_list_hex_v3.csv", "r")
all_colours = list(csv.reader(file, delimiter=","))
file.close()

all_colours.pop(0)

round_colours = []
colour_scores = []

while len(round_colours) < 4:
    potential_colour = random.choice(all_colours)

    if potential_colour[1] not in colour_scores:
        round_colours.append(potential_colour)
        colour_scores.append(potential_colour[1])

print(round_colours)
print(colour_scores)

int_scores = [int(x) for x in colour_scores]
int_scores.sort()

median = (int_scores[1] + int_scores[2]) / 2
median = round_ans(median)
print("Median", median)