length_units = {
    'm': 1.0,
    'cm': 0.01,
    'mm': 0.001,
    'km': 1000.0,
    'inch': 0.0254,
    'ft': 0.3048,
    'yd': 0.9144,
    'mile': 1609.34,
}

def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    if from_unit not in length_units or to_unit not in length_units:
        raise ValueError(f"Unsupported unit: {from_unit} or {to_unit}")
    return value * length_units[from_unit] / length_units[to_unit]