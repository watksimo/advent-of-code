import math
def load_input(input_filename):
  f = open(input_filename, "r")
  return [list(line.strip()) for line in f.readlines()]

def create_asteroid_dict(input_array):
  asteroids = {}
  for row_idx, row in enumerate(input_array):
    for col_idx, cell in enumerate(row):
      if cell == '#':
        idx_str = "{},{}".format(str(row_idx), str(col_idx))
        asteroids[idx_str] = {}
  return asteroids

def solve_part1(input_array):
  asteroids = create_asteroid_dict(input_array)

  # Compare each asteroid to all other asteroids
  for idx_str in asteroids:
    for idx_str2 in asteroids:
      if idx_str != idx_str2:
        x1 = int(idx_str.split(",")[0])
        y1 = int(idx_str.split(",")[1])
        x2 = int(idx_str2.split(",")[0])
        y2 = int(idx_str2.split(",")[1])
        slope = math.atan2(y2-y1, x2-x1)
        if slope not in asteroids[idx_str]:
          asteroids[idx_str][slope] = {'cannot see': [], 'can see': idx_str2}
        else:
          curr_see = asteroids[idx_str][slope]['can see']
          ref_x = x1
          ref_y = y1
          see_x = int(curr_see.split(",")[0])
          see_y = int(curr_see.split(",")[1])
          new_x = x2
          new_y = y2
          see_dist = math.dist((ref_x, ref_y), (see_x, see_y))
          new_dist = math.dist((ref_x, ref_y), (new_x, new_y))
          if see_dist < new_dist:
            asteroids[idx_str][slope]['cannot see'].append(idx_str2)
          else:
            asteroids[idx_str][slope]['cannot see'].append(curr_see)
            asteroids[idx_str][slope]['can see'] = idx_str2

  viewable_asteroid_cnt = [(ast, len([(aa['can see']) for aa in asteroids[ast].values()])) for ast in asteroids]

  viewable_asteroids = [(ast, [(aa['can see']) for aa in asteroids[ast].values()], [(aa['cannot see']) for aa in asteroids[ast].values()]) for ast in asteroids]

  most_view_cnt = 0
  most_view_ast = None
  for ast in viewable_asteroid_cnt:
    if ast[1] > most_view_cnt:
      most_view_ast = ast[0]
      most_view_cnt = ast[1]

  return most_view_ast, most_view_cnt

if __name__ == '__main__':
  input_array = load_input("../input.txt")
  most_view_ast, most_view_cnt = solve_part1(input_array)

  print("Part 1: Best is {}, {} with {} other asteroids".format(most_view_ast.split(",")[1], most_view_ast.split(",")[0], most_view_cnt))