from seatings_two import Seatings

input = '...LLLLL\nLLLLLLLL\n........\nLLLLLLLL\n'

def test_get_adj():
    s = Seatings()
    s.parse_input(input)
    assert s.get_adjacent((0,0)) == {(0,3), (1,1), (1,0)}

