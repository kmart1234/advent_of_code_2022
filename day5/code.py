def main():
	text_file = open("input.txt")
	data = text_file.read()
	text_file.close()

  # Testing stacks:
	#stacks = [
	#	["blah"],		# stupid one so that the indexes start at 1
	#	["Z", "N"],
	#	["M", "C", "D"],
	#	["P"]		
	#]

	# Stacks for part 1:
	stacks = [
		["blah"],		# stupid one so that the indexes start at 1
		["F", "D", "B", "Z", "T", "J", "R", "N"],
		["R", "S", "N", "J", "H"],
		["C", "R", "N", "J", "G", "Z", "F", "Q"],
		["F", "V", "N", "G", "R", "T", "Q"],
		["L", "T", "Q", "F"],
		["Q", "C", "W", "Z", "B", "R", "G", "N"],
		["F", "C", "L", "S", "N", "H", "M"],
		["D", "N", "Q", "M", "T", "J"],
		["P", "G", "S"]
	]

	print("starting arrangement")
	print(f"Stack1: {stacks[1]}")
	print(f"Stack2: {stacks[2]}")
	print(f"Stack3: {stacks[3]}")
	print()

	for line in data.splitlines():
		
		if line.startswith("move"):
			quantity = int(line.split(" ")[1])
			from_stack = int(line.split(" ")[3])
			to_stack = int(line.split(" ")[5])

			print(f"quantity: {quantity}, from: {from_stack}, to: {to_stack}")

			# Part 1 logic, with popping just a single crate
			#i=0
			#while i<quantity:
			#	temp_crate = stacks[from_stack].pop()
			#	print(f"temp crate is: {temp_crate}")
			#	stacks[to_stack].append(temp_crate)
			#	i+=1

			# Part 2 logic, grabbing multiple crates
			grabbed_crates = stacks[from_stack][-quantity:]
			print(f"Grabbed crates: {grabbed_crates}")

			print("Arrangement after grabbing:")
			#del stacks[from_stack][quantity]
			del stacks[from_stack][-quantity:]
			print(f"Stack1: {stacks[1]}")
			print(f"Stack2: {stacks[2]}")
			print(f"Stack3: {stacks[3]}")

			for crate in grabbed_crates:
				stacks[to_stack].append(crate)

			print("Arrangement after moving:")
			print(f"Stack1: {stacks[1]}")
			print(f"Stack2: {stacks[2]}")
			print(f"Stack3: {stacks[3]}")

			print()

	print("Ending stacks:")
	answer = ""
	for stack in stacks:
		#print(stack.pop())
		answer+=stack.pop()

	print(f"Answer: {answer}")


main()