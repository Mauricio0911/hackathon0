def calculate(expression: str):
    expression = expression.strip()
    if not expression:
        raise ValueError("Empty input")
    allowed_chars = "0123456789./ "
    for char in expression:
        if char not in allowed_chars:
            raise ValueError("Invalid character in expression")
    try:
        parts = expression.split('/')
        result = float(parts[0].strip())
        for part in parts[1:]:
            part = part.strip()
            if part == "":
                raise SyntaxError("Invalid syntax")
            divisor = float(part)
            if divisor == 0:
                raise ZeroDivisionError("Division by zero")
            result /= divisor
        return int(result) if result.is_integer() else result
    except ValueError:
        raise ValueError("Invalid character or syntax")
