
def load_input(input_filename):
  f = open(input_filename, "r")
  elf_count = 1
  elf_dict = {elf_count: 0}

  for line in f.readlines():
    line = line.strip()
    if line == "":
      elf_count += 1
      elf_dict[elf_count] = 0
      continue
    
    elf_dict[elf_count] += int(line)
  return elf_dict

def solve_part1(input_array):
  ordered_vals = [input_array[key] for key in input_array]
  ordered_vals.sort()

  return ordered_vals[-1]

def solve_part2(input_array):
  ordered_vals = [input_array[key] for key in input_array]
  ordered_vals.sort()

  return sum(ordered_vals[-3:])


if __name__ == '__main__':
  # input_array = load_input("../test-input1.txt")
  input_array = load_input("../input.txt")
  
  # part 1 solution
  part1_solution = solve_part1(input_array)
  print("Part 1: {}".format(part1_solution))
  

  # part 2 solution
  part2_solution = solve_part2(input_array)
  print("Part 2: {}".format(part2_solution))
