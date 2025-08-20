class Data:
    """
    Clase con métodos para manipulación de datos en listas y estructuras similares.
    Incluye operaciones como suma, promedio, búsqueda de máximos/mínimos y limpieza de duplicados.
    """

    def suma_lista(self, lista):
        """
        Calcula la suma de todos los elementos de una lista numérica.
        """
        return sum(lista)

    def promedio_lista(self, lista):
        """
        Calcula el promedio de una lista numérica.
        """
        if not lista:
            return 0
        return sum(lista) / len(lista)

    def maximo_lista(self, lista):
        """
        Devuelve el valor máximo de una lista.
        """
        return max(lista) if lista else None

    def minimo_lista(self, lista):
        """
        Devuelve el valor mínimo de una lista.
        """
        return min(lista) if lista else None

    def eliminar_duplicados(self, lista):
        """
        Elimina elementos duplicados manteniendo el orden original.
        Distingue entre valores iguales pero de distinto tipo (ej: 1 y True).
        """
        resultado = []
        visto = set()
        for item in lista:
            clave = (type(item), item)  # clave única por tipo y valor
            if clave not in visto:
                resultado.append(item)
                visto.add(clave)
        return resultado

    def ordenar_lista(self, lista):
        """
        Ordena una lista de forma ascendente.
        """
        return sorted(lista)

    def contar_elemento(self, lista, elemento):
        """
        Cuenta cuántas veces aparece un elemento en la lista.
        """
        return lista.count(elemento)

    def existe_elemento(self, lista, elemento):
        """
        Verifica si un elemento existe en la lista.
        """
        return elemento in lista

    def concatenar_listas(self, lista1, lista2):
        """
        Concatena dos listas en una sola.
        """
        return lista1 + lista2
