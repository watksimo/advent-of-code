
def load_input(input_filename):
  f = open(input_filename, "r")
  return [line.strip() for line in f.readlines()]

def binary_array_to_number(binary_array):
  return sum([int(digit) * (2**(len(binary_array)-idx-1)) for idx, digit in enumerate(binary_array)])

def get_most_common_bits(input_array):
    counts = [0] * len(input_array[0])
    for line in input_array:
      for idx, digit in enumerate(line):
        counts[idx] += int(digit)
    return [digit/len(input_array) for digit in counts]

def solve_part1(input_array):
  counts = get_most_common_bits(input_array)

  gamma_arr = [0 if digit < 0.5 else 1 for digit in counts]
  epsilon_arr = [1 if digit < 0.5 else 0 for digit in counts]

  gamma = binary_array_to_number(gamma_arr)
  epsilon = binary_array_to_number(epsilon_arr)

  return gamma, epsilon
  
def solve_part2(input_array):
  ox_gen = input_array.copy()
  c02_scrub = input_array.copy()

  for idx in range(len(ox_gen[0])):
    ox_counts = get_most_common_bits(ox_gen)
    co2_counts = get_most_common_bits(c02_scrub)
    
    most_comm = (0 if ox_counts[idx] < 0.5 else 1)
    least_comm = (0 if co2_counts[idx] >= 0.5 else 1)
    
    if len(ox_gen) > 1: ox_gen = [line for line in ox_gen if int(line[idx]) == most_comm]
    if len(c02_scrub) > 1: c02_scrub = [line for line in c02_scrub if int(line[idx]) == least_comm]

  ox_gen_val = binary_array_to_number(list(ox_gen[0]))
  c02_scrub_val = binary_array_to_number(list(c02_scrub[0]))
  return ox_gen_val, c02_scrub_val

if __name__ == '__main__':
  input_array = load_input("../input.txt")
  # input_array = load_input("../test-input1.txt")

  # part 1 solution
  gamma, epsilon = solve_part1(input_array)
  print("Part 1: {}".format(gamma * epsilon))

  # part 2 solution
  depth, horiz = solve_part2(input_array)
  print("Part 2: {}".format(depth * horiz))
