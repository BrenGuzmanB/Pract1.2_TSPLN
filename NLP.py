"""
Created on Mon Mar 11 21:11:34 2024

@author: Bren Guzmán
"""

# Lematización
class Lematizador:
    def __init__(self):
        self.reglas = self.cargar_reglas()
        self.excepciones = self.cargar_excepciones()

    def cargar_reglas(self):
        reglas = {}
        with open('reglas.txt', 'r') as file:
            for line in file:
                palabra, lema = line.strip().split(':')
                reglas[palabra] = lema
        return reglas

    def cargar_excepciones(self):
        excepciones = {}
        with open('excepciones.txt', 'r') as file:
            for line in file:
                palabra, lema = line.strip().split(':')
                excepciones[palabra] = lema
        return excepciones

    def lematizar_texto_completo(self, texto):
        tokens = texto.split()
        lematizado = [self.lematizar_palabra(token) for token in tokens]
        return ' '.join(lematizado)

    def lematizar_palabra(self, palabra):
        palabra_sin_puntuacion = palabra.strip(",.")
        if palabra_sin_puntuacion in self.excepciones:
            return self.excepciones[palabra_sin_puntuacion]
        for regla, lema in self.reglas.items():
            if palabra_sin_puntuacion.endswith(regla):
                return palabra_sin_puntuacion[:-len(regla)] + lema
        return palabra
    

# Stemming
