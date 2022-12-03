
conv = {
  'A': 'rock',
  'B': 'paper',
  'C': 'scissors',
  'X': 'rock',
  'Y': 'paper',
  'Z': 'scissors'
}

conv2 = {
  'rock': 'X',
  'paper': 'Y',
  'scissors': 'Z'
}

beaten_by = {
  'rock': ['paper'],
  'paper': ['scissors'],
  'scissors': ['rock']
}
beats = {
  'rock': ['scissors'],
  'paper': ['rock'],
  'scissors': ['paper']
}

scores = {
  'rock': 1,
  'paper': 2,
  'scissors': 3
}

result = {
  'X': 'lose',
  'Y': 'draw',
  'Z': 'win'
}

def load_input(input_filename):
  global conv
  f = open(input_filename, "r")
  games = []

  for line in f.readlines():
    line = line.strip()
    games.append([conv[a] for a in line.split(" ")])
  return games
  

def solve_part1(input_array):
  score = 0
  
  for game in input_array:
    mine = game[1]
    theirs = game[0]
    print(mine, theirs)

    score += scores[mine]

    if mine in beaten_by[theirs]:
      score += 6
    elif mine == theirs:
      score += 3
    print(score)

  return score

def solve_part2(input_array):
  score = 0
  
  for game in input_array:
    result = conv2[game[1]]
    theirs = game[0]
    mine = 'l'
    print(theirs, result)

    if result == 'X':
      # lose
      mine = beats[theirs][0]
    elif result == 'Y':
      # draw
      mine = theirs
      score += 3
    else:
      # win
      mine = beaten_by[theirs][0]
      score += 6

    score += scores[mine]
    print(score, mine)

  return score


if __name__ == '__main__':
  # input_array = load_input("../test-input1.txt")
  input_array = load_input("../input.txt")
  print(input_array)
  # exit()
  
  # part 1 solution
  part1_solution = solve_part1(input_array)
  print("Part 1: {}".format(part1_solution))
  # 12387
  # exit()
  

  # part 2 solution
  part2_solution = solve_part2(input_array)
  print("Part 2: {}".format(part2_solution))
