import one

def test_get_summable():
    assert one.get_summable([1,2,3]) == {3, 4, 5}
    assert 30 in one.get_summable([ 17, 14, 2, 35, 39, 31, 5, 25, 1, 29, 40, 48, 9, 37, 21, 7, 41, 8, 15, 28, 47, 13, 16, 50, 45])
