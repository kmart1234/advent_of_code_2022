def main():
	text_file = open("input.txt")
	data = text_file.read()
	text_file.close()

	completely_overlapping_pairs = 0
	any_overlapping_pairs = 0

	for elf_pair in data.splitlines():
		print(elf_pair)

		elf1 = elf_pair.split(',')[0]
		elf1_min = int(elf1.split('-')[0])
		elf1_max = int(elf1.split('-')[1])
		elf1_range = range(elf1_min, elf1_max+1)

		elf2 = elf_pair.split(',')[1]
		elf2_min = int(elf2.split('-')[0])
		elf2_max = int(elf2.split('-')[1])
		elf2_range = range(elf2_min, elf2_max+1)

		#print(f"elf1: {elf1}")
		#print(f"elf1 min: {elf1_min}")
		#print(f"elf1 max: {elf1_max}")
		#print(f"elf1 range: {elf1_range}")
		#print(f"elf2: {elf2}")
		#print(f"elf2 min: {elf2_min}")
		#print(f"elf2 max: {elf2_max}")
		#print(f"elf2 range: {elf2_range})")

		# Part 1
		if elf1_min >= elf2_min and elf1_max <= elf2_max:
			print("total overlap")
			completely_overlapping_pairs+=1
		elif elf1_min <= elf2_min and elf1_max >= elf2_max:
			print("total overlap")
			completely_overlapping_pairs+=1
		else:
			print("Not completely overlapping")

		# Part 2
		for room in elf1_range:
			if room in elf2_range:
				any_overlapping_pairs+=1
				print("Partial or total overlap")
				break

		print()

	print(f"Number of overlapping pairs is: {completely_overlapping_pairs}")
	print(f"Number of any overlapping pairs is: {any_overlapping_pairs}")

main()