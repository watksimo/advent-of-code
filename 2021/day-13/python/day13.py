# rows = y
# cols = x

def load_input(input_filename):
  f = open(input_filename, "r")
  paper_map = []
  fold_array = []

  folds = False
  for line in f.readlines():
    if line.strip() == '':
      folds = True
      continue
    if not folds:
      coords = [int(_) for _ in line.strip().split(',')]
      increase_map(paper_map, coords[0]+1, coords[1]+1)
      paper_map[coords[1]][coords[0]] = '#'
    else:
      fold_temp = line.strip().split(" ")[-1].split('=')
      fold_temp[1] = int(fold_temp[1])
      fold_array.append(fold_temp)

  return paper_map, fold_array

def fold_x(input_map, x_fold):
  # print_map(input_map, ('x', x_fold))
  new_map_size = max(len(input_map) - x_fold - 1, x_fold)
  new_map = input_map.copy()
  new_map = [row[:new_map_size] for row in new_map]

  for i in range(1, new_map_size + 1):
    left_col = [row[x_fold-i] if x_fold-i >= 0 else '.' for row in input_map]
    right_col = [row[x_fold+i] if x_fold+i < len(row) else '.' for row in input_map]
    combined_col = combine_row(left_col, right_col)
    for col_idx, col in enumerate(combined_col):
      new_map[col_idx][-1 * i] = col

  return new_map

def fold_y(input_map, y_fold):
  # print_map(input_map, ('y', y_fold))
  new_map_size = max(len(input_map) - y_fold - 1, y_fold)
  new_map = input_map.copy()[:new_map_size]

  for i in range(1, new_map_size + 1):
    empty_row = ['.'] * len(input_map[0])
    upper_row = input_map[y_fold - i] if y_fold - i >= 0 else empty_row
    lower_row = input_map[y_fold + i] if y_fold + i < len(input_map) else empty_row
    new_map[-1 * i] = combine_row(lower_row, upper_row)
  
  return new_map

def combine_row(row_1, row_2):
  out_row = ['.'] * len(row_1)
  for idx, val in enumerate(row_1):
    if val == '#' or row_2[idx] == '#': out_row[idx] = '#'

  # print("Combine: ")
  # print(row_1)
  # print(row_2)
  # print(out_row)
  return out_row

def solve_part1(input_array):
  return None

def solve_part2(input_array):
  return None

def increase_map(map, x_size, y_size):
  if y_size > len(map):
    for i in range(len(map), y_size):
      curr_x_size = len(map[0]) if len(map) > 0 else 0
      map.append(["."] * curr_x_size)
  
  if x_size > len(map[0]):
    for idx, row in enumerate(map):
      row.extend(["."] * (x_size-len(row)))

def print_map(map_array, fold_info = None):
  print_map = map_array.copy()
  if fold_info is not None:
    if fold_info[0] == 'y': print_map[fold_info[1]] = ['-'] * len(map_array[0])
    if fold_info[0] == 'x':
      for idx, row in enumerate(print_map): print_map[idx][fold_info[1]] = '|'

  print('--START PRINT MAP--')
  for row in print_map:
    print(''.join(row))
  print('--END PRINT MAP--')

def count_dots(map_array):
  return sum([sum([1 for col in row if col == '#']) for row in map_array])

if __name__ == '__main__':
  paper_map, fold_array = load_input("../input.txt")
  # paper_map, fold_array = load_input("../test-input1.txt")
  # print_map(paper_map)
  # print(fold_array)

  # part 1 solution
  fold_cnt = 0
  folded_map = paper_map.copy()
  part1_solution = None
  for fold_details in fold_array:
    if fold_details[0] == 'x': folded_map = fold_x(folded_map, fold_details[1])
    if fold_details[0] == 'y': folded_map = fold_y(folded_map, fold_details[1])
    fold_cnt += 1

    if fold_cnt == 1:
      part1_solution = count_dots(folded_map)
      print("Part 1: {}".format(part1_solution))  

  # part 2 solution
  print("Part 2:")
  print_map(folded_map)
