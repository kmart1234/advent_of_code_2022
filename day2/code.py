def points_from_shape(player_shape):
	if player_shape == "X":			# rock
		return(1)
	elif player_shape == "Y":		# paper
		return(2)
	elif player_shape == "Z":		# scissor
		return(3)
	else:									# invalid shape
		return(100000)


def points_from_outcome(player_shape, opponent_shape):
	outcome = determine_outcome(player_shape, opponent_shape)

	if outcome == "win":
		return(6)
	elif outcome == "draw":
		return(3)
	elif outcome == "lose":
		return(0)
	else:
		return(100000)


def determine_outcome(player_shape, opponent_shape):
	if player_shape == "X":							# Rock
		if opponent_shape == "A":						# Rock
			return("draw")
		elif opponent_shape == "B":					# Paper
			return("lose")
		elif opponent_shape == "C":					# Scissor
			return("win")

	elif player_shape == "Y":						# Paper
		if opponent_shape == "A":						# Rock
			return("win")
		elif opponent_shape == "B":					# Paper
			return("draw")
		elif opponent_shape == "C":					# Scissor
			return("lose")

	elif player_shape == "Z":						# Scissor
		if opponent_shape == "A":						# Rock
			return("lose")
		elif opponent_shape == "B":					# Paper
			return("win")
		elif opponent_shape == "C":					# Scissor
			return("draw")


def determine_player_shape(opponent_shape, desired_outcome):
	if desired_outcome == "X":					# Lose
		if opponent_shape == "A":						# Rock
			return("Z")
		elif opponent_shape == "B":					# Paper
			return("X")
		elif opponent_shape == "C":					# Scissor
			return("Y")
	if desired_outcome == "Y":					# Draw
		if opponent_shape == "A":						# Rock
			return("X")
		elif opponent_shape == "B":					# Paper
			return("Y")
		elif opponent_shape == "C":					# Scissor
			return("Z")
	if desired_outcome == "Z":					# Win
		if opponent_shape == "A":						# Rock
			return("Y")
		elif opponent_shape == "B":					# Paper
			return("Z")
		elif opponent_shape == "C":					# Scissor
			return("X")


def main():
	text_file = open("input.txt")
	data = text_file.read()
	text_file.close()
	
	#pt1_score = 0
#
	#for line in data.splitlines():
	#	print(line)
#
	#	player_shape = line.split()[1]
	#	opponent_shape = line.split()[0]
#
	#	pt1_score+=points_from_shape(player_shape)
	#	pt1_score+=points_from_outcome(player_shape, opponent_shape)
#
	# print(f"Final score is: {pt1_score}")

	pt2_score = 0

	for line in data.splitlines():
		print(line)

		opponent_shape = line.split()[0]
		desired_outcome = line.split()[1]

		player_shape = determine_player_shape(opponent_shape, desired_outcome)
		pt2_score+=points_from_shape(player_shape)
		pt2_score+=points_from_outcome(player_shape, opponent_shape)

	print(f"Final score is: {pt2_score}")

main()