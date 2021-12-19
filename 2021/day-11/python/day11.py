def load_input(input_filename):
  f = open(input_filename, "r")
  return [[int(ch1) for ch1 in list(line.strip())] for line in f.readlines()]

def solve_part1(input_array):
  return None

def solve_part2(input_array):
  return None

if __name__ == '__main__':
  input_array = load_input("../input.txt")
  # input_array = load_input("../test-input1.txt")

  # part 1 solution
  pt1_result = solve_part1(input_array)
  print("Part 1: {}".format(pt1_result))

  # part 2 solution
  pt2_result = solve_part2(input_array)
  print("Part 2: {}".format(pt2_result))
