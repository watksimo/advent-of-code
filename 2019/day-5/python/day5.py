from copy import deepcopy

def load_input(input_filename):
  f = open(input_filename, "r")
  return [int(val) for val in f.readline().split(",")]

def solve_part1(input_array, given_input):
  prev_opcode = prev_params = None

  position = 0
  incr_count = 0

  instr_val = str(input_array[position])
  opcode = int(instr_val[-2:])
  params = [int(_) for _ in list(instr_val[:-2])]
  params.reverse()

  input_val = given_input
  prev_output_val = output_val = None

  while opcode != 99: # Halt
    print(opcode, params)
    if opcode == 1:   # Addition
      for i in range(3-len(params)): params.append(0)
      val1 = input_array[input_array[position+1]] if params[0] == 0 else input_array[position+1]
      val2 = input_array[input_array[position+2]] if params[1] == 0 else input_array[position+2]

      input_array[input_array[position+3]] = val1 + val2  # Storing value in immediate mode doesn't make sense, ignored
      incr_count = 4
    elif opcode == 2: # Multiplication
      for i in range(3-len(params)): params.append(0)
      val1 = input_array[input_array[position+1]] if params[0] == 0 else input_array[position+1]
      val2 = input_array[input_array[position+2]] if params[1] == 0 else input_array[position+2]

      input_array[input_array[position+3]] = val1 * val2  # Storing value in immediate mode doesn't make sense, ignored
      incr_count = 4
    elif opcode == 3: # Set to input value
      # print("{}, {}".format(input_array[position], input_array[position+1]))
      input_array[input_array[position+1]] = input_val
      incr_count = 2
    elif opcode == 4: # Set output to given
      for i in range(2-len(params)): params.append(0)
      val1 = input_array[input_array[position+1]] if params[0] == 0 else input_array[position+1]
      output_val = val1
      incr_count = 2
    elif opcode == 5: #jump if true
      for i in range(2-len(params)): params.append(0)
      val1 = input_array[input_array[position+1]] if params[0] == 0 else input_array[position+1]
      val2 = input_array[input_array[position+2]] if params[1] == 0 else input_array[position+2]
      if val1 != 0: position = val2
      else: incr_count = 3
    elif opcode == 6: # jump if false
      for i in range(2-len(params)): params.append(0)
      val1 = input_array[input_array[position+1]] if params[0] == 0 else input_array[position+1]
      val2 = input_array[input_array[position+2]] if params[1] == 0 else input_array[position+2]
      if val1 == 0: position = val2
      else: incr_count = 3
    elif opcode == 7: # less than
      for i in range(4-len(params)): params.append(0)
      val1 = input_array[input_array[position+1]] if params[0] == 0 else input_array[position+1]
      val2 = input_array[input_array[position+2]] if params[1] == 0 else input_array[position+2]
      
      if val1 < val2:
        input_array[input_array[position+3]] = 1
      else:
        input_array[input_array[position+3]] = 0
      incr_count = 4
    elif opcode == 8: # equals
      for i in range(4-len(params)): params.append(0)
      val1 = input_array[input_array[position+1]] if params[0] == 0 else input_array[position+1]
      val2 = input_array[input_array[position+2]] if params[1] == 0 else input_array[position+2]

      if val1 == val2:
        input_array[input_array[position+3]] = 1
      else:
        input_array[input_array[position+3]] = 0
      incr_count = 4
    else:
      print("Unknown opcode: " + str(opcode))
      exit(0)
    
    position = position + incr_count
    incr_count = 0
    if position >= len(input_array):
      print("Input fully consumed with no halt.")
      break
    
    if prev_output_val != output_val:
      print("Output value: " + str(output_val))
      prev_output_val = output_val

    prev_opcode = opcode
    prev_params = params

    instr_val = str(input_array[position])
    opcode = int(instr_val[-2:])
    params = [int(_) for _ in list(instr_val[:-2])]
    params.reverse()

  if opcode == 99:
    print("Halted.")
  return input_array, output_val

if __name__ == '__main__':
  input_array = load_input("../input.txt")
  print("Input length: {}".format(len(input_array)))
  part1_array, part1_out = solve_part1(deepcopy(input_array), 1)
  part2_array, part2_out = solve_part1(deepcopy(input_array), 5)

  # Solutions
  print("Part 1: {}".format(part1_out))
  print("Part 2: {}".format(part2_out))
