from day_20 import *
import pytest

@pytest.fixture
def global_var():
    pytest.original_rows = [
        '..##.#..#.',
        '##..#.....',
        '#...##..#.',
        '####.#...#',
        '##.##.###.',
        '##...#.###',
        '.#.#.#..##',
        '..#....#..',
        '###...#.#.',
        '..###..###'
        ]

    pytest.original_rows_listed = [list(row) for row in pytest.original_rows]
    pytest.test_tile = Tile(2311, pytest.original_rows)

def test_static_tile_creation():
    test_tile = Tile(2311, ['..##.#..#.', '##..#.....', '#...##..#.', '####.#...#', '##.##.###.', '##...#.###', '.#.#.#..##', '..#....#..', '###...#.#.', '..###..###'])
    assert test_tile.tile_no == 2311
    assert test_tile.puzzle_rows[0] == list('..##.#..#.')
    assert test_tile.puzzle_rows[1] == list('##..#.....')

def test_tile_reorient(global_var):
    test_tile = pytest.test_tile
    original_rows_listed = pytest.original_rows_listed

    test_tile.reorient_tile(TileOrientation.ORIGINAL)
    test_tile.pretty_print()
    assert test_tile.puzzle_rows == original_rows_listed

    test_tile.reorient_tile(TileOrientation.CLOCKWISE_1)
    test_tile.pretty_print()
    cw1_top_row    = list('.#..#####.')
    cw1_bottom_row = list('#..##.#...')
    assert test_tile.puzzle_rows[0] == cw1_top_row
    assert test_tile.puzzle_rows[-1] == cw1_bottom_row
    assert test_tile.orientation == TileOrientation.CLOCKWISE_1

    test_tile.reorient_tile(TileOrientation.ORIGINAL)
    assert test_tile.puzzle_rows == original_rows_listed
    assert test_tile.orientation == TileOrientation.ORIGINAL

    test_tile.reorient_tile(TileOrientation.CLOCKWISE_2)
    test_tile.pretty_print()
    cw2_top_row = list('###..###..')
    cw2_bottom_row = list('.#..#.##..')
    assert test_tile.puzzle_rows[0] == cw2_top_row
    assert test_tile.puzzle_rows[-1] == cw2_bottom_row
    assert test_tile.orientation == TileOrientation.CLOCKWISE_2

    test_tile.reorient_tile(TileOrientation.CLOCKWISE_3)
    test_tile.pretty_print()
    cw3_top_row    = list('...#.##..#')
    cw3_bottom_row = list('.#####..#.')
    assert test_tile.puzzle_rows[0] == cw3_top_row
    assert test_tile.puzzle_rows[-1] == cw3_bottom_row
    assert test_tile.orientation == TileOrientation.CLOCKWISE_3

    test_tile.reorient_tile(TileOrientation.HORIZ_FLIP)
    test_tile.pretty_print()
    assert test_tile.puzzle_rows[0] == original_rows_listed[-1]
    assert test_tile.puzzle_rows[-1] == original_rows_listed[0]
    assert test_tile.orientation == TileOrientation.HORIZ_FLIP

    test_tile.reorient_tile(TileOrientation.VERT_FLIP)
    test_tile.pretty_print()
    vert_top_row = list('.#..#.##..')
    vert_bottom_row = list('###..###..')
    assert test_tile.puzzle_rows[0] == vert_top_row
    assert test_tile.puzzle_rows[-1] == vert_bottom_row
    assert test_tile.orientation == TileOrientation.VERT_FLIP

def test_get_tile_edges(global_var):
    test_tile = pytest.test_tile
    original_rows_listed = pytest.original_rows_listed

    tile_top = test_tile.get_tile_edge(TileEdge.TOP)
    assert tile_top == original_rows_listed[0]

    tile_bottom = test_tile.get_tile_edge(TileEdge.BOTTOM)
    assert tile_bottom == original_rows_listed[-1]

    tile_left = test_tile.get_tile_edge(TileEdge.LEFT)
    assert tile_left == list('.#####..#.')

    tile_right = test_tile.get_tile_edge(TileEdge.RIGHT)
    assert tile_right == list('...#.##..#')
