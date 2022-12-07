# Advent of Code 2022 Day 3
# Prompt: https://adventofcode.com/2022/day/3

priorities_string = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priority_sum = 0



i = 1
rucksacks = []
file = open("input.txt", "r")
for line in file:
	rucksacks.append(line)
	if i%3==0:	# We got three
		common_1 = "".join((set(rucksacks[0]).intersection(rucksacks[1])))		# Figure out the unique item
		common = "".join((set(common_1).intersection(rucksacks[2]))).strip()
		priority = priorities_string.index(common)
		priority_sum += priority
		rucksacks.clear()
	i+=1

print(priority_sum)
