# Advent of Code 2022 Day 1
# Prompt: https://adventofcode.com/2022/day/1

this_elfs_calories = 0
elves = []

file = open("input.txt", "r")
for line in file:
	line = line.strip()
	if line == "":	# Current elf is done. Add them to the array.
		elves.append(this_elfs_calories)
		this_elfs_calories = 0
	else:
		this_elfs_calories += int(line)

elves.sort(reverse=True)
print(str(elves[0] + elves[1] + elves[2]))