# Advent of Code 2022 Day 3
# Prompt: https://adventofcode.com/2022/day/3

priorities_string = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priority_sum = 0

file = open("input.txt", "r")
for line in file:
	compartment_1 = line[slice(0,len(line)//2)]
	compartment_2 = line[slice(len(line)//2, len(line))]
	common = "".join((set(compartment_1).intersection(compartment_2)))
	priority = priorities_string.index(common)
	priority_sum += priority

print(priority_sum)
