import os
import json
import uuid

def save_user_data(
    name: str,
    bank_name: str,
    account_type: str,
    state: str,
    operation: str = "save_account"
):
    """
    Save user bank account details after confirmation.

    Returns:
        dict with status and reference_id
    """

    if operation != "save_account":
        return {
            "status": "error",
            "message": "Invalid operation"
        }

    try:
        file_path = "data/users.json"

        # ✅ ensure folder exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # ✅ generate reference ID
        reference_id = f"ACC-{uuid.uuid4().hex[:8].upper()}"

        data = {
            "reference_id": reference_id,
            "name": name,
            "bank_name": bank_name,
            "account_type": account_type,
            "state": state
        }

        # ✅ load existing safely
        if os.path.exists(file_path):
            try:
                with open(file_path, "r") as f:
                    existing = json.load(f)
                    if not isinstance(existing, list):
                        existing = []
            except:
                existing = []
        else:
            existing = []

        # ✅ append new record
        existing.append(data)

        # ✅ save
        with open(file_path, "w") as f:
            json.dump(existing, f, indent=4)

        return {
            "status": "success",
            "reference_id": reference_id,
            "message": "Bank account created successfully"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
    

