from copy import deepcopy
from itertools import permutations

class IntcodeComputer:
  def __init__(self, intcode_array, input_queue):
    self.completed = False
    self.prev_opcode = self.prev_params = None
    self.position = 0
    self.intcode_array = intcode_array
    self.input_queue = input_queue

  def run_computer(self):
    opcode = 0
    prev_output_val = output_val = None
    while opcode != 99: # Halt
      incr_count = 0
      instr_val = str(self.intcode_array[self.position])
      opcode = int(instr_val[-2:])
      params = [int(_) for _ in list(instr_val[:-2])]
      params.reverse()
      # print(opcode, params)
      if opcode == 1:   # Addition
        for i in range(3-len(params)): params.append(0)
        val1 = self.intcode_array[self.intcode_array[self.position+1]] if params[0] == 0 else self.intcode_array[self.position+1]
        val2 = self.intcode_array[self.intcode_array[self.position+2]] if params[1] == 0 else self.intcode_array[self.position+2]

        self.intcode_array[self.intcode_array[self.position+3]] = val1 + val2  # Storing value in immediate mode doesn't make sense, ignored
        incr_count = 4
      elif opcode == 2: # Multiplication
        for i in range(3-len(params)): params.append(0)
        val1 = self.intcode_array[self.intcode_array[self.position+1]] if params[0] == 0 else self.intcode_array[self.position+1]
        val2 = self.intcode_array[self.intcode_array[self.position+2]] if params[1] == 0 else self.intcode_array[self.position+2]

        self.intcode_array[self.intcode_array[self.position+3]] = val1 * val2  # Storing value in immediate mode doesn't make sense, ignored
        incr_count = 4
      elif opcode == 3: # Set to input value
        # print("{}, {}".format(input_array[position], input_array[position+1]))
        self.intcode_array[self.intcode_array[self.position+1]] = self.input_queue.pop(0)
        incr_count = 2
      elif opcode == 4: # Set output to given
        for i in range(2-len(params)): params.append(0)
        val1 = self.intcode_array[self.intcode_array[self.position+1]] if params[0] == 0 else self.intcode_array[self.position+1]
        output_val = val1
        incr_count = 2
      elif opcode == 5: #jump if true
        for i in range(2-len(params)): params.append(0)
        val1 = self.intcode_array[self.intcode_array[self.position+1]] if params[0] == 0 else self.intcode_array[self.position+1]
        val2 = self.intcode_array[self.intcode_array[self.position+2]] if params[1] == 0 else self.intcode_array[self.position+2]
        if val1 != 0: self.position = val2
        else: incr_count = 3
      elif opcode == 6: # jump if false
        for i in range(2-len(params)): params.append(0)
        val1 = self.intcode_array[self.intcode_array[self.position+1]] if params[0] == 0 else self.intcode_array[self.position+1]
        val2 = self.intcode_array[self.intcode_array[self.position+2]] if params[1] == 0 else self.intcode_array[self.position+2]
        if val1 == 0: self.position = val2
        else: incr_count = 3
      elif opcode == 7: # less than
        for i in range(4-len(params)): params.append(0)
        val1 = self.intcode_array[self.intcode_array[self.position+1]] if params[0] == 0 else self.intcode_array[self.position+1]
        val2 = self.intcode_array[self.intcode_array[self.position+2]] if params[1] == 0 else self.intcode_array[self.position+2]
        
        if val1 < val2:
          self.intcode_array[self.intcode_array[self.position+3]] = 1
        else:
          self.intcode_array[self.intcode_array[self.position+3]] = 0
        incr_count = 4
      elif opcode == 8: # equals
        for i in range(4-len(params)): params.append(0)
        val1 = self.intcode_array[self.intcode_array[self.position+1]] if params[0] == 0 else self.intcode_array[self.position+1]
        val2 = self.intcode_array[self.intcode_array[self.position+2]] if params[1] == 0 else self.intcode_array[self.position+2]

        if val1 == val2:
          self.intcode_array[self.intcode_array[self.position+3]] = 1
        else:
          self.intcode_array[self.intcode_array[self.position+3]] = 0
        incr_count = 4
      elif opcode == 99:  # halt
        self.completed = True
        return
      else:
        print("Unknown opcode: " + str(opcode))
        exit(0)
      
      self.position = self.position + incr_count
      incr_count = 0
      if self.position >= len(self.intcode_array):
        print("int codes fully consumed with no halt.")
        self.completed = True
        return None
      
      if prev_output_val != output_val:
        # print("Output value: " + str(output_val))
        prev_output_val = output_val

      prev_opcode = opcode
      prev_params = params

      if prev_opcode == 4:
        # print("Output: {}".format(output_val))
        return output_val

def load_input(input_filename):
  f = open(input_filename, "r")
  return [int(val) for val in f.readline().split(",")]

def amplifier_loop(start_phase, end_phase, intcode_array):
  num_completed = 0
  highest_output = 0
  phase_list = list(permutations(range(start_phase, end_phase+1)))
  computer_list = []
  for phase_combo in phase_list:
    amp_output = 0
    for phase_setting in phase_combo:
      input_vals = []
      input_vals.append(phase_setting)
      input_vals.append(amp_output)

      # print("Run intcode with input: [{}, {}]".format(input_vals[0], input_vals[1]))
      int_comp = IntcodeComputer(deepcopy(intcode_array), input_vals)
      amp_output = int_comp.run_computer()
      computer_list.append(int_comp)
      
      if amp_output is not None and amp_output > highest_output: highest_output = amp_output
    
  print("Computers setup")

  comp_idx = 0
  last_output = amp_output
  while num_completed != len(computer_list):
    curr_comp = computer_list[comp_idx]
    if last_output is not None: curr_comp.input_queue.append(last_output)

    amp_output = curr_comp.run_computer()

    if amp_output is not None:
      last_output = amp_output
      if amp_output > highest_output: highest_output = amp_output
    else:
      last_output = None

    if curr_comp.completed: num_completed += 1
    comp_idx != 1
    if comp_idx == len(computer_list) - 1: comp_idx = 0

  return highest_output

if __name__ == '__main__':
  # input_array = load_input("../input.txt")
  # print("Input length: {}".format(len(input_array)))

  # output = amplifier_loop(0, 4, input_array)
  

  # Solutions
  input_array = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
  output = amplifier_loop(0, 4, input_array)
  print("Part 1: {}".format(output))

  input_array = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
  output = amplifier_loop(5, 9, input_array)
  print("Part 2: {}".format(output))
