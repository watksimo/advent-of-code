import math

def fuel_calc(mass):
  return math.floor(mass/3) - 2

def load_input(input_filename):
  f = open(input_filename, "r")
  return [int(line.strip()) for line in f.readlines()]

def solve_part1(input_array):
  return [fuel_calc(val) for val in input_array]

# def solve_part2(input_array):
if __name__ == '__main__':
  input_array = load_input("../input.txt")

  # part 1 solution
  fuel_array = solve_part1(input_array)
  total_fuel = sum(fuel_array)
  print("Part 1: {}".format(total_fuel))

  # part 2 solution
  fuel_provision = []

  for fuel in fuel_array:
    fuel_prov = fuel_calc(fuel)
    while fuel_prov > 0:
      fuel_provision.append(fuel_prov)
      fuel_prov = fuel_calc(fuel_prov)

  total_part2_fuel = total_fuel + sum(fuel_provision)
  print("Part 2: {}".format(total_part2_fuel))
