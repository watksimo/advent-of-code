def load_input(input_filename):
  f = open(input_filename, "r")
  line = f.readlines()[0]
  line.strip()
  list(line)
  
  return line
  

def solve_part1(input_array):
  score = 0
  
  for idx, char in enumerate(input_array):
    seq = input_array[idx:idx+4]
    # print(seq)
    if len(set(seq)) == 4: return idx+4
  

def solve_part2(input_array):
  score = 0
  
  for idx, char in enumerate(input_array):
    seq = input_array[idx:idx+14]
    # print(seq)
    if len(set(seq)) == 14: return idx+14


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
