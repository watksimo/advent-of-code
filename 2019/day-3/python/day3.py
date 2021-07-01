from copy import deepcopy

# Coordinates are +ve U & R, -ve L & D around the central port.
# Coordinates stored as a dict<string, list<string>> where the string key is the coordinate 'U,R' (e.g. 1U & 1L from
#   central is '1,-1'), and the value is a list of string representing the wire that crossed that coordinate.

def load_input(input_filename):
  f = open(input_filename, "r")
  out_array = []
  for line in f.readlines():
    out_array.append([val for val in line.strip().split(",")])
  return out_array

def merge_dicts(dict1, dict2):
  intersects = []
  dict3 = {**dict1, **dict2}
  for key, value in dict3.items():
    if key in dict1 and key in dict2:
      dict3[key] = [value , dict1[key]]
      intersects.append(key)
  return dict3, intersects

def solve_part1(input_array):
  intersects = []
  final_grid = {}
  for wire_no, wire_map in enumerate(input_array):
    # print("----NEW WIRE----")
    steps = 0
    curr_pos = [0,0]
    grid = {}
    for wire_dir in wire_map:
      direction = wire_dir[:1]
      distance = int(wire_dir[1:])
      for step in range(distance):
        steps += 1
        new_step = -1 if (direction in ['L','D']) else 1
        new_pos = curr_pos
        if direction in ['U','D']: new_pos[0] = curr_pos[0] + new_step
        if direction in ['L','R']: new_pos[1] = curr_pos[1] + new_step
        
        new_pos_str = ','.join([str(_) for _ in new_pos])
        # print(wire_dir, new_pos_str, steps)
        if new_pos_str not in grid:
          grid[new_pos_str] = steps
        # We don't care about points we've already been to
        # else:
        #   grid[new_pos_str].append(steps)
        #   intersects.append(new_pos_str)
        curr_pos = new_pos
    final_grid, new_intersects = merge_dicts(final_grid, grid)
    intersects.extend(new_intersects)

  return final_grid, intersects

if __name__ == '__main__':
  input_array = load_input("../input.txt")
  part1_grid, part1_intersects = solve_part1(input_array)

  # part 1 solution
  intersect_coords = [[abs(int(_)) for _ in pos.split(',')] for pos in part1_intersects]
  min_manhattan = min([sum(_) for _ in intersect_coords])
  print("Part 1 solution: {}".format(min_manhattan))

  # part 2 solution
  min_steps = min([sum(part1_grid[pos]) for pos in part1_intersects])
  print("Part 2 solution: {}".format(min_steps))

