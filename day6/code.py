def main():
	text_file = open("input.txt")
	data = text_file.read()
	text_file.close()

	answers = []

	# Part 1
	#N = 4
	# Part 2
	N = 14

	for line in data.splitlines():
		print(line)
		
		# Make all the substrings of N characters starting at beginning of line
		character_pointer = 0
		while character_pointer < len(line)-N:
			
			substring = line[character_pointer:character_pointer+N]
			print(substring)
			
			# Check substring to see if all characters are unique
			if check_unique(substring) == True:
				print("All characters in this substring are unique")
				answers.append(character_pointer+N)
				break
			else:
				print("Not all characters are unique, making another substring")
			
			character_pointer+=1

		print()
	print(f"Answers: {answers}")


def check_unique(characters):

	char_ptr = 0

	while char_ptr < len(characters):
		
		character = characters[char_ptr:char_ptr+1]
		rest_of_substring = characters[char_ptr+1:len(characters)]

		print(f"Checking if {character} is in {rest_of_substring}")

		if character in rest_of_substring:
			return(False)
		else:
			char_ptr+=1

	return(True)

main()