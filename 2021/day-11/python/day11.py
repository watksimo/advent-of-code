def load_input(input_filename):
  f = open(input_filename, "r")
  return [[int(ch1) for ch1 in list(line.strip())] for line in f.readlines()]

def get_adjacent_coords(map, pos):
  row = pos[0]
  col = pos[1]

  neighbours = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1), (row, col - 1), (row, col + 1), (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
  neighbours = [pt for pt in neighbours if ((pt[0] >= 0 and pt[0] < len(map)) and (pt[1] >= 0 and pt[1] < len(map[0])))]
  neighbours = ["{},{}".format(c[0], c[1]) for c in neighbours]
  return neighbours

def process_map(input_array):
  out_dict = {}
  for row_idx, row_vals in enumerate(input_array):
    for col_idx, col_val in enumerate(row_vals):
      coord_str = "{},{}".format(row_idx, col_idx)
      out_dict[coord_str] = {
        'energy': col_val,
        'adjacent': get_adjacent_coords(input_array, (row_idx, col_idx))
      }

  return out_dict

def iterate_step(oct_dict):
  global flash_cnt
  flashing_oct = []
  for oct_coord in oct_dict:
    oct_dict[oct_coord]['energy'] += 1
    if oct_dict[oct_coord]['energy'] > 9:
      flashing_oct.append(oct_coord)
      oct_dict[oct_coord]['energy'] = 0
      flash_cnt += 1
  flash_neighbours(oct_dict, flashing_oct)

def flash_neighbours(oct_dict, flashing_oct):
  global flash_cnt
  if len(flashing_oct) == 0: return
  new_flashes = []
  for oct in flashing_oct:
    for adj_oct in oct_dict[oct]['adjacent']:
      if oct_dict[adj_oct]['energy'] != 0: oct_dict[adj_oct]['energy'] += 1
      if oct_dict[adj_oct]['energy'] > 9:
        new_flashes.append(adj_oct)
        oct_dict[adj_oct]['energy'] = 0
        flash_cnt += 1
  flash_neighbours(oct_dict, new_flashes)

def check_all_flashing(oct_dict):
  for oct in oct_dict:
    if oct_dict[oct]['energy'] != 0: return False
  return True

def solve_part1(input_array):
  return None

def solve_part2(input_array):
  return None

def print_dict(oct_dict):
  prev_row = None
  for oct in oct_dict:
    row = oct.split(",")[0]
    if prev_row != row:
      print()
      prev_row = row
    print(str(oct_dict[oct]['energy']) + " ", end='')
  print()

flash_cnt = 0

if __name__ == '__main__':
  input_array = load_input("../input.txt")
  # input_array = load_input("../test-input1.txt")
  # input_array = load_input("../test-input2.txt")

  oct_dict = process_map(input_array)

  # part 1 solution
  step_cnt = 0
  while not check_all_flashing(oct_dict):
    iterate_step(oct_dict)
    step_cnt += 1
    if step_cnt == 100: print("Part 1: {}".format(flash_cnt))
  
  # part 2 solution
  print("Part 2: {}".format(step_cnt))
