import os
import requests
from dotenv import load_dotenv

load_dotenv()


def currency_tool(from_currency: str, to_currency: str) -> float:
    """
    Get exchange rate from one currency to another.

    Args:
        from_currency: Source currency (e.g., 'MYR')
        to_currency: Target currency (e.g., 'INR')

    Returns:
        Exchange rate as float (e.g., 23.21) or None if failed
    """

    try:
        base_url = os.getenv("EXCHANGE_API_URL")
        api_key = os.getenv("EXCHANGE_API_KEY")

        if not base_url or not api_key:
            return None

        from_currency = from_currency.upper().strip()
        to_currency = to_currency.upper().strip()

        params = {
            "apikey": api_key,
            "base": from_currency
        }

        response = requests.get(base_url, params=params, timeout=10)

        if response.status_code != 200:
            return None

        try:
            data = response.json()
        except:
            return None

        rate = data.get("rates", {}).get(to_currency)

        if rate:
            return float(rate)

        return None

    except Exception:
        return None