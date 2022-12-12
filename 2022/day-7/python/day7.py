class SysObj:
  def __init__(self, name, parent, type, size, files):
    self.name = name
    self.parent = parent
    self.type = type
    self.size = int(size)
    self.files = files

  def __repr__(self):
    return f"{self.name}: {[key for key in self.files]}"
    return f"SysObj({self.type}, {self.size}, {self.files})"

def load_input(input_filename):
  file_system = {
    '/': SysObj('/', None, 'd', 0, {})
  }
  

  curr_loc = file_system['/']

  f = open(input_filename, "r")
  curr_command = None
  for line in f.readlines():
    # print(f"Curr loc: {curr_loc.name}. Children: {[key for key in curr_loc.files]}")
    line = line.strip()
    line_elems = line.split(" ")

    if line_elems[0] == "$":  # command
      print(f"Command: {line}")
      # print(f"Curr loc: {curr_loc.name}")
      curr_command = None
      command = line_elems[1]
      if command == 'cd':
        folder_name = line_elems[2]
        if folder_name == '/':
          continue
        elif folder_name == "..":
          curr_loc = curr_loc.parent
        else:
          if folder_name not in curr_loc.files and folder_name != curr_loc.name:
            print(f"Before add : {curr_loc.name} contains {[key for key in curr_loc.files]}")
            curr_loc.files[folder_name] = SysObj(folder_name, curr_loc, 'd', 0, {})
            print(f"After add : {curr_loc.name} contains {[key for key in curr_loc.files]}")
          curr_loc = curr_loc.files[folder_name]
          print(f"New curr loc : {curr_loc.name} contains {[key for key in curr_loc.files]}")
      elif command == 'ls':
        curr_command = 'ls'
    elif curr_command == 'ls':
      # print("Inside ls command")
      # print(line)
      if line_elems[0] == 'dir':
        if line_elems[1] not in curr_loc.files:
          curr_loc.files[line_elems[1]] = SysObj(line_elems[1], curr_loc, 'd', 0, {})
      else:
        curr_loc.files[line_elems[1]] = SysObj(line_elems[1], curr_loc, 'f', line_elems[0], {})
  return file_system
  
def print_children(curr_loc, name):
  if curr_loc.type == 'f' or len(curr_loc.files) == 0: print(name)
  else: 
    for child in curr_loc.files:
      print(child)
      print_children(curr_loc.files[child], child)

def get_all_weight(node, score):
  print(f"Get all weight: {node.name}, {score}")
  if len(node.files) == 0:
    return score + node.size
  else:
    for child in node.files:
      print(f"Recalling getAllWeight with score {score + node.size}")
      get_all_weight(node.files[child], score + node.size)



def solve_part1(input_array):
  score = 0
  
  for idx, char in enumerate(input_array):
    seq = input_array[idx:idx+4]
    # print(seq)
    if len(set(seq)) == 4: return idx+4
  

def solve_part2(input_array):
  score = 0
  
  for idx, char in enumerate(input_array):
    seq = input_array[idx:idx+14]
    # print(seq)
    if len(set(seq)) == 14: return idx+14


if __name__ == '__main__':
  input_array = load_input("../test-input1.txt")
  # input_array = load_input("../input.txt")
  print(input_array)
  print(get_all_weight(input_array['/'], 0))
  

  # print_children(input_array['/'], '/')
  # print("SCORING")
  # score = score_dir(input_array['/'], '/', 0)

  exit()
  
  # part 1 solution
  part1_solution = solve_part1(input_array)
  print("Part 1: {}".format(part1_solution))
  exit()
  

  # part 2 solution
  part2_solution = solve_part2(input_array)
  print("Part 2: {}".format(part2_solution))
