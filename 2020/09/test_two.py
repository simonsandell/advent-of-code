import two

def test_find_contigous():
    assert two.find_contigous([1,3,4,7,8,9,11], 20) == [5,6]
    assert two.find_contigous([1,3,4,7,8,9,11], 7) == [1,2]
    assert two.find_contigous([1,3,4,7,8,9,11], 24) == [3,4,5]
