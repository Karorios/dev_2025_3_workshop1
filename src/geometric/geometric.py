class Geometria:
    """
    Class with geometric exercises.
    Include basic and funny operations in 2D and 3D.
    """

    def area_rectangulo(self, base, altura):
        """
        Calcula el área de un rectángulo.
        """
        return base * altura

    def area_triangulo(self, base, altura):
        """
        Calcula el área de un triángulo.
        """
        return (base * altura) / 2

    def area_circulo(self, radio):
        """
        Calcula el área de un círculo.
        """
        import math
        return math.pi * (radio ** 2)

    def perimetro_rectangulo(self, base, altura):
        """
        Calcula el perímetro de un rectángulo.
        """
        return 2 * (base + altura)

    def perimetro_circulo(self, radio):
        """
        Calcula el perímetro (circunferencia) de un círculo.
        """
        import math
        return 2 * math.pi * radio

    def volumen_cubo(self, lado):
        """
        Calcula el volumen de un cubo.
        """
        return lado ** 3

    def volumen_esfera(self, radio):
        """
        Calcula el volumen de una esfera.
        """
        import math
        return (4/3) * math.pi * (radio ** 3)

    def distancia_puntos(self, x1, y1, x2, y2):
        """
        Calcula la distancia entre dos puntos en el plano.
        """
        import math
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def pendiente_recta(self, x1, y1, x2, y2):
        """
        Calcula la pendiente de la recta que pasa por dos puntos.
        """
        if x2 - x1 == 0:
            return None  # pendiente indefinida (recta vertical)
        return (y2 - y1) / (x2 - x1)

    def ecuacion_recta(self, x1, y1, x2, y2):
        """
        Devuelve la ecuación de la recta en forma Ax + By + C = 0 que pasa por dos puntos.
        """
        A = y2 - y1
        B = -(x2 - x1)
        C = (x2 - x1) * y1 - (y2 - y1) * x1
        return (A, B, C)
