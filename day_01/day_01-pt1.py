# Advent of Code 2022 Day 1
# Prompt: https://adventofcode.com/2022/day/1

highest_calorie_count = 0
current_calorie_count = 0

file = open("input.txt", "r")
for line in file:
	line = line.strip()
	if line == "":	# end the current elf's count
		if current_calorie_count > highest_calorie_count:
			highest_calorie_count = current_calorie_count
			current_calorie_count = 0
		else:
			current_calorie_count = 0
	else:
		current_calorie_count += int(line)

print(str(highest_calorie_count))