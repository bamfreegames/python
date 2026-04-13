import pytest
from utils.helpers import validate_order, calculate_order_price

class TestOrderValidation:

    @pytest.mark.unit
    @pytest.mark.smoke
    def test_valid_order_passes(self, valid_order):
        result = validate_order(**valid_order)
        assert result == True

    @pytest.mark.unit
    @pytest.mark.parametrize("amount, asset, side, error_msg", [
        (0,    "BTC",  "buy",  "Amount must be positive"),
        (-1,   "BTC",  "buy",  "Amount must be positive"),
        (0.5,  "DOGE", "buy",  "Invalid asset"),
        (0.5,  "BTC",  "hold", "Invalid side"),
    ])
    def test_invalid_orders_raise_error(self, amount, asset, side, error_msg):
        with pytest.raises(ValueError, match=error_msg):
            validate_order(amount, asset, side)

class TestPriceCalculation:

    @pytest.mark.unit
    @pytest.mark.parametrize("amount, price, fee, expected", [
        (1.0,  50000, 0.001, 50050.0),
        (0.5,  50000, 0.001, 25025.0),
        (2.0,  30000, 0.002, 60120.0),
    ])
    def test_price_calculation(self, amount, price, fee, expected):
        result = calculate_order_price(amount, price, fee)
        assert result == expected

    @pytest.mark.unit
    def test_negative_amount_raises_error(self):
        with pytest.raises(ValueError, match="Amount must be positive"):
            calculate_order_price(-1, 50000)