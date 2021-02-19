import day_5

def test_separate_code_1():
    test1 = day_5.separate_code("BFFFBBFRRR")
    assert test1[0] == "BFFFBBF" and test1[1] == "RRR"

def test_separate_code_2():
    test2 = day_5.separate_code("FFFBBBFRRR")
    assert test2[0] == "FFFBBBF" and test2[1] == "RRR"

def test_separate_code_3():
    test3 = day_5.separate_code("BBFFBBFRLL")
    assert test3[0] == "BBFFBBF" and test3[1] == "RLL"

def test_get_seat_from_code():
    test1 = day_5.get_seat_from_code("BFFFBBFRRR")
    assert test1 == 567
    test2 = day_5.get_seat_from_code("FFFBBBFRRR")
    assert test2 == 119
    test3 = day_5.get_seat_from_code("BBFFBBFRLL")
    assert test3 == 820

def test_get_seats_from_code_list():
    code_list = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
    seat_list = day_5.get_seats_from_code_list(code_list)
    assert seat_list == [567, 119, 820]

def test_find_missing_seat():
    seat_list = [2, 4, 1, 5]    # Missing 3
    assert 3 == day_5.find_missing_seat(seat_list)