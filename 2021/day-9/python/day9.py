def load_input(input_filename):
  f = open(input_filename, "r")
  return [[int(ch1) for ch1 in list(line.strip())] for line in f.readlines()]

def get_neighbours(lava_map, pos):
  row = pos[0]
  col = pos[1]

  neighbours = [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]
  neighbours = [pt for pt in neighbours if ((pt[0] >= 0 and pt[0] < len(lava_map)) and (pt[1] >= 0 and pt[1] < len(lava_map[0])))]

  return neighbours

def find_low_points(lava_map):
  low_points = []
  low_point_idxs = []
  for row_idx, row in enumerate(lava_map):
    for col_idx, col in enumerate(row):
      neighbours = get_neighbours(lava_map, (row_idx, col_idx))
      lower_points = []
      for pt in neighbours:
        n_val = lava_map[pt[0]][pt[1]]
        if n_val <= col:
          lower_points.append(n_val)
      if len(lower_points) == 0:
        low_points.append(col)
        low_point_idxs.append((row_idx, col_idx))

  return low_point_idxs, low_points

def get_basins(lava_map, low_points):
  basin_dict = {}
  for lp in low_points:
    lp_val = lava_map[lp[0]][lp[1]]
    basin = [lp_val]
    print(lp)
    for lp_row_idx in range(lp[0], -1, -1):
      pos_val = lava_map[lp_row_idx][lp[1]]
      if pos_val == 9: break
      basin.append(pos_val)
    basin_dict[",".join([str(_) for _ in lp])] = basin
      
  return basin_dict

if __name__ == '__main__':
  # fish_array = load_input("../input.txt")
  fish_array = load_input("../test-input1.txt")

  # part 1 solution
  low_point_indexes, low_point_values = find_low_points(fish_array)
  risk_lvl = sum([v+1 for v in low_point_values])
  # print(low_point_values)
  # print("Part 1: {}".format(risk_lvl))  #1574 too high

  print(get_basins(fish_array, low_point_indexes))

  # # part 2 solution
  # solution = solve_part2(fish_array)
  # print("Part 2: {}".format(solution))
