import two


def test_parse():
    assert two.parse_mask("mask = 100110010000101110000001000010001101") == (
        0b100110010000101110000001000010001101,
        set(),
    )
    assert two.parse_mask("mask = 1001100100001011100000010000100X11X1") == (
        0b100110010000101110000001000010001101,
        {5, 2},
    )


def test_mask_addr():
    assert two.mask_addr(0b0101, 0b1010, {}) == {0b1111}
    assert two.mask_addr(0b0101, 0b1010, {1}) == {0b1111, 0b1110}

    assert two.mask_addr(0b101010, 0b010010, {1, 6}) == {26, 27, 58, 59}


def test_set():
    assert two.set_one(32, 1) == 33
    assert two.set_zero(33, 1) == 32


# def test_whole():
#    assert sum(list(two.load_program("""mask = 000000000000000000000000000000X1001X
#    mem[42] = 100
#    mask = 00000000000000000000000000000000X0XX
#    mem[26] = 1"""))) == 208
