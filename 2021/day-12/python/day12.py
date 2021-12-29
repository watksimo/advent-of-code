def load_input(input_filename):
  f = open(input_filename, "r")
  map_dict = {}
  for line in f.readlines():
    nodes = line.strip().split("-")
    if nodes[0] not in map_dict: map_dict[nodes[0]] = {'neighbours': []}
    if nodes[1] not in map_dict: map_dict[nodes[1]] = {'neighbours': []}
    if nodes[1] != 'start': map_dict[nodes[0]]['neighbours'].append(nodes[1])
    if nodes[0] != 'start': map_dict[nodes[1]]['neighbours'].append(nodes[0])

  return map_dict

def split_path_list(path_list, start_node):
    split_path_list = []
    split_path = []
    for node in path_list:
      if node == start_node:
        if len(split_path) != 0: split_path_list.append(split_path)
        split_path = [node]
      else:
        split_path.append(node)
    if len(split_path) != 0: split_path_list.append(split_path)

    return split_path_list

def solve_part1(map_dict, start_node, end_node, visited):
  path_list = []
  new_visit = visited + [start_node]

  if start_node == end_node:
    return new_visit
  for neighbour in map_dict[start_node]['neighbours']:
    if neighbour.isupper() or neighbour not in visited:
      temp_path = solve_part1(map_dict, neighbour, end_node, new_visit)
      path_list.extend(temp_path)

  return path_list

def solve_part2(map_dict, start_node, end_node, visited, small_cave_dbl):
  # print(map_dict, start_node, end_node, visited, small_cave_dbl)
  path_list = []
  new_visit = visited + [start_node]

  if start_node == end_node:
    return new_visit
  for neighbour in map_dict[start_node]['neighbours']:
    dbl = len([a for a in new_visit if a.islower() and a!='start' and a!='end' and new_visit.count(a) > 1]) > 0
    if neighbour.isupper():
      temp_path = solve_part2(map_dict, neighbour, end_node, new_visit, small_cave_dbl)
      path_list.extend(temp_path)
    elif neighbour not in visited or not dbl:
      temp_path = solve_part2(map_dict, neighbour, end_node, new_visit, small_cave_dbl)
      path_list.extend(temp_path)
    # elif not small_cave_dbl and neighbour in visited:
    #   small_cave_dbl = True
    #   temp_path = solve_part2(map_dict, neighbour, end_node, new_visit, small_cave_dbl)
    #   path_list.extend(temp_path)

  return path_list

if __name__ == '__main__':
  map_dict = load_input("../input.txt")
  # map_dict = load_input("../test-input1.txt")
  # map_dict = load_input("../test-input2.txt")
  # map_dict = load_input("../test-input3.txt")
  # print(map_dict)

  # part 1 solution
  all_paths = solve_part1(map_dict, 'start', 'end', [])  
  all_paths = split_path_list(all_paths, 'start')
  print("Part 1: {}".format(len(all_paths)))

  # part 2 solution
  all_paths = solve_part2(map_dict, 'start', 'end', [], False)  
  all_paths = split_path_list(all_paths, 'start')
  print("Part 2: {}".format(len(all_paths)))
