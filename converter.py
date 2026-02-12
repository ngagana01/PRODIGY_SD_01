def celsius_to_others(c):
    f = (c * 9/5) + 32
    k = c + 273.15
    return f, k


def fahrenheit_to_others(f):
    c = (f - 32) * 5/9
    k = c + 273.15
    return c, k


def kelvin_to_others(k):
    c = k - 273.15
    f = (c * 9/5) + 32
    return c, f


def convert(value, unit):
    unit = unit.lower()

    if unit == "celsius":
        f, k = celsius_to_others(value)
        return {"Fahrenheit": f, "Kelvin": k}

    elif unit == "fahrenheit":
        c, k = fahrenheit_to_others(value)
        return {"Celsius": c, "Kelvin": k}

    elif unit == "kelvin":
        c, f = kelvin_to_others(value)
        return {"Celsius": c, "Fahrenheit": f}

    else:
        return None
