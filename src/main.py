def calculate(expression: str):
    expression = expression.strip()
    if not expression:
        raise ValueError("Empty input")
    # Solo se permiten dígitos, punto, el operador * y espacios.
    allowed_chars = "0123456789.* "
    for char in expression:
        if char not in allowed_chars:
            raise ValueError("Invalid character in expression")
    try:
        # Se separa la cadena usando el operador de multiplicación.
        parts = expression.split('*')
        result = 1.0
        for part in parts:
            part = part.strip()
            if part == "":
                raise SyntaxError("Invalid syntax")
            result *= float(part)
        return int(result) if result.is_integer() else result
    except ValueError:
        raise ValueError("Invalid character or syntax")
