import one


def test_midpoint():
    assert one.get_midpoints(1, 10) == (5, 6)
    assert one.get_midpoints(0, 127) == (63, 64)
    assert one.get_midpoints(0, 0) == (0, 0)
    assert one.get_midpoints(0, 1) == (0, 1)
    assert one.get_midpoints(15, 16) == (15, 16)


def test_find_seat():
    assert one.find_seat("FBFBBFFRLR") == (44, 5)


def test_seatid():
    assert one.get_seatid(44, 5) == 357
