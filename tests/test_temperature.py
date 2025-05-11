from unit_converter.temperature import convert_temperature

def test_c_to_f():
    assert round(convert_temperature(0, 'C', 'F'), 2) == 32.00

def test_f_to_c():
    assert round(convert_temperature(212, 'F', 'C'), 2) == 100.00

def test_c_to_k():
    assert round(convert_temperature(100, 'C', 'K'), 2) == 373.15

def test_k_to_f():
    assert round(convert_temperature(273.15, 'K', 'F'), 2) == 32.00
