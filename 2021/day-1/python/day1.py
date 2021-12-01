
def load_input(input_filename):
  f = open(input_filename, "r")
  return [int(line.strip()) for line in f.readlines()]

def solve_part1(input_array):
  prev_depth = None
  increase_cnt = 0
  for depth in input_array:
    if prev_depth is not None and depth > prev_depth:
      increase_cnt += 1
    prev_depth = depth

  return increase_cnt

def solve_part2(input_array):
  window = [None, None, None]
  increase_cnt = 0
  prev_window = None

  array_length = len(input_array)

  for idx, depth in enumerate(input_array):
    if idx + 3 > array_length:
      return increase_cnt
    window = sum(input_array[idx:idx+3])
    if prev_window is not None and window > prev_window:
      increase_cnt += 1
    prev_window = window


if __name__ == '__main__':
  input_array = load_input("../input.txt")

  # part 1 solution
  increase_count = solve_part1(input_array)

  print("Part 1: {}".format(increase_count))

  # part 2 solution
  increase_count = solve_part2(input_array)
  print("Part 2: {}".format(increase_count))
