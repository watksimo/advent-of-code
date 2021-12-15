import statistics
def load_input(input_filename):
  f = open(input_filename, "r")
  return [int(val) for val in f.readline().split(',')]

def solve_part1(fish_array):
  fuel_cost = 0
  median_val = statistics.median(fish_array)
  for val in fish_array: fuel_cost += abs(val-median_val)
  return fuel_cost

def triangular_number(n):
  return sum(range(n + 1))

def solve_part2(fish_array):
  min_horiz = min(fish_array)
  max_horiz = max(fish_array)

  low_fuel = None
  low_val = None
  for val1 in range(min_horiz, max_horiz+1):
    fuel = 0
    for idx2, val2 in enumerate(fish_array):
      if val1 == val2: continue
      dist = abs(val2 - val1)
      fuel += triangular_number(dist)
    if low_fuel is None or fuel < low_fuel:
      low_fuel = fuel
      low_val = val1
    # print(val1, fuel)

  # print(low_val, low_fuel)
  return low_fuel


if __name__ == '__main__':
  fish_array = load_input("../input.txt")
  # fish_array = load_input("../test-input1.txt")

  # part 1 solution
  solution = solve_part1(fish_array)
  print("Part 1: {}".format(solution))

  # part 2 solution
  solution = solve_part2(fish_array)
  print("Part 2: {}".format(solution))
