
def load_input(input_filename):
  return_map = {'boards':[]}
  first_line = True
  f = open(input_filename, "r")

  board_array = []
  for line in f.readlines():
    if first_line and line.strip() != "":
      return_map['draw_order'] = [int(num) for num in line.strip().split(',')]
    elif first_line and line.strip() == "":
      first_line = False
    elif line.strip() == "":
      if len(board_array) > 0:
        return_map['boards'].append(board_array)
        board_array = []
    else:
      board_array.append([int(num) for num in line.strip().split()])
  return_map['boards'].append(board_array)
  return return_map

# Negative numbers indicate that the number has been checked off
def check_win(marked_board):
  row_one = True
  for idx, line in enumerate(marked_board):
    row_marked = [num for num in line if num > 0]
    if len(row_marked) == 0: return True

    col_marked = [line[idx] for line in marked_board if line[idx] > 0]
    if len(col_marked) == 0: return True
    if row_one: row_one = False

  return False

def mark_on_boards(board_array, draw_num):
  for board_idx, board in enumerate(board_array):
    for row_idx, row in enumerate(board):
      for num_idx, num in enumerate(row):
        if num == draw_num: board_array[board_idx][row_idx][num_idx] = num * -1

def calculate_board_score(board):
  score = 0
  for row in board:
    for num in row:
      if num > 0: score += num
  return score

def solve_part1(input_map):
  for draw_num in input_map['draw_order']:
    mark_on_boards(input_array['boards'], draw_num)
    for board in input_map['boards']:
      if check_win(board): 
        return calculate_board_score(board) * draw_num
  return None

def solve_part2(input_map):
  complete_board_idx = []
  for draw_num in input_map['draw_order']:
    mark_on_boards(input_array['boards'], draw_num)
    for board_idx, board in enumerate(input_map['boards']):
      if board_idx not in complete_board_idx and check_win(board):
        complete_board_idx.append(board_idx)
        if len(input_array['boards']) == len(complete_board_idx):
          return calculate_board_score(board) * draw_num
          
  return None
  

if __name__ == '__main__':
  input_array = load_input("../input.txt")
  # input_array = load_input("../test-input1.txt")

  # print(input_array['draw_order'], input_array['boards'])

  # part 1 solution
  final_score1 = solve_part1(input_array)
  print("Part 1: {}".format(final_score1))

  # # part 2 solution
  final_score2 = solve_part2(input_array)
  print("Part 2: {}".format(final_score2))
