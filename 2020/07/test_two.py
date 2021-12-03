import two

inp = "striped orange bags contain 1 vibrant green bag, 5 plaid yellow bags, 1 drab magenta bag."


def test_parse():
    assert two.parse_content(
        "1 vibrant green bag, 5 plaid yellow bags, 1 drab magenta bag."
    ) == {(1, "vibrant green"), (5, "plaid yellow"), (1, "drab magenta")}
    assert two.parse_input(inp) == {
        "striped orange": {
            (1, "vibrant green"),
            (5, "plaid yellow"),
            (1, "drab magenta"),
        }
    }
