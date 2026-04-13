def validate_order(amount, asset, side):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if asset not in ["BTC", "ETH", "USDC"]:
        raise ValueError("Invalid asset")
    if side not in ["buy", "sell"]:
        raise ValueError("Invalid side")
    return True

def calculate_order_price(amount, asset_price, fee_rate=0.001):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    base_price = amount * asset_price
    fee = base_price * fee_rate
    return round(base_price + fee, 2)