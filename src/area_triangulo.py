import math

def area_triangulo(a, b, c):
    # Semiperímetro
    s = (a + b + c) / 2
    # Área utilizando la fórmula de Herón
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
