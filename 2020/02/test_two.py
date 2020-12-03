import two

def test_parse():
    assert two.parse_input('14-15 v: vdvvvvvsvvvvvfpv') == (14,15,'v', 'vdvvvvvsvvvvvfpv')

def test_check():
    assert not two.check_rule(3,4,'b','lkaefaliewjfalwifbbb') 
    assert not two.check_rule(3,4,'b','lkaefaliewjfalwifbbbbb') 
    assert not two.check_rule(3,4, 'b', 'bbbbbbbbbb')
    assert not two.check_rule(3,4, 'b', 'aabbaaaaaa')
    assert two.check_rule(3,4, 'b', 'aaabaaaaaa')
    assert two.check_rule(3,4, 'b', 'aabaaaaaaa')
