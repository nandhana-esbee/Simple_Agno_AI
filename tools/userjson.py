import json
import os

def save_user_data(name: str, age: int, account_type: str, bank_name: str, place: str):
    
    data = {
        "name": name,
        "age": age,
        "account_type": account_type,
        "bank_name": bank_name,
        "place": place
    }

    file_path = "data/users.json"

    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            existing = json.load(f)
    else:
        existing = []

    existing.append(data)

    with open(file_path, "w") as f:
        json.dump(existing, f, indent=4)

    return "✅ Bank account created successfully!"