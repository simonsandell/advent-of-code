import one


def test_find_values_that_sum():
    assert one.find_values_that_sum([1, 2, 3, 4, 5], 9) == (4, 5)
