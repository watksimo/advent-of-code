def load_input(input_filename):
  pair_list = []
  f = open(input_filename, "r")

  for line in f.readlines():
    line = line.strip()
    pairs = line.split(",")
    pairs = [elf.split('-') for elf in pairs]
    pairs = [list(range(int(elf[0]), int(elf[1])+1)) for elf in pairs]
    pair_list.append(pairs)
  
  return pair_list
  

def solve_part1(input_array):
  score = 0
  
  for pair in input_array:
    max_elf = max(len(pair[0]), len(pair[1]))
    if len(set(pair[0]).union(set(pair[1]))) == max_elf:
      # print(pair)
      score+=1
  
  return score

def solve_part2(input_array):
  score = 0

  for pair in input_array:
    if len(set(pair[0]).intersection(set(pair[1]))) > 0:
      print(pair)
      score+=1
  
  return score


if __name__ == '__main__':
  input_array = load_input("../test-input1.txt")
  # input_array = load_input("../input.txt")
  # print(input_array)
  # exit()
  
  # part 1 solution
  part1_solution = solve_part1(input_array)
  print("Part 1: {}".format(part1_solution))
  # exit()
  

  # part 2 solution
  part2_solution = solve_part2(input_array)
  print("Part 2: {}".format(part2_solution))
