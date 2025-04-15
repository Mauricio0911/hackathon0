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
        raise ValueError("Invalid character or syntax")

def calculate(expression: str):
    expression = expression.strip()
    if not expression:
        raise ValueError("Empty input")
    # Solo se permiten dígitos, punto, el operador / y espacios.
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
def calculate(expression: str):
    expression = expression.strip()
    if not expression:
        raise ValueError("Empty input")
    # Solo se permiten dígitos, punto, el signo - y espacios.
    allowed_chars = "0123456789.- "
    for char in expression:
        if char not in allowed_chars:
            raise ValueError("Invalid character in expression")
    try:
        # Se asume que la expresión contiene únicamente restas.
        parts = expression.split('-')
        if parts[0] == "":
            # Si la expresión inicia con "-" se interpreta el primer número negativo.
            if len(parts) < 2 or parts[1].strip() == "":
                raise SyntaxError("Invalid syntax")
            result = -float(parts[1].strip())
            parts = parts[2:]
        else:
            result = float(parts[0].strip())
            parts = parts[1:]
        for part in parts:
            part = part.strip()
            if part == "":
                raise SyntaxError("Invalid syntax")
            result -= float(part)
        return int(result) if result.is_integer() else result
    except ValueError:
        raise ValueError("Invalid character or syntax")