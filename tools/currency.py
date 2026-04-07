import os
import requests
from dotenv import load_dotenv

load_dotenv()

def currency_tool(from_currency: str, to_currency: str, amount: float = 1):
    url = f"{os.getenv('EXCHANGE_API_URL')}/{from_currency}"
    
    data = requests.get(url).json()
    rate = data["rates"].get(to_currency)

    if rate:
        return f"{amount} {from_currency} = {amount * rate} {to_currency}"
    return "Currency not found"