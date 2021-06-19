from copy import deepcopy

def load_input(input_filename):
  f = open(input_filename, "r")
  return [int(val) for val in f.readline().split(",")]

def solve_part1(input_array, val1, val2):
  input_array[1] = val1
  input_array[2] = val2

  position = 0
  opcode = input_array[position]
  while opcode != 99:
    if opcode == 1:
      input_array[input_array[position+3]] = input_array[input_array[position+1]] + input_array[input_array[position+2]]
    elif opcode == 2:
      input_array[input_array[position+3]] = input_array[input_array[position+1]] * input_array[input_array[position+2]]
    
    position = position + 4
    if position >= len(input_array):
      break
    opcode = input_array[position]

  return input_array

def solve_part2(input_array):
  for noun in range(100):
    for verb in range(100):
      test_array = solve_part1(deepcopy(input_array), noun, verb)
      if test_array[0] == 19690720:
        return noun, verb

if __name__ == '__main__':
  input_array = load_input("../input.txt")
  part1_array = solve_part1(deepcopy(input_array), 12, 2)

  # part 1 solution
  print("Part 1: {}".format(part1_array[0]))

  noun, verb = solve_part2(input_array)
  answer = 100 * noun + verb
  print("Part 2: noun = {}, verb = {}. Answer = {}".format(noun, verb, answer))

