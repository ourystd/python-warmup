""" 
Implementation of complex numbers in Python 3
in order to practice OOP
"""


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(
            self.real * other.real - self.imaginary * other.imaginary,
            self.real * other.imaginary + self.imaginary * other.real,
        )

    def __truediv__(self, other):
        return ComplexNumber(
            (self.real * other.real + self.imaginary * other.imaginary)
            / (other.real * other.real + other.imaginary * other.imaginary),
            (self.imaginary * other.real - self.real * other.imaginary)
            / (other.real * other.real + other.imaginary * other.imaginary),
        )

    def __abs__(self):
        return (self.real * self.real + self.imaginary * self.imaginary) ** 0.5

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __ne__(self, other):
        return self.real != other.real or self.imaginary != other.imaginary

    def __lt__(self, other):
        return self.real < other.real and self.imaginary < other.imaginary

    def __le__(self, other):
        return self.real <= other.real and self.imaginary <= other.imaginary

    def __gt__(self, other):
        return self.real > other.real and self.imaginary > other.imaginary

    def __ge__(self, other):
        return self.real >= other.real and self.imaginary >= other.imaginary

    def __bool__(self):
        return self.real != 0 or self.imaginary != 0

    def __invert__(self):
        return ComplexNumber(self.real, -self.imaginary)

    def __complex__(self):
        return self.real, self.imaginary


if __name__ == "__main__":
    pass
