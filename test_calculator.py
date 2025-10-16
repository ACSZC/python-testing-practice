from calculator import add,substract

def test_add():
	assert add(2,3)==5
	assert add(-1,1)==0

def test_substract():
    assert substract(4,2)==2
    assert add(substract(4,2),3)==5

