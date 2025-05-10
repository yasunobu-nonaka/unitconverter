from unit_converter.length import convert_length

def test_cm_to_m():
    assert convert_length(100, 'cm', 'm') == 1.0

def test_inch_to_cm():
    assert round(convert_length(1, 'inch', 'cm'), 2) == 2.54