def to_kelvin(value: float, from_unit: str) -> float:
    if from_unit == 'C':
        return value + 273.15
    elif from_unit == 'F':
        return (value - 32) * 5 / 9 + 273.15
    elif from_unit == 'K':
        return value
    else:
        raise ValueError(f"Unsupported temperature unit: {from_unit}")
    
def from_kelvin(kelvin: float, to_unit: str) -> float:
    if to_unit == 'C':
        return kelvin - 273.15
    elif to_unit == 'F':
        return (kelvin - 273.15) * 9 / 5 + 32
    elif to_unit == 'K':
        return kelvin
    else:
        raise ValueError(f"Unsupported temperature unit: {to_unit}")
    
def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    kelvin = to_kelvin(value, from_unit)
    return from_kelvin(kelvin, to_unit)

