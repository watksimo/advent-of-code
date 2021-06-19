import math
 
def get_code_value(input):
    min_val = 0
    max_val = 2**len(input) - 1
 
    for char in input:
        mid_diff_val = (max_val - min_val) / 2
        if char in ['F', 'L']:  # Lower half
            max_val = math.floor(max_val - mid_diff_val)
        if  char in ['B', 'R']:  # Upper half
            min_val = math.ceil(max_val - mid_diff_val)
   
    if min_val == max_val:
        return min_val
   
    return -1   # Incomplete
   
def get_seat_id(row, column):
    return row * 8 + column
   
def separate_code(input):
    l_pos = input.find('L')
    r_pos = input.find('R')
    col_start = r_pos if (l_pos < 0 or (r_pos < l_pos and r_pos > 0)) else l_pos
    return (input[:col_start], input[col_start:])

def get_seat_from_code(input_code):
    row_code, col_code = separate_code(input_code)
    row_num = get_code_value(row_code)
    col_num = get_code_value(col_code)
    seat_id = get_seat_id(row_num, col_num)
    if seat_id == 3264: print(row_code, row_num, col_num, seat_id)
    return seat_id
   
def get_seats_from_code_list(input_code_list):
    return [get_seat_from_code(input_code) for input_code in input_code_list]

def get_seats_list(input_filename):
    f = open(input_filename, "r")
    seat_code_list = [line.strip() for line in f.readlines()]
    return get_seats_from_code_list(seat_code_list)
   
def find_missing_seat(seat_list):
    seat_list.sort()
    for idx, seat in enumerate(seat_list):
        if idx > 0 and seat - seat_list[idx-1] != 1: return seat - 1
 
if __name__ == "__main__":
    test_input = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
    part_one_seat_list = get_seats_list("../real-input.txt")
    part_one_max_seat = max(part_one_seat_list)
    part_two_missing_seat = find_missing_seat(part_one_seat_list)
    print("Part 1: The highest seat ID is {}.".format(part_one_max_seat))
    print("Part 2: The missing seat ID is {}.".format(part_two_missing_seat))
