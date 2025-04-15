def calculate(expression: str):
    expression = expression.strip()
    if not expression:
        raise ValueError("Empty input")
    # Solo se permiten dígitos, punto, el signo +, el signo - (como parte de números negativos) y espacios.
    allowed_chars = "0123456789.+- "
    for char in expression:
        if char not in allowed_chars:
            raise ValueError("Invalid character in expression")
    try:
        # Separa la cadena usando el operador de suma.
        parts = expression.split('+')
        total = 0
        for part in parts:
            part = part.strip()
            if part == "":
                # Esto sucede por un operador final o dobles operadores seguidos.
                raise SyntaxError("Invalid syntax")
            total += float(part)
        # Se regresa número entero si no tiene parte decimal
        return int(total) if total.is_integer() else total
    except ValueError:
        raise ValueError("Invalid character or syntax")
