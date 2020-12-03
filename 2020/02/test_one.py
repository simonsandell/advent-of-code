import one

def test_parse():
    assert one.parse_input('14-15 v: vdvvvvvsvvvvvfpv') == (14,15,'v', 'vdvvvvvsvvvvvfpv')

def test_check():
    assert one.check_rule(3,4,'b','lkaefaliewjfalwifbbb') 
    assert not one.check_rule(3,4,'b','lkaefaliewjfalwifbbbbb') 
    assert not one.check_rule(3,4,'b','') 
