import two


def test_extract_paranthesis():
    assert two.extract_paranthesis('(123(123)123)') == '123(123)123'
    assert two.extract_paranthesis('(2 + 6 * 8) * 3') == '2 + 6 * 8'

def test_evaluate():
    assert two.evaluate_expression('1 + 2') == '3'
    assert two.evaluate_expression('(2 + 6 * 8) * 3') == '192'
    assert two.evaluate_expression('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == '23340'
