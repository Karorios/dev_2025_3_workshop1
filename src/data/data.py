class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """

    def invertir_lista(self, lista):
        """
        Invierte el orden de los elementos en una lista sin usar reversed() o lista[::-1].
        """
        resultado = []
        for i in range(len(lista) - 1, -1, -1):
            resultado.append(lista[i])
        return resultado

    def buscar_elemento(self, lista, elemento):
        """
        Busca un elemento en una lista y devuelve su índice (o -1 si no existe).
        """
        for i, val in enumerate(lista):
            if val == elemento:
                return i
        return -1

    def eliminar_duplicados(self, lista):
        """
        Elimina elementos duplicados manteniendo el orden original.
        """
        resultado = []
        visto = set()
        for item in lista:
            if item not in visto:
                resultado.append(item)
                visto.add(item)
        return resultado

    def merge_ordenado(self, lista1, lista2):
        """
        Combina dos listas ordenadas en una sola lista ordenada.
        """
        i, j = 0, 0
        resultado = []
        while i < len(lista1) and j < len(lista2):
            if lista1[i] <= lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1
        # agregar restos
        resultado.extend(lista1[i:])
        resultado.extend(lista2[j:])
        return resultado

    def rotar_lista(self, lista, k):
        """
        Rota los elementos de una lista k posiciones a la derecha.
        """
        if not lista:
            return []
        n = len(lista)
        k = k % n
        return lista[-k:] + lista[:-k]

    def encuentra_numero_faltante(self, lista):
        """
        Encuentra el número faltante en una lista de enteros del 1 al n.
        """
        n = len(lista) + 1
        suma_total = n * (n + 1) // 2
        return suma_total - sum(lista)

    def es_subconjunto(self, conjunto1, conjunto2):
        """
        Verifica si conjunto1 es subconjunto de conjunto2.
        """
        for item in conjunto1:
            if item not in conjunto2:
                return False
        return True

    def implementar_pila(self):
        """
        Implementa una pila con métodos push, pop, peek y is_empty.
        """
        pila = []

        def push(x):
            pila.append(x)

        def pop():
            if pila:
                return pila.pop()
            return None

        def peek():
            if pila:
                return pila[-1]
            return None

        def is_empty():
            return len(pila) == 0

        return {
            "push": push,
            "pop": pop,
            "peek": peek,
            "is_empty": is_empty,
        }

    def implementar_cola(self):
        """
        Implementa una cola con métodos enqueue, dequeue, peek y is_empty.
        """
        cola = []

        def enqueue(x):
            cola.append(x)

        def dequeue():
            if cola:
                return cola.pop(0)
            return None

        def peek():
            if cola:
                return cola[0]
            return None

        def is_empty():
            return len(cola) == 0

        return {
            "enqueue": enqueue,
            "dequeue": dequeue,
            "peek": peek,
            "is_empty": is_empty,
        }

    def matriz_transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz.
        """
        if not matriz:
            return []
        filas = len(matriz)
        columnas = len(matriz[0])
        resultado = [[0] * filas for _ in range(columnas)]
        for i in range(filas):
            for j in range(columnas):
                resultado[j][i] = matriz[i][j]
        return resultado
