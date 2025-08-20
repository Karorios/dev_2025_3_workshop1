class Stats:
    """
    Clase con métodos estadísticos básicos:
    promedio, mediana, moda, desviación estándar, varianza y rango.
    """

    def promedio(self, datos):
        """Calcula el promedio de una lista de números."""
        if not datos:
            return 0
        return sum(datos) / len(datos)

    def mediana(self, datos):
        """Calcula la mediana de una lista de números."""
        if not datos:
            return 0
        datos_ordenados = sorted(datos)
        n = len(datos_ordenados)
        medio = n // 2
        if n % 2 == 0:
            return (datos_ordenados[medio - 1] + datos_ordenados[medio]) / 2
        else:
            return float(datos_ordenados[medio])

    def moda(self, datos):
        """Calcula la moda de una lista (primer valor en caso de empate)."""
        if not datos:
            return None
        frecuencias = {}
        for valor in datos:
            frecuencias[valor] = frecuencias.get(valor, 0) + 1
        max_frecuencia = max(frecuencias.values())
        for valor in datos:
            if frecuencias[valor] == max_frecuencia:
                return valor

    def varianza(self, datos):
        """Calcula la varianza poblacional de una lista de números."""
        if not datos:
            return 0
        if len(datos) == 1:
            return 0.0
        promedio = self.promedio(datos)
        return sum((x - promedio) ** 2 for x in datos) / len(datos)

    def desviacion_estandar(self, datos):
        """Calcula la desviación estándar poblacional."""
        if not datos:
            return 0
        return self.varianza(datos) ** 0.5

    def rango(self, datos):
        """Calcula el rango (máximo - mínimo) de una lista."""
        if not datos:
            return 0
        return max(datos) - min(datos)
