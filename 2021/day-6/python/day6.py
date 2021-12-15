
def load_input(input_filename):
  f = open(input_filename, "r")
  return [int(val) for val in f.readline().split(',')]

def solve_part1(fish_array, num_days):
  fish_dict = {}
  for interval in range(0, 9): fish_dict[interval] = 0

  for fish_int in fish_array: fish_dict[fish_int] += 1
  for i in range(0, num_days): progress_day(fish_dict)

  return sum(list(fish_dict.values()))

def progress_day(fish_dict):
  prev_day = None
  for interval in range(8, -1, -1):
    if interval == 8:
      prev_day = fish_dict[interval]
      continue

    temp = fish_dict[interval]
    fish_dict[interval] = prev_day
    prev_day = temp
  fish_dict[6] += prev_day
  fish_dict[8] = prev_day

  return fish_dict

def solve_part2(fish_array):
  return None

if __name__ == '__main__':
  fish_array = load_input("../input.txt")
  # fish_array = load_input("../test-input1.txt")

  # part 1 solution
  solution = solve_part1(fish_array, 80)
  print("Part 1: {}".format(solution))

  # part 2 solution
  solution = solve_part1(fish_array, 256)
  print("Part 2: {}".format(solution))
