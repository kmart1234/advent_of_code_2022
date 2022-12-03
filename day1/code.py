text_file = open("input.txt")
data = text_file.read()
text_file.close()

elves = []
calories = 0

for line in data.splitlines():
	#print(line)
	if line == "":
		elves.append(calories)
		calories = 0
	else:
		calories+=int(line)

print(elves)
max_elf = max(elves)
print(max_elf)
print(elves.index(max_elf))

### Added for part two
first_most = max_elf
elves.remove(max_elf)
second_most = max(elves)
elves.remove(second_most)
third_most = max(elves)
top_three = first_most+second_most+third_most
print(top_three)
