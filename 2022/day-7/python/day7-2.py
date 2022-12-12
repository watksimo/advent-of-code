part1 = []
part2 = None
to_free = 0
class TreeNode:
  def __init__(self, name, parent):
    self.name = name
    self.parent = parent
    self.children = []
    self.size = 0
    self.recurse_size = 0

  def __repr__(self):
    return f"{self.name}({self.size})(r: {self.recurse_size}): {[key for key in self.children]}"

  def get_sizes(self):
    global part1
    if len(self.children) == 0: 
      self.recurse_size += self.size
      return self.recurse_size
    else:
      for child in self.children:
        self.recurse_size += child.get_sizes()

    if self.recurse_size <= 100000:
      part1.append(self)
    return self.recurse_size

  def iterate_tree(self):
    global part2, to_free
    if len(self.children) == 0: 
      return
    else:
      for child in self.children:
        child.iterate_tree()

    if self.recurse_size >= to_free and (part2 is None or self.recurse_size < part2.recurse_size):
      print(f"Inside: {self}, TO_free: {to_free}")
      part2 = self
    return

def load_input(input_filename):
  base_node = TreeNode('/', None)

  tree = base_node
  curr_loc = base_node

  f = open(input_filename, "r")
  curr_command = None
  for line in f.readlines():
    line = line.strip()
    line_elems = line.split(" ")

    curr_child_names = [a.name for a in curr_loc.children]

    print("START")
    print(f"Line: {line}")
    print(f"Curr loc: {curr_loc.name}")
    print(f"curr_child_names: {curr_child_names}")

    if line_elems[0] == "$":  # command
      curr_command = None
      command = line_elems[1]
      if command == 'cd':
        folder_name = line_elems[2]
        if folder_name == '/':
          continue
        elif folder_name == "..":
          curr_loc = curr_loc.parent
        else:
          print(f"Folder name: {folder_name}")
          if folder_name not in curr_child_names and folder_name != curr_loc.name:
            # print(f"Before add : {curr_loc.name} contains {[key for key in curr_loc.files]}")
            new_node = TreeNode(folder_name, curr_loc)
            curr_loc.children.append(new_node)
            curr_loc = new_node
            # print(f"After add : {curr_loc.name} contains {[key for key in curr_loc.files]}")
          else:
            for child in curr_loc.children:
              if child.name == folder_name:
                curr_loc = child
                break
          # print(f"Changing curr location to {curr_loc.name}")
          # print(f"New curr loc : {curr_loc.name} contains {[key for key in curr_loc.files]}")
      elif command == 'ls':
        curr_command = 'ls'
    elif curr_command == 'ls':
      print("Inside LS")
      if line_elems[1] not in curr_child_names:
        print(f"Adding {line_elems[1]}")
        new_node = TreeNode(line_elems[1], curr_loc)
        curr_loc.children.append(new_node)
        if 'dir' not in line_elems: new_node.size = int(line_elems[0])

    print("END")
    print(f"Line: {line}")
    print(f"Curr loc: {curr_loc.name}")
    print(f"curr_child_names: {[a.name for a in curr_loc.children]}")

  return tree


def solve_part1(input_array):
  score = 0
  
  for idx, char in enumerate(input_array):
    seq = input_array[idx:idx+4]
    # print(seq)
    if len(set(seq)) == 4: return idx+4
  

def solve_part2(file_tree):
  total_space = 70000000
  required_space = 30000000
  remaining_space = 70000000 - file_tree.recurse_size
  global to_free
  to_free = 30000000 - remaining_space

  file_tree.iterate_tree()

  print(f"We need to free {to_free}")


if __name__ == '__main__':
  # file_tree = load_input("../test-input1.txt")
  file_tree = load_input("../input.txt")
  file_tree.get_sizes()
  # print(file_tree)
  print(f"part1 solution: {sum([n.recurse_size for n in part1])}")

  # print(get_all_weight(input_array['/'], 0))
  

  # print_children(input_array['/'], '/')
  # print("SCORING")
  # score = score_dir(input_array['/'], '/', 0)

  # exit()

  # part 2 solution
  part2_solution = solve_part2(file_tree)
  # 2391728 too high
  print("Part 2: {}".format(part2.recurse_size))
