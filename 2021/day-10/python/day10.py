from collections import deque
import math

def load_input(input_filename):
  f = open(input_filename, "r")
  return [list(line.strip()) for line in f.readlines()]

def solve_part1(input_array):
  close_dict = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
  }

  score_dict = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137
  }

  brace_q = []
  incorrect_closes = []

  for line in input_array:
    for brace in line:
      if brace in close_dict.values():
        brace_q.append(brace)
      else:
        match = brace_q.pop()
        expected = close_dict[brace]
        if match != expected: incorrect_closes.append(brace)

  score = sum([score_dict[close_brace] for close_brace in incorrect_closes])
  return score


def solve_part2(input_array):
  
  close_dict = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
  }
  open_dict = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
  }

  score_dict = {
    ')' : 1,
    ']' : 2,
    '}' : 3,
    '>' : 4
  }

  line_completions = []

  for line in input_array:
    brace_q = []
    for brace in line:
      if brace in close_dict.values():
        brace_q.append(brace)
      else:
        match = brace_q[-1]
        expected = close_dict[brace]
        if match != expected:
          brace_q = []
          break
        else:
          brace_q.pop()

    if len(brace_q) != 0:
      cl = []
      for b in brace_q: cl.insert(0, open_dict[b])
      line_completions.append(cl)

    score_list = []
    for lc in line_completions:
      score = 0
      for b in lc: score = score * 5 + score_dict[b]
      score_list.append(score)

    score_list.sort()

  return score_list[math.floor(len(score_list)/2)]

if __name__ == '__main__':
  input_array = load_input("../input.txt")
  # input_array = load_input("../test-input1.txt")

  # part 1 solution
  pt1_result = solve_part1(input_array)
  print("Part 1: {}".format(pt1_result))

  # part 2 solution
  pt2_result = solve_part2(input_array)
  print("Part 2: {}".format(pt2_result))
