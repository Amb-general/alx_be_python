def safe_divide(numerator, denominator):
    try:
        # Convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Check for division by zero
        if den == 0:
            return "Error: Cannot divide by zero."

        # Perform division
        result = num / den
        return f"The result of the division is {result}"

    except ValueError:
        return "Error: Please enter numeric values only."

