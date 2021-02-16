class MapSolver:
    def __init__(self, input_filename, r_speed, d_speed, wrap_right = False, wrap_down = False):
        f = open(input_filename, "r")
        self.map_array = [line.strip() for line in f.readlines()]
        self.r_speed = r_speed
        self.d_speed = d_speed
        self.r_pos = 0
        self.d_pos = 0
        self.wrap_right = wrap_right
        self.wrap_down = wrap_down
 
    def get_tree(self):
        return self.map_array[self.d_pos][self.r_pos] == '#'
 
    def make_move(self):
        self.r_pos += self.r_speed
        if self.wrap_right:
            self.r_pos = self.r_pos % (len(self.map_array[0]))
            self.d_pos += self.d_speed
 
    def get_position(self):
        return (self.r_pos, self.d_pos)
 
    def at_bottom(self):
        return self.d_pos == len(self.map_array) - 1
 
    def past_top_bottom(self):
        if self.wrap_down:
            return False
        return 0 < self.d_pos > len(self.map_array) - 1
 
    def past_left_right(self):
        if self.wrap_right:
            return False
        return 0 < self.r_pos > len(self.map_array[0]) - 1
   
    def past_edges(self):
        return self.past_top_bottom() or self.past_left_right()
 
    def get_trees_to_bottom(self):
        tree_count = 0
        while not self.past_edges():
            # print(self.get_position())
            if self.get_tree():
                tree_count += 1
                # print("--Tree")
            self.make_move()
        return tree_count

def solve_part2(input_file):
    slope_list = [(1,1), (3,1), (5,1), (7,1), (1,2)]

    mult = 1
    for slope in slope_list:
        map_solve = MapSolver(input_file, slope[0], slope[1], wrap_right = True)
        mult *= map_solve.get_trees_to_bottom()

    return mult

if __name__ == '__main__':
    # input_file = "test-input.txt"
    input_file = "part1-input.txt"
    part1 = MapSolver(input_file, 3, 1, wrap_right = True)
    tree_count = part1.get_trees_to_bottom()
    print("Part 1: {} trees encountered.".format(tree_count))
    print("Part 2: {} solution.".format(solve_part2(input_file)))


