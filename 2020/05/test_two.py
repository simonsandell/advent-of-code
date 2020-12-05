import two


def test_midpoint():
    assert two.get_midpoints(1,10) == (5,6)
    assert two.get_midpoints(0,127) == (63,64)
    assert two.get_midpoints(0,0) == (0,0)
    assert two.get_midpoints(0,1) == (0,1)
    assert two.get_midpoints(15,16) == (15,16)

def test_find_seat():
    assert two.find_seat('FBFBBFFRLR') == (44,5)

def test_seatid():
    assert two.get_seatid(44,5) == 357

def test_inv():
    assert two.get_seatid(*two.get_rowcol(367)) == 367

