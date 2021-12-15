def load_input(input_filename):
  f = open(input_filename, "r")

  input_output = [ line.strip().split(" | ") for line in f.readlines() ]
  
  return [[i[0].split(" "), i[1].split(" ")] for i in input_output]

def determine_numbers(segment_array):
  number_dict = {
    0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None
  }
  loop_count = 0
  while len([key for key in list(number_dict.values()) if key is None]) != 0 and loop_count < 200:
    loop_count += 1
    for seg in segment_array:
      if seg in list(number_dict.values()): continue
      # print(seg, list(number_dict.values()))

      # 1
      if number_dict[1] is None and len(seg) == 2:
        number_dict[1] = seg
      #4
      if number_dict[4] is None and len(seg) == 4:
        number_dict[4] = seg
      #7
      if number_dict[7] is None and len(seg) == 3:
        number_dict[7] = seg
      #8
      if number_dict[8] is None and len(seg) == 7:
        number_dict[8] = seg

      if number_dict[1] is not None and number_dict[4] is not None and number_dict[7] is not None and number_dict[8] is not None:
        ### 6 segments
        #9
        if number_dict[9] is None and len(seg) == 6:
          tester = True
          for t_char in number_dict[4]:
            if t_char not in seg:
              tester = False 
              break
          if tester:
            number_dict[9] = seg
            continue

        #0
        if number_dict[0] is None and len(seg) == 6 and number_dict[9] is not None:
          tester = True
          for t_char in number_dict[1]:
            if t_char not in seg:
              tester = False 
              break
          if tester:
            number_dict[0] = seg
            continue

        #6
        if number_dict[6] is None and len(seg) == 6 and number_dict[9] is not None and number_dict[0] is not None:
          number_dict[6] = seg
          continue

        if number_dict[9] is not None and number_dict[0] is not None and number_dict[6] is not None:
          ### 5 segments

          #3
          if number_dict[3] is None and len(seg) == 5:
            tester = True
            for t_char in number_dict[1]:
              if t_char not in seg:
                tester = False 
                break
            if tester:
              number_dict[3] = seg
              continue

          #5
          if number_dict[5] is None and len(seg) == 5 and number_dict[3] is not None:
            tester = True
            for t_char in seg:
              if t_char not in number_dict[6]:
                tester = False 
                break
            if tester:
              number_dict[5] = seg
              continue
          
          #2
          if number_dict[2] is None and len(seg) == 5 and number_dict[3] is not None and number_dict[5] is not None:
            number_dict[2] = seg
            continue
  
  seg_dict = {}
  for key in number_dict:
    seg_dict[number_dict[key]] = key
  return seg_dict, number_dict

def compare_string_chars(string1, string2):
  if len(string1) != len(string2): return False
  for t_char in string1:
    if t_char not in string2: return False
  return True

def solve_part1(fish_array):
  num_count = 0
  for line in fish_array:
    seg_dict, number_dict = determine_numbers(line[0])
    # print(seg_dict)
    for seg in line[1]:
      rearr_seg = [arr_seg for arr_seg in seg_dict.keys() if compare_string_chars(seg, arr_seg)][0]
      if seg_dict[rearr_seg] in [1, 4, 7, 8]:
        num_count += 1

  return num_count

def solve_part2(fish_array):
  num_sum = 0
  for line in fish_array:
    seg_dict, number_dict = determine_numbers(line[0])
    # print(seg_dict)
    num_str = ""
    for seg in line[1]:
      rearr_seg = [arr_seg for arr_seg in seg_dict.keys() if compare_string_chars(seg, arr_seg)][0]
      num_str += str(seg_dict[rearr_seg])
    num_sum += int(num_str)

  return num_sum

if __name__ == '__main__':
  fish_array = load_input("../input.txt")
  # fish_array = load_input("../test-input1.txt")

  # print(fish_array)

  # part 1 solution
  solution = solve_part1(fish_array)
  print("Part 1: {}".format(solution))

  # part 2 solution
  solution = solve_part2(fish_array)
  print("Part 2: {}".format(solution)) # 3787 too low
