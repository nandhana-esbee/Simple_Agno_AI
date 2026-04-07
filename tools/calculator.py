# def calculator_tool(principal: float, rate: float, time: float):
#     interest = (principal * rate * time) / 100
#     return f"Interest = {interest}"

import re

def calculator_tool(query: str) -> str:
    q = query.lower().strip()

    try:
        # -------------------------
        # Percentage (e.g., 25% of 800)
        # -------------------------
        if "%" in q and "of" in q:
            parts = q.replace("%", "").split("of")
            percent = float(parts[0].strip())
            value = float(parts[1].strip())
            return str((percent / 100) * value)

        # -------------------------
        # Simple Interest
        # Format: si p r t
        # Example: si 10000 5 2
        # -------------------------
        if q.startswith("si"):
            _, p, r, t = q.split()
            p, r, t = float(p), float(r), float(t)
            si = (p * r * t) / 100
            return str(si)

        # -------------------------
        # Compound Interest
        # Format: ci p r t
        # Example: ci 10000 5 2
        # -------------------------
        if q.startswith("ci"):
            _, p, r, t = q.split()
            p, r, t = float(p), float(r), float(t)
            amount = p * (1 + r / 100) ** t
            return str(amount - p)

        # -------------------------
        # Basic arithmetic
        # -------------------------
        if re.match(r'^[0-9+\-*/(). ]+$', q):
            return str(eval(q))

        return "Invalid input"

    except:
        return "Error in calculation"