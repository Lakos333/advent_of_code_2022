def get_data(INPUT) -> list:
    with open(INPUT) as f:
        fileinput = map(str.rstrip, f.readlines())
    data = []
    data2 = []

    translation = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors',
               'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors',}
    for line in fileinput:
        left, right = line.split()
        data.append((translation.get(left), (translation.get(right))))
        data2.append((left, right))
    return data,data2

def play_turn(round):
    score = 0
    opponent,me = round
    
    # ties
    if opponent == me:
        score += 3
    # winning
    elif (opponent == "Rock" and me =="Paper") or (opponent == "Paper" and me =="Scissors") or (opponent == "Scissors" and me =="Rock"):
        score += 6    
    # loosing no score added no condition for that

    # adding score for shape
    if me == "Rock":
        score += 1
    elif me == "Paper":
        score += 2
    else:
        score += 3
    return score

def part2_turn(round,part2):
    score = 0
    opponent,me = round
    _,instruction = part2

    if instruction == "X":
        # need to loose
        if opponent == "Rock":
            score += 3
        elif opponent == "Paper":
            score += 1
        else:
            score += 2

    elif instruction == "Y":
        # need to draw
        if opponent == "Rock":
            score += 1
        elif opponent == "Paper":
            score += 2
        else:
            score += 3
        # + for draw
        score += 3

    elif instruction == "Z":
        # need to win
        if opponent == "Rock":
            score += 2
        elif opponent == "Paper":
            score += 3
        else:
            score += 1
        # + for win
        score += 6     

    return score
##### MAIN PART ######
INPUT = ".\\02.txt"
instructions,part2 = get_data(INPUT)

total_score = 0
total_score2 = 0

for round in instructions:
    total_score += play_turn(round)

for i, round in enumerate(instructions):
    total_score2 += part2_turn(round,part2[i])

print(f"Part 1 answer is: {total_score}")
print(f"Part 2 answer is: {total_score2}")








