def get_priority(item):
	item_priorities = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	return(item_priorities.rfind(item))


def find_common_items(group_rucksacks):
	# Seems dumb but should work if there's always 3 in a group

	items_in_one_and_two = []
	for item in group_rucksacks[0]:
		if item in group_rucksacks[1]:
			items_in_one_and_two+=item
	#print(f"Items in one and two: {items_in_one_and_two}")

	item_in_all_three = set()
	for item in group_rucksacks[2]:
		if item in items_in_one_and_two:
			item_in_all_three.add(item)

	print(f"Common items are: {item_in_all_three}")
	return(item_in_all_three)


def main():
	text_file = open("input.txt")
	data = text_file.read()
	text_file.close()
	
	sum_of_priorities = 0

	# Part 1
	for rucksack in data.splitlines():
	#	print(rucksack)

		first_compartment = rucksack[0:len(rucksack)//2]
		second_compartment = rucksack[len(rucksack)//2:]		
		common_items = set()

		for item in first_compartment:
			if item in second_compartment:
				common_items.add(item)

		for item in common_items:
			sum_of_priorities+=get_priority(item)

	#print(f"The sum of priorities is: {sum_of_priorities}")

	# Part 2
	curr_group_size = 0
	group_rucksacks = []
	group_priorities = 0

	for rucksack in data.splitlines():
		
		# Split all elves into groups of 3
		if curr_group_size < 3:
			group_rucksacks.append(rucksack)
			curr_group_size+=1
		else:
			# Do the stuff
			print(group_rucksacks)
			common_item = find_common_items(group_rucksacks)
			group_priorities+=get_priority(list(common_item)[0])

			# Start the next group
			curr_group_size = 1
			group_rucksacks = []
			group_rucksacks.append(rucksack)
		
		#print(group_rucksacks)
		#print()
	print(f"After checking all groups, the total priority is: {group_priorities}")


main()