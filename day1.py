def get_data(INPUT) -> list:
    with open(INPUT) as f:
        fileinput = map(str.rstrip, f.readlines())
    data = []
    for line in fileinput:
        data.append(line)
    return data

##### MAIN PART ######
INPUT = ".\\01.txt"
instructions = get_data(INPUT)

elf_count = 0
max_food_list=[] # sum of calories per elf
for food in instructions:
    if len(food) > 0:
        elf_count += int(food)
    else:
        max_food_list.append(elf_count)
        elf_count = 0

max_food_list.sort()
print(f"Part 1 answer is: {max_food_list[-1]}")
print(f"Part 2 answer is: {sum(max_food_list[-3:])}")