from copy import deepcopy

def load_input(input_filename):
  f = open(input_filename, "r")
  return [int(val) for val in f.readline().split(",")]

def solve_part1(input_array):
  position = 0
  incr_count = 0

  instr_val = str(input_array[position])
  opcode = int(instr_val[-2:])
  params = [int(_) for _ in list(instr_val[:-2])]
  params.reverse()

  input_val = 1
  prev_output_val = output_val = None

  while opcode != 99: # Halt
    # print(opcode, params)
    if opcode == 1:   # Addition
      for i in range(3-len(params)): params.append(0)
      # print("{}, {}, {}, {}".format(input_array[position], input_array[position+1], input_array[position+2], input_array[position+3]))
      val1 = input_array[input_array[position+1]] if params[0] == 0 else input_array[position+1]
      val2 = input_array[input_array[position+2]] if params[1] == 0 else input_array[position+2]

      input_array[input_array[position+3]] = val1 + val2  # Storing value in immediate mode doesn't make sense, ignored
      incr_count = 4
      # print("{} + {} = {} stored in {}".format(val1, val2, val1+val2, input_array[position+3]))
    elif opcode == 2: # Multiplication
      # print("{}, {}, {}, {}".format(input_array[position], input_array[position+1], input_array[position+2], input_array[position+3]))
      for i in range(3-len(params)): params.append(0)
      val1 = input_array[input_array[position+1]] if params[0] == 0 else input_array[position+1]
      val2 = input_array[input_array[position+2]] if params[1] == 0 else input_array[position+2]

      input_array[input_array[position+3]] = val1 * val2  # Storing value in immediate mode doesn't make sense, ignored
      incr_count = 4
    elif opcode == 3:
      # print("{}, {}".format(input_array[position], input_array[position+1]))
      input_array[input_array[position+1]] = input_val
      incr_count = 2
    elif opcode == 4:
      for i in range(1-len(params)): params.append(0)
      # print("{}, {}".format(input_array[position], input_array[position+1]))
      val1 = input_array[input_array[position+1]] if params[0] == 0 else input_array[position+1]
      output_val = val1
      incr_count = 2
    else:
      print("Unknown opcode: " + str(opcode))
      exit(0)
    
    position = position + incr_count
    if position >= len(input_array):
      print("Input fully consumed with no halt.")
      break
    
    if prev_output_val != output_val:
      print("Output value: " + str(output_val))
      prev_output_val = output_val

    instr_val = str(input_array[position])
    opcode = int(instr_val[-2:])
    params = [int(_) for _ in list(instr_val[:-2])]
    params.reverse()

  if opcode == 99:
    print("Halted.")
  return input_array, output_val

if __name__ == '__main__':
  input_array = load_input("../input.txt")
  # input_array = [1002,4,3,4,33,99]
  # input_array = [1101,100,-1,4,0]
  print("Input length: {}".format(len(input_array)))
  part1_array, part1_out = solve_part1(deepcopy(input_array))

  # part 1 solution
  print("Part 1: {}".format(part1_out))
