import os
import requests
from dotenv import load_dotenv

load_dotenv()


def currency_tool(from_currency: str, to_currency: str, amount: float = 1):
    base_url = os.getenv("EXCHANGE_API_URL")
    api_key = os.getenv("EXCHANGE_API_KEY")

    params = {
        "apikey": api_key,
        "base": from_currency
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    rate = data.get("rates", {}).get(to_currency)

    if rate:
        return f"{amount} {from_currency} = {amount * rate} {to_currency}"
    return "Currency not found"