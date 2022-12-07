# Advent of Code 2022 Day 2
# Prompt: https://adventofcode.com/2022/day/2

# Rock		= A, 1
# Paper		= B, 2
# Scissors  = C, 3
# Win		= Z, +6
# Lose		= X, +0
# Draw		= Y, +3

score = 0

file = open("input.txt", "r")
for line in file:
	game = line.split()
	if game[1] == "X":
		#lose 
		if game[0] == "A":
			score += 3
		elif game[0] == "B":
			score += 1
		elif game[0] == "C":
			score += 2
	elif game[1] == "Y":
		#draw
		score += 3
		if game[0] == "A":
			score += 1
		elif game[0] == "B":
			score += 2
		elif game[0] == "C":
			score += 3
	elif game[1] == "Z":
		#win
		score += 6
		if game[0] == "A":
			score += 2
		elif game[0] == "B":
			score += 3
		elif game[0] == "C":
			score += 1
	
print(str(score))