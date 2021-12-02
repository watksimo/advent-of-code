
def load_input(input_filename):
  f = open(input_filename, "r")
  commands = [line.strip().split(" ") for line in f.readlines()]
  commands = [[line[0], int(line[1])] for line in commands]
  return commands

def solve_part1(input_array):
  depth = horiz = 0
  for dir, mag in input_array:
    if dir == "up":
      depth -= mag
    elif dir == "down":
      depth += mag
    elif dir == "forward":
      horiz += mag

  return depth, horiz
  

def solve_part2(input_array):
  depth = horiz = aim = 0
  for dir, mag in input_array:
    if dir == "up":
      aim -= mag
    elif dir == "down":
      aim += mag
    elif dir == "forward":
      horiz += mag
      depth += (aim * mag)

  return depth, horiz


if __name__ == '__main__':
  input_array = load_input("../input.txt")
  # input_array = load_input("../test-input1.txt")

  # part 1 solution
  depth, horiz = solve_part1(input_array)

  print("Part 1: {}".format(depth * horiz))

  # part 2 solution
  depth, horiz = solve_part2(input_array)
  print("Part 2: {}".format(depth * horiz))
