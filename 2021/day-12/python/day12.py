def load_input(input_filename):
  f = open(input_filename, "r")
  return [[int(ch1) for ch1 in list(line.strip())] for line in f.readlines()]

def solve_part1(input_array):
  return None

def solve_part2(input_array):
  return None

if __name__ == '__main__':
  # input_array = load_input("../input.txt")
  input_array = load_input("../test-input1.txt")

  # part 1 solution
  part1_solution = solve_part1(input_array)
  print("Part 2: {}".format(part1_solution))

  # part 2 solution
  part2_solution = solve_part2(input_array)
  print("Part 2: {}".format(part2_solution))
