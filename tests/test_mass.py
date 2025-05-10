from unit_converter.mass import convert_mass

def test_kg_to_g():
    assert convert_mass(1, 'kg', 'g') == 1000.0


def test_lb_to_kg():
    result = convert_mass(2.20462, 'lb', 'kg')
    assert round(result, 2) == 1.0
