def load_input(input_filename):
  ruck_list = []
  f = open(input_filename, "r")

  for line in f.readlines():
    line = list(line.strip())
    mid = int(len(line)/2)
    print(mid)
    ruck_list.append([line[:mid], line[mid:]])
  return ruck_list
  

def solve_part1(input_array):
  comm_items = []
  score = 0
  
  for ruck in input_array:
    comm = list(set(ruck[0]).intersection(ruck[1]))
    comm_items.append(comm)
    for elem in comm:
      score += to_priority(elem)
  
  return score

def solve_part2(input_array):
  comm_items = []
  score = 0

  last_elf = 3

  while last_elf <= len(input_array):
    group_elves = input_array[last_elf-3:last_elf]
    group_elves = [elem[0] + elem[1] for elem in group_elves]
    # print(group_elves[0])
    comm = list(set(group_elves[0]).intersection(group_elves[1]).intersection(group_elves[2]))
    comm_items.append(comm)
    for elem in comm:
      score += to_priority(elem)
    print(comm)
    last_elf += 3
  
  return score

def to_priority(char):
  if ord(char) > 96: return ord(char) - 96
  if ord(char) < 96: return ord(char) - 38

if __name__ == '__main__':
  # input_array = load_input("../test-input1.txt")
  input_array = load_input("../input.txt")
  print(input_array)
  # exit()
  
  # part 1 solution
  part1_solution = solve_part1(input_array)
  print("Part 1: {}".format(part1_solution))
  # exit()
  

  # part 2 solution
  part2_solution = solve_part2(input_array)
  print("Part 2: {}".format(part2_solution))
