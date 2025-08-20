import re

class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        """Verifica si una cadena es un palíndromo."""
        limpio = re.sub(r'[^a-zA-Z0-9]', '', texto).lower()
        return limpio == limpio[::-1]
    
    def invertir_cadena(self, texto):
        """Invierte una cadena de texto sin usar slicing ni reversed()."""
        invertida = ""
        for char in texto:
            invertida = char + invertida
        return invertida
    
    def contar_vocales(self, texto):
        """Cuenta el número de vocales en una cadena."""
        return sum(1 for c in texto if c.lower() in "aeiou")
    
    def contar_consonantes(self, texto):
        """Cuenta el número de consonantes en una cadena."""
        return sum(1 for c in texto if c.isalpha() and c.lower() not in "aeiou")
    
    def es_anagrama(self, texto1, texto2):
        """Verifica si dos cadenas son anagramas."""
        limpiar = lambda t: sorted(re.sub(r'[^a-zA-Z]', '', t).lower())
        return limpiar(texto1) == limpiar(texto2)
    
    def contar_palabras(self, texto):
        """Cuenta el número de palabras en una cadena."""
        palabras = texto.strip().split()
        return len(palabras)
    
    def palabras_mayus(self, texto):
        """Pon en mayúscula la primera letra de cada palabra en una cadena."""
        resultado = ""
        en_palabra = False
        for i, c in enumerate(texto):
            if c.isalpha() and not en_palabra:
                resultado += c.upper()
                en_palabra = True
            else:
                resultado += c
                if c.isspace():
                    en_palabra = False
        return resultado
    
    def eliminar_espacios_duplicados(self, texto):
        """Elimina espacios duplicados en una cadena."""
        return re.sub(r'\s+', ' ', texto)
    
    def es_numero_entero(self, texto):
        """Verifica si una cadena representa un número entero sin usar isdigit()."""
        if not texto:
            return False
        if texto[0] in ['-', '+']:
            return texto[1:].isdigit()
        return texto.isdigit()
    
    def cifrar_cesar(self, texto, desplazamiento):
        """Aplica el cifrado César a una cadena de texto."""
        resultado = ""
        for c in texto:
            if c.isalpha():
                base = ord('A') if c.isupper() else ord('a')
                resultado += chr((ord(c) - base + desplazamiento) % 26 + base)
            else:
                resultado += c
        return resultado
    
    def descifrar_cesar(self, texto, desplazamiento):
        """Descifra una cadena cifrada con el método César."""
        return self.cifrar_cesar(texto, -desplazamiento)
    
    def encontrar_subcadena(self, texto, subcadena):
        """Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index()."""
        if not subcadena:
            return []
        posiciones = []
        for i in range(len(texto) - len(subcadena) + 1):
            if texto[i:i+len(subcadena)] == subcadena:
                posiciones.append(i)
        return posiciones
