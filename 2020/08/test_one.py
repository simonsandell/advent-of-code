import one


def test_parse():
    assert one.parse_int('+1234') == 1234
    assert one.parse_int('-1234') == -1234

    assert one.parse_input('acc +45\nnop +631\nacc +12\n') == [
            ('acc', 45),
            ('nop', 631),
            ('acc', 12)
            ]
