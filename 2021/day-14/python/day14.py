import copy

def load_input(input_filename):
  f = open(input_filename, "r")
  start_word = []
  char_map = {}
  char_map2 = {}
  for line in f.readlines():
    if len(start_word) == 0:
      start_word = list(line.strip())
      continue
    if line.strip() == '': continue
    tmp_char = line.strip().split(' -> ')
    char_map[tmp_char[0]] = tmp_char[1]
    char_map2[tmp_char[0]] = {
      'occurrences': 0,
      'creates': [tmp_char[0][0] + tmp_char[1], tmp_char[1] + tmp_char[0][1]]
    }
  for char_idx, char_val in enumerate(start_word):
    if char_idx + 1 >= len(start_word): break
    comb = char_val + start_word[char_idx + 1]
    char_map2[comb]['occurrences'] += 1

  return start_word, char_map, char_map2

def step_word(start_word, char_map):
  new_word = start_word.copy()
  for char_idx, char_val in enumerate(start_word):
    if char_idx + 1 >= len(start_word): break
    comb = char_val + start_word[char_idx + 1]
    new_word[char_idx] = char_val + char_map[comb]
  new_word_split = []
  for chars in new_word: new_word_split.extend(list(chars))
  return new_word_split

def step_word2(char_map2):
  new_char_map = copy.deepcopy(char_map2)
  for char_comb in new_char_map: new_char_map[char_comb]['occurrences'] = 0
  for char_comb in char_map2:
    if char_map2[char_comb]['occurrences'] > 0:
      for char_create in char_map2[char_comb]['creates']:
        new_char_map[char_create]['occurrences'] += char_map2[char_comb]['occurrences']
  return new_char_map

def most_least_common2(char_map2, last_char):
  occ_map = {}
  for comb in char_map2:
    char_list = [comb[0]]
    occur = char_map2[comb]['occurrences']
    for ch in char_list:
      if ch in occ_map:
        occ_map[ch] += (1 * occur)
      else:
        occ_map[ch] = occur
  if last_char in occ_map:
    occ_map[last_char] += 1
  else:
    occ_map[last_char] = 1
  return occ_map

def most_least_common(start_word):
  char_set = set(start_word)
  most_common = 0
  least_common = 999999
  for char_val in char_set:
    char_occ = start_word.count(char_val)
    if char_occ > most_common:
      most_common = char_occ
    if char_occ < least_common:
      least_common = char_occ
  return least_common, most_common

if __name__ == '__main__':
  start_word, char_map, char_map2 = load_input("../input.txt")

  # inefficient part 1 solution
  new_word = start_word.copy()
  test_iter = 1
  test_word = []
  part1 = []
  part2 = []
  for i in range(0, 10):
    new_word = step_word(new_word, char_map)
    if i == test_iter - 1: test_word = new_word.copy()
    if i == 9: 
      part1 = new_word
      lc, mc = most_least_common(new_word)
      # part 1 solution
      part1_solution = mc - lc
      print("Part 1: {}".format(part1_solution))

  # part 1 & 2 solved using pair count method - efficient
  for i in range(0, 40):
    char_map2 = step_word2(char_map2)
    if i == 9:
      mlc2 = most_least_common2(char_map2, start_word[-1])
      occ_list = mlc2.values()
      part1_solution = max(occ_list) - min(occ_list)
      print("Part 1: {}".format(part1_solution))
  mlc2 = most_least_common2(char_map2, start_word[-1])
  occ_list = mlc2.values()
  part2_solution = max(occ_list) - min(occ_list)
  print("Part 2: {}".format(part2_solution))
  

