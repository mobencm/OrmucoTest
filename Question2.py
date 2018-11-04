import pytest

def String_Compare(A,B):
    if not A or not B :
        raise AttributeError('Argument should not be empty')
    if (A > B) : return A + " greater than " + B
    if (A < B) : return A + " less than " + B
    if (A > B) : return A + " equal " + B

def test_EmptyString():

    with pytest.raises(AttributeError) as excinfo:
        String_Compare('', 'B')
    assert 'Argument should not be empty' in str(excinfo.value)


print(String_Compare('A b','Ab'))
assert String_Compare('A b','Ab') == "A b less than Ab"