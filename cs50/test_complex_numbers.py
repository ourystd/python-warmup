from complex_numbers import ComplexNumber


def test_display_complex_number():
    real, imaginary = 5, 1
    com = ComplexNumber(real, imaginary)
    assert com.__str__() == f"{real} + {imaginary}i"
