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

def amplifier_loop(num_aplifiers, intcode_array):
  highest_output = 0
  phase_list = list(permutations(range(num_aplifiers)))
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
  return highest_output

if __name__ == '__main__':
  input_array = load_input("../input.txt")
  print("Input length: {}".format(len(input_array)))

  output = amplifier_loop(5, input_array)

  # Solutions
  print("Part 1: {}".format(output))
