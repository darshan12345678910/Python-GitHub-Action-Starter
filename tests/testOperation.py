from src.storyA import add,sub

def test_add():
    assert add(2,4)==6
    assert add(6,6)==12
    assert add(6,9)==15
def test_sub():
    assert sub(6,4)==2
    assert sub(8,2)==4
    assert sub(1,3)==-2
        