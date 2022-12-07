# Advent of Code 2022 Day 4
# Prompt: https://adventofcode.com/2022/day/4

count = 0

file = open("input.txt", "r")
for line in file:
	line = line.strip()
	assignments = line.split(",")
	a1min = int(assignments[0].split("-")[0])
	a1max = int(assignments[0].split("-")[1])
	a2min = int(assignments[1].split("-")[0])
	a2max = int(assignments[1].split("-")[1])

	if (a1min <= a2min and a1max >= a2max) or (a2min <= a1min and a2max >= a1max):
		count += 1

print(count)
