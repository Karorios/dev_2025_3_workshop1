class Data:
    """
    Clase con métodos para manipulación de datos en listas y estructuras similares.
    Incluye operaciones como suma, promedio, búsqueda de máximos/mínimos, limpieza de duplicados
    y estructuras de datos como pila y cola.
    """

    def suma_lista(self, lista):
        return sum(lista)

    def promedio_lista(self, lista):
        if not lista:
            return 0
        return sum(lista) / len(lista)

    def maximo_lista(self, lista):
        return max(lista) if lista else None

    def minimo_lista(self, lista):
        return min(lista) if lista else None

    def eliminar_duplicados(self, lista):
        resultado = []
        visto = set()
        for item in lista:
            clave = (type(item), item)  # distingue por valor y tipo
            if clave not in visto:
                resultado.append(item)
                visto.add(clave)
        return resultado

    def ordenar_lista(self, lista):
        return sorted(lista)

    def contar_elemento(self, lista, elemento):
        return lista.count(elemento)

    def existe_elemento(self, lista, elemento):
        return elemento in lista

    def concatenar_listas(self, lista1, lista2):
        return lista1 + lista2

    # =========================
    # Métodos adicionales para tests
    # =========================

    def invertir_lista(self, lista):
        return lista[::-1]

    def buscar_elemento(self, lista, elemento):
        try:
            return lista.index(elemento)
        except ValueError:
            return -1

    def merge_ordenado(self, lista1, lista2):
        return sorted(lista1 + lista2)

    def rotar_lista(self, lista, n):
        if not lista:
            return []
        n = n % len(lista)  # manejo de n mayor que len(lista)
        return lista[-n:] + lista[:-n]

    def encuentra_numero_faltante(self, lista):
        # asumimos que lista tiene números consecutivos excepto 1 faltante
        minimo = min(lista)
        maximo = max(lista)
        esperado = set(range(minimo, maximo + 1))
        faltante = list(esperado - set(lista))
        if faltante:
            return faltante[0]
        # si no falta dentro, puede faltar en los extremos
        if 1 not in lista:
            return 1
        return maximo + 1

    def es_subconjunto(self, lista1, lista2):
        return set(lista1).issubset(set(lista2))

    def implementar_pila(self):
        pila = []

        return {
            "push": lambda x: pila.append(x),
            "pop": lambda: pila.pop() if pila else None,
            "peek": lambda: pila[-1] if pila else None,
            "is_empty": lambda: len(pila) == 0
        }

    def implementar_cola(self):
        from collections import deque
        cola = deque()

        return {
            "enqueue": lambda x: cola.append(x),
            "dequeue": lambda: cola.popleft() if cola else None,
            "peek": lambda: cola[0] if cola else None,
            "is_empty": lambda: len(cola) == 0
        }

    def matriz_transpuesta(self, matriz):
        if not matriz:
            return []
        return [list(fila) for fila in zip(*matriz)]
