def load_input(input_filename):
  # 1, 5, 9, 13
  # 0, 1, 2, 3
  stack_dict = {}
  moves = []
  f = open(input_filename, "r")

  all_stacks = False

  for line in f.readlines():
    line = line.rstrip('\n') 
    
    if not all_stacks:
      if "[" in line:
        cnt = 1
        line_list = list(line)
        while cnt < len(line_list):
          stack_num = int((cnt-1)/4) + 1
          if stack_num not in stack_dict: stack_dict[stack_num] = []
          if line_list[cnt] != " ": stack_dict[stack_num].append(line_list[cnt])
          cnt += 4
      elif line == "":
        all_stacks = True
      continue

    move_item = line.split(" ")
    moves.append([int(move_item[1]), [int(move_item[-3]), int(move_item[-1])]])
  
  return stack_dict, moves
  

def solve_part1(stack_dict, moves):
  
  for move in moves:
    for cnt in range(move[0]):
      from_stack = move[1][0]
      to_stack = move[1][1]
      stack_dict[to_stack].insert(0, stack_dict[from_stack].pop(0))
  
  return ''.join([stack_dict[key][0] for key in stack_dict])

def solve_part2(stack_dict, moves):
  print(stack_dict)
  for move in moves:
    from_stack = move[1][0]
    to_stack = move[1][1]
    move_stack = stack_dict[from_stack][:move[0]]
    stay_stack = stack_dict[from_stack][move[0]:]

    stack_dict[to_stack] = move_stack + stack_dict[to_stack]
    stack_dict[from_stack] = stay_stack    

    # print(stack_dict)
  
  return ''.join([stack_dict[key][0] for key in stack_dict])


if __name__ == '__main__':
  # stacks, moves = load_input("../test-input1.txt")
  stacks, moves = load_input("../input.txt")
  print(stacks, moves)
  # exit()
  
  # part 1 solution
  part1_solution = solve_part1(stacks, moves)
  print("Part 1: {}".format(part1_solution))
  # exit()
  

  # part 2 solution
  stacks, moves = load_input("../input.txt")
  part2_solution = solve_part2(stacks, moves)
  print("Part 2: {}".format(part2_solution))
