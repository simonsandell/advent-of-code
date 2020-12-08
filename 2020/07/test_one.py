import one

inp = 'striped orange bags contain 1 vibrant green bag, 5 plaid yellow bags, 1 drab magenta bag.'

def test_parse():
    assert one.parse_content('1 vibrant green bag, 5 plaid yellow bags, 1 drab magenta bag.') == {'vibrant green', 'plaid yellow', 'drab magenta'}
    assert one.parse_input(inp) == {'striped orange': {'vibrant green', 'plaid yellow', 'drab magenta'}}

