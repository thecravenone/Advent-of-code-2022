# Advent of Code 2022 Day 2 Part 1
# Prompt: https://adventofcode.com/2022/day/2

# Rock		= A, X, 1
# Paper		= B, Y, 2
# Scissors  = C, Z, 3
# Win		= +6
# Lose		= +0
# Draw		= +3

score = 0

file = open("input.txt", "r")
for line in file:
	game = line.split()
	if game[1] == "X":
		score += 1
		if game[0] == "C":
			score += 6
		elif game[0] == "A":
			score += 3
	elif game[1] == "Y":
		score += 2
		if game[0] == "A":
			score += 6
		elif game[0] == "B":
			score += 3
	elif game[1] == "Z":
		score +=3
		if game[0] == "B":
			score += 6
		elif game[0] == "C":
			score +=3

print(str(score))