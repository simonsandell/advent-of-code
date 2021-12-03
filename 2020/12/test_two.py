import two

two.pos = [0, 0]
two.waypoint = [2, 5]


def test_rotate_clockwise():
    two.rotate_clockwise()
    two.rotate_clockwise()
    assert two.waypoint != [2, 5]
    assert two.waypoint == [-2, -5]
    two.rotate_anticlock()
    two.rotate_anticlock()
    assert two.waypoint == [2, 5]
    assert two.waypoint != [-2, -5]
