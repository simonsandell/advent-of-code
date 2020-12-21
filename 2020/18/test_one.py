import one


def test_extract_paranthesis():
    assert one.extract_paranthesis('(123(123)123)') == '123(123)123'
    assert one.extract_paranthesis('(2 + 6 * 8) * 3') == '2 + 6 * 8'

def test_evaluate():
    assert one.evaluate_expression('1 + 2') == '3'
    assert one.evaluate_expression('(2 + 6 * 8) * 3') == '192'
    assert one.evaluate_expression('(2 + (6 * 8)) * ((3 + (2 + 1) * 3) * 3)') == '2700'
