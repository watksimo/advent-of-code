from enum import Enum
import numpy as np

TileOrientation = Enum('TileOrientation', 'ORIGINAL CLOCKWISE_1 CLOCKWISE_2 CLOCKWISE_3 HORIZ_FLIP VERT_FLIP')
TileEdge = Enum('TileEdge', 'TOP RIGHT BOTTOM LEFT')

class Tile():
    def __init__(self, tile_no, puzzle_rows):
        self.tile_no = tile_no
        self.orientation = TileOrientation.ORIGINAL
        self.puzzle_rows = [list(row) for row in puzzle_rows]
        self.adj_tiles = {
            TileEdge.TOP: None,
            TileEdge.RIGHT: None,
            TileEdge.BOTTOM: None,
            TileEdge.LEFT: None
        }

    def reset_tile_orientation(self):
        opposite_map = {
            TileOrientation.ORIGINAL: None,
            TileOrientation.CLOCKWISE_1: TileOrientation.CLOCKWISE_3,
            TileOrientation.CLOCKWISE_2: TileOrientation.CLOCKWISE_2,
            TileOrientation.CLOCKWISE_3: TileOrientation.CLOCKWISE_1,
            TileOrientation.HORIZ_FLIP: TileOrientation.HORIZ_FLIP,
            TileOrientation.VERT_FLIP: TileOrientation.VERT_FLIP
        }
        old_orientation = self.orientation
        self.orientation = TileOrientation.ORIGINAL
        self.reorient_tile(opposite_map[old_orientation])

    def reorient_tile(self, new_orientation):
        if not new_orientation in TileOrientation: return

        new_rows = self.puzzle_rows
        if self.orientation != TileOrientation.ORIGINAL: self.reset_tile_orientation()
        
        self.orientation = new_orientation
        if new_orientation == TileOrientation.ORIGINAL:
            return
        if new_orientation == TileOrientation.CLOCKWISE_1:
            np_array = np.array(self.puzzle_rows)
            np_array = np.rot90(np_array, axes=(1,0))
            new_rows = np_array.tolist()
        if new_orientation == TileOrientation.CLOCKWISE_2:
            np_array = np.array(self.puzzle_rows)
            np_array = np.rot90(np_array, 2, axes=(1,0))
            new_rows = np_array.tolist()
        if new_orientation == TileOrientation.CLOCKWISE_3:
            np_array = np.array(self.puzzle_rows)
            np_array = np.rot90(np_array, 3, axes=(1,0))
            new_rows = np_array.tolist()
        if new_orientation == TileOrientation.HORIZ_FLIP:
            np_array = np.array(self.puzzle_rows)
            np_array = np.flipud(np_array)
            new_rows = np_array.tolist()
        if new_orientation == TileOrientation.VERT_FLIP:
            np_array = np.array(self.puzzle_rows)
            np_array = np.fliplr(np_array)
            new_rows = np_array.tolist()
        
        self.puzzle_rows = new_rows

    def get_tile_edge(self, tile_edge):
        if tile_edge == TileEdge.TOP:
            return self.puzzle_rows[0]
        if tile_edge == TileEdge.BOTTOM:
            return self.puzzle_rows[-1]
        if tile_edge == TileEdge.LEFT:
            return [row[0] for row in self.puzzle_rows]
        if tile_edge == TileEdge.RIGHT:
            return [row[-1] for row in self.puzzle_rows]

    def get_all_edges(self):
        return [
            [TileEdge.TOP, self.get_tile_edge(TileEdge.TOP)],
            [TileEdge.BOTTOM, self.get_tile_edge(TileEdge.BOTTOM)],
            [TileEdge.LEFT, self.get_tile_edge(TileEdge.LEFT)],
            [TileEdge.RIGHT, self.get_tile_edge(TileEdge.RIGHT)]
        ]

    def get_adj_ids(self):
        return [adj[0] for adj in self.adj_tiles.values() if adj is not None]

    def is_corner(self):
        return sum([1 for adj_tile in self.adj_tiles.values() if adj_tile is None]) == 2

    def pretty_print(self):
        for row in self.puzzle_rows:
            print(''.join(row))
        print("----")

def file_to_tiles(input_filename):
    tile_dict = {}
    f = open(input_filename, 'r')

    tile_no = 0
    row_array = []
    for line in f.readlines():
        line = line.strip()
        if line != "":
            if 'Tile' in line:
                tile_no = int(line.split(" ")[1][:-1])
            else:
                row_array.append(line)
        else:
            tile_dict[tile_no] = (Tile(tile_no, row_array))
            tile_no = 0
            row_array = []
    return tile_dict

def find_edge_match(tile_dict, tile_id):
    check_tile = tile_dict[tile_id]
    check_tile_edges = check_tile.get_all_edges()

    for tile in tile_dict.values():
        if tile.tile_no != tile_id:
            # for tile_orient in TileOrientation:
            #     tile.reorient_tile(tile_orient)
            for tile_edge in tile.get_all_edges():
                for check_tile_edge in check_tile_edges:
                        if (tile_edge[1] == check_tile_edge[1] or tile_edge[1].reverse() == check_tile_edge[1]) and tile.tile_no not in tile.get_adj_ids():
                            check_tile.adj_tiles[check_tile_edge[0]] = [tile.tile_no, tile.orientation, tile_edge[0]]


if __name__=="__main__":
    tile_dict = file_to_tiles("../test_input.txt")

    for tile in tile_dict.values():
        print(tile.tile_no)
        find_edge_match(tile_dict, tile.tile_no)
        print(tile.adj_tiles)
        print()
    
    corner_tile_ids = [tile.tile_no for tile in tile_dict.values() if tile.is_corner()]

    print(corner_tile_ids)
    print(np.prod(corner_tile_ids))



    

