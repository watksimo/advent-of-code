
def load_input(input_filename):
  f = open(input_filename, "r")
  coords = [ line.strip().split(" -> ") for line in f.readlines() ]

  new_coords = []
  for i in coords:
    new_coords.append([[int(k) for k in i[0].split(",")], [int(l) for l in i[1].split(",")]])

  return new_coords

def is_horiz_vertic(coords):
  if coords[0][0] == coords[1][0]:
    # print("Coord {} -> {} is vertical".format(coords[0], coords[1]))
    return True

  elif coords[0][1] == coords[1][1]:
    # print("Coord {} -> {} is horizontal".format(coords[0], coords[1]))
    return True
  else:
    return False

def get_horiz_line_points(coords):
  points = []
  if coords[0][0] == coords[1][0]:
    min_val = min(coords[0][1], coords[1][1])
    max_val = max(coords[0][1], coords[1][1])
    for i in range(min_val, max_val + 1): points.append([coords[0][0], i])
  elif coords[0][1] == coords[1][1]:
    min_val = min(coords[0][0], coords[1][0])
    max_val = max(coords[0][0], coords[1][0])
    for i in range(min_val, max_val + 1): points.append([i, coords[0][1]])

  return points

def get_diag_line_points(coords):
  points = []
  x_list = list(range(coords[0][0], coords[1][0] + 1) if coords[0][0] <= coords[1][0] else range(coords[0][0], coords[1][0] - 1, -1))
  y_list = list(range(coords[0][1], coords[1][1] + 1) if coords[0][1] <= coords[1][1] else range(coords[0][1], coords[1][1] - 1, -1))

  # print(coords, x_list, y_list)

  for x_idx, x_point in enumerate(x_list):
    points.append([x_point, y_list[x_idx]])

  return points

def solve_part1(coord_array):
  position_count = {}
  for coords in coord_array:
    if is_horiz_vertic(coords):
      points = get_horiz_line_points(coords)
      points_str = [",".join([str(b) for b in a]) for a in points]
      # print(points_str)
      for str_val in points_str:
        if str_val not in position_count:
          position_count[str_val] = 1
        else:
          position_count[str_val] += 1
  return position_count

def solve_part2(input_map):          
  position_count = {}
  for coords in coord_array:
    if is_horiz_vertic(coords):
      points = get_horiz_line_points(coords)
      # print('line')
    else: #is diagonal
      points = get_diag_line_points(coords)
      # print('diag')
    # print(points)

    points_str = [",".join([str(b) for b in a]) for a in points]
    # print(points_str)
    for str_val in points_str:
      if str_val not in position_count:
        position_count[str_val] = 1
      else:
        position_count[str_val] += 1
    
  return position_count
  

if __name__ == '__main__':
  coord_array = load_input("../input.txt")
  # coord_array = load_input("../test-input1.txt")

  # part 1 solution
  position_count = solve_part1(coord_array)
  multiple_overlaps = len( [overlaps for overlaps in position_count.values() if overlaps > 1] )
  print("Part 1: {}".format(multiple_overlaps))

  # # part 2 solution
  position_count = solve_part2(coord_array)
  multiple_overlaps = len( [overlaps for overlaps in position_count.values() if overlaps > 1] )
  print("Part 2: {}".format(multiple_overlaps))
