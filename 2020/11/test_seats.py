from seatings import Seatings

input = 'LLLLLLLL\nLLLLLLLL\nLLLLLLLL\n'

def test_get_adj():
    s = Seatings()
    s.parse_input(input)
    assert s.get_adjacent((0,0)) == { (0,1), (1,1), (1,0)}

