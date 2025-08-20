import math

class Geometria:

    # Rectángulo
    def area_rectangulo(self, base, altura):
        return base * altura

    def perimetro_rectangulo(self, base, altura):
        return 2 * (base + altura)

    # Círculo
    def area_circulo(self, radio):
        return math.pi * radio**2

    def perimetro_circulo(self, radio):
        return 2 * math.pi * radio

    # Triángulo
    def area_triangulo(self, base, altura):
        return (base * altura) / 2

    def perimetro_triangulo(self, lado1, lado2, lado3):
        return lado1 + lado2 + lado3

    def es_triangulo_valido(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            return False
        return (a + b > c) and (a + c > b) and (b + c > a)

    # Trapecio
    def area_trapecio(self, base_mayor, base_menor, altura):
        return ((base_mayor + base_menor) * altura) / 2

    # Rombo
    def area_rombo(self, d1, d2):
        return (d1 * d2) / 2

    # Pentágono regular
    def area_pentagono_regular(self, perimetro, apotema):
        return (perimetro * apotema) / 2

    def perimetro_pentagono_regular(self, lado):
        return 5 * lado

    # Hexágono regular
    def area_hexagono_regular(self, perimetro, apotema):
        return (perimetro * apotema) / 2

    def perimetro_hexagono_regular(self, lado):
        return 6 * lado

    # Cubo
    def volumen_cubo(self, lado):
        return lado**3

    def area_superficie_cubo(self, lado):
        return 6 * (lado**2)

    # Esfera
    def volumen_esfera(self, radio):
        return (4/3) * math.pi * (radio**3)

    def area_superficie_esfera(self, radio):
        return 4 * math.pi * (radio**2)

    # Cilindro
    def volumen_cilindro(self, radio, altura):
        return math.pi * (radio**2) * altura

    def area_superficie_cilindro(self, radio, altura):
        return 2 * math.pi * radio * (radio + altura)

    # Distancia entre puntos
    def distancia_entre_puntos(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # Punto medio
    def punto_medio(self, x1, y1, x2, y2):
        return ((x1 + x2) / 2, (y1 + y2) / 2)

    # Pendiente de una recta
    def pendiente_recta(self, x1, y1, x2, y2):
        return (y2 - y1) / (x2 - x1)

    # Ecuación de la recta en forma Ax + By + C = 0
    def ecuacion_recta(self, x1, y1, x2, y2):
        A = y1 - y2
        B = x2 - x1
        C = (x1 * y2) - (x2 * y1)
        return (A, B, C)

    # Polígono regular
    def area_poligono_regular(self, n, perimetro, apotema):
        return (perimetro * apotema) / 2

    def perimetro_poligono_regular(self, n, lado):
        return n * lado
