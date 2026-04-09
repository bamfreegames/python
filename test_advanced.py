import pytest

def func(x):
    if x <= 0:
        raise ValueError("x needs to be larger than zero")

def test_try():
    with pytest.raises(ValueError):func(-1)

def f():
    raise ExceptionGroup("", [IndexError()])


@pytest.mark.xfail(raises=pytest.RaisesGroup(IndexError))
def test_f():
    f()

def test_set_comparison():
        set1 = set("1308")
        set2 = set("8031")
        assert set1 == set2

def foo(x,y=1):
     return x + y

@pytest.mark.parametrize(
    ["a", "b", "result"],
    [
        [1, 0, 1],
        [2, 3, 5],
        [5, 3, 8],
    ],
)

def test_foo(a, b, result):
    assert foo(a, b) == result

    # Arrange
@pytest.fixture
def first_entry():
    return "a"


# Arrange
@pytest.fixture
def order(first_entry):
    return [first_entry]


def test_string(order):
    # Act
    order.append("b")

    # Assert
    assert order == ["a", "b"]