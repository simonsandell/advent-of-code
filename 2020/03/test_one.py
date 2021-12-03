import one


def test_check_tree():
    assert one.check_if_pos_tree(3, 0)
    assert not one.check_if_pos_tree(0, 0)
