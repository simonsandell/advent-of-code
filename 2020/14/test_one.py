import one


def test_parse_mask():
    assert one.parse_mask("mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") == (
        0,
        2 ** 36 - 1,
    )
    assert one.parse_mask("mask = 111111111111111111111111111111111111") == (
        0b111111111111111111111111111111111111,
        2 ** 36 - 1,
    )
    assert one.parse_mask("mask = 000000000000000000000000000000000000") == (0, 0)


def test_parse_mem():
    assert one.parse_mem("mem[9150] = 255662") == [9150, 255662]


def test_mask_value():
    assert one.mask_value(0b111, 0, 0b000) == 0b000
    assert one.mask_value(0b010, 0b101, 0b101) == 0b101
    assert one.mask_value(0b000, 0b111, 0b111) == 0b111


def test_whole():
    inp = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
    mem[8] = 11
    mem[7] = 101
    mem[8] = 0"""
    assert one.load_program(inp) == {8: 64, 7: 101}
