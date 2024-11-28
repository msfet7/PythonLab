import math

class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __abs__(self):
        return math.sqrt(self.real**2 + self.imag**2)

    def __str__(self):
        return f"{self.real} + {self.imag}j"

# Przykład użycia
if __name__ == "__main__":
    a = Complex(1.0, 2.5)
    b = Complex(2.3, 3.0)
    c = a + b
    d = a - b
    print(f"{a} + {b} = {c}")
    print(f"{a} - {b} = {d}")
