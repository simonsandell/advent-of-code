import two


def test_contigous():
    assert two.count_contigous_ones([1,1,1,3,1,1,3,1,3,3,3,]) == {1:1, 2:1, 3:1}
    assert two.count_contigous_ones([3,1,1,1,3,1,1,3,1,3,3,3,]) == {1:1, 2:1, 3:1}
