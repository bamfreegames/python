import pytest

class TestClass:

    def hi(self):
        pass
        
    value = 0

    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")

    def test_three(self):
        v = TestClass()
        assert hasattr(v,"hi")

    def test_four(self):
        self.value = 1
        assert self.value == 1

    def test_five(self):
        assert self.value == 1

    def test_sum(self):
        assert (0.1 + 0.2) == pytest.approx(0.3)