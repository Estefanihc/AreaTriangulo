
import pytest
from src.area_triangulo import area_triangulo

def test_area_triangulo():
    assert area_triangulo(3, 4, 5) == 6.0

def test_area_triangulo_equilatero():
    expected_area = 10.825317547305485
    calculated_area = area_triangulo(5, 5, 5)
    tolerance = 1e-6  # Tolerancia pequeña para comparaciones de punto flotante
    assert abs(expected_area - calculated_area) < tolerance

def test_area_triangulo_invalido():
    with pytest.raises(ValueError):
        area_triangulo(1, 2, 10)
