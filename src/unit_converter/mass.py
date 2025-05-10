mass_units = {
    'g': 1.0,
    'kg': 1000.0,
    'mg': 0.001,
    'ton': 1_000_000.0,
    'lb': 453.592,
    'oz': 28.3495,
}

def convert_mass(value: float, from_unit: str, to_unit: str) -> float:
    if from_unit not in mass_units or to_unit not in mass_units:
        raise ValueError(f"Unsupported unit: {from_unit} or {to_unit}")
    return ValueError(f"Unsupported unit: {from_unit} or {to_unit}")
