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
    def area_pentagono_regular(self, lado, apotema):
        if apotema <=0 or lado <=0:
            return 0
        return (5*lado*apotema)/2

    # Hexágono regular
    def area_hexagono_regular(self,lado,apotema):
        if apotema == 0 or lado == 0:
            return 0
        perimetro = 6*lado
        return (perimetro*apotema)/2

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

    def ecuacion_recta(self, x1, y1, x2, y2):
        # Coeficientes
        A = y2 - y1
        B = -(x2 - x1)
        C = (x2 - x1) * y1 - (y2 - y1) * x1

        # Normalización para que siempre dé el mismo resultado
        if B < 0 or (B == 0 and A < 0):
            A, B, C = -A, -B, -C

        return (A, B, C)

    # Polígono regular
    def area_poligono_regular(self, n_lados, lado, apotema):
        if n_lados < 3 or lado <= 0 or apotema <= 0:
            return 0
        perimetro = n_lados * lado
        return (perimetro * apotema) / 2

    def perimetro_poligono_regular(self, n_lados, lado):
        if n_lados < 3 or lado <= 0:
            return 0
        return n_lados * lado

