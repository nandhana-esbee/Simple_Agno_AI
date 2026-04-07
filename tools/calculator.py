def calculator_tool(principal: float, rate: float, time: float):
    interest = (principal * rate * time) / 100
    return f"Interest = {interest}"