
def load_input(input_filename):
  f = open(input_filename, "r")
  return [line.strip() for line in f.readlines()]

def solve_part1(input_array):
  counts = [0] * len(input_array[0])
  for line in input_array:
    for idx, digit in enumerate(line):
      counts[idx] += int(digit)

  counts = [digit/len(input_array) for digit in counts]
  gamma_arr = [0 if digit < 0.5 else 1 for digit in counts]
  epsilon_arr = [1 if digit < 0.5 else 0 for digit in counts]

  gamma = [digit * (2**(len(gamma_arr)-idx-1)) for idx, digit in enumerate(gamma_arr)]
  epsilon = [digit * (2**(len(epsilon_arr)-idx-1)) for idx, digit in enumerate(epsilon_arr)]
  # print(gamma, epsilon)
  return sum(gamma), sum(epsilon)
  

# def solve_part2(input_array):



if __name__ == '__main__':
  input_array = load_input("../input.txt")
  # input_array = load_input("../test-input1.txt")

  # part 1 solution
  gamma, epsilon = solve_part1(input_array)

  print("Part 1: {}".format(gamma * epsilon))

  # part 2 solution
  # depth, horiz = solve_part2(input_array)
  # print("Part 2: {}".format(depth * horiz))
