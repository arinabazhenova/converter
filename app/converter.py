import requests

def get_price(coin_id: str) -> float:
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    data = requests.get(url).json()
    return data.get(coin_id, {}).get("usd", 0.0)

def convert(from_coin: str, to_coin: str, amount: float) -> float:
    from_price = get_price(from_coin)
    to_price = get_price(to_coin)
    if to_price == 0:
        raise ValueError(f"Cannot get price for {to_coin}")
    return amount * from_price / to_price
