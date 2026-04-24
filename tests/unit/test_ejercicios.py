import pytest

def sum_numbers(a, b):
    return a + b

def test_sum_numbers_positives():
    assert sum_numbers(1,2) == 3

def test_sum_numbers_negativo():
    assert sum_numbers(-1,2) == 1

def test_sum_numbers_cero():
    assert sum_numbers(0,2) == 2

def validate_order_amount(amount):
    #"""Valida que el amount de una orden sea válido."""
    if amount is None:
        raise ValueError("Amount cannot be None")
    if not isinstance(amount, (int, float)):
        raise TypeError("Amount must be a number")
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > 1000000:
        raise ValueError("Amount exceeds maximum allowed")
    return True

def test_amount_null():
    with pytest.raises(ValueError, match="Amount cannot be None"):validate_order_amount(None)

def test_amount_format():
    with pytest.raises(TypeError, match="Amount must be a number"):validate_order_amount("4")

def test_amount_positive():
    with pytest.raises(ValueError, match="Amount must be positive"):validate_order_amount(-1)

def test_amount_maximum():
    with pytest.raises(ValueError, match="Amount exceeds maximum allowed"):validate_order_amount(20000000)

def test_amount_ok():
    assert validate_order_amount(5)




