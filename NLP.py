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
class Stemmer:
    "Realiza stemming a un texto."

    def _init_(self):
        self.letras_con_acento = "áéíóúüñ"
        self.letras_sin_acento = "aeiouun"
        self.pronombres_encliticos = ["nos", "me", "te", "os", "se", "ando", "endo", "ea", "la", "lo", "ear", "las", "los", "le", "les", "izar", "ecer", "ificar", "al"]
        self.terminaciones_verbales = ["ar", "er", "ir"]
        self.desinencias_verbales = {
            "ar": ["mos", "ais", "eis", "an", "bas", "ba", "bamos", "bais", "ban", "ste", "steis", "ron", "re", "ras", "ra", "remos", "reis", "ran", "ria", "rias", "riamos", "riais", "rian", "se", "ndo", "ndo"],
            "er": ["mos", "ais", "eis", "an", "bas", "ba", "bamos", "bais", "ban", "ste", "steis", "eron", "ere", "eras", "era", "eremos", "ereis", "eran", "eria", "erias", "eriamos", "eriais", "erian", "ese", "iendo", "iendo"],
            "ir": ["mos", "ais", "eis", "an", "bas", "ba", "bamos", "bais", "ban", "ste", "steis", "eron", "ire", "iras", "ira", "iremos", "ireis", "iran", "iria", "irias", "iriamos", "iriais", "irian", "iese", "iendo", "iendo"]
        }
        self.sufijos_sustantivos = ["a", "o", "e", "es", "os", "as", "ador", "adora", "amiento", "anza", "cion", "era", "iza", "ero", "eza", "ion"]
        self.sufijos_rv = {"o": "ó", "a": "á", "e": "é"}

    def stem(self, texto):
        """Aplica stemming por palabra a un texto."""

        palabras = texto.split()
        palabras_procesadas = [self.stem_palabra(palabra) if len(palabra) > 4 else palabra for palabra in palabras]
        texto_procesado = " ".join(palabras_procesadas)
        return texto_procesado

    def stem_palabra(self, palabra):
        """Aplica stemming a una palabra si tiene más de tres letras."""

        # Elimina los acentos del texto
        palabra = self.eliminar_acentos(palabra)

        # Elimina terminaciones verbales
        palabra = self.eliminar_terminaciones_verbales(palabra)

        # Elimina pronombres enclíticos
        palabra = self.eliminar_pronombres_encliticos(palabra)

        # Elimina desinencias verbales
        palabra = self.eliminar_desinencias_verbales(palabra)

        # Eliminación del número del sufijo
        palabra = self.eliminar_numero_sufijo(palabra)

        # Eliminación de sufijo
        palabra = self.eliminar_sufijo(palabra)

        # Reducción vocálica
        palabra = self.reducir_vocalica(palabra)

        return palabra
    
    def eliminar_acentos(self, texto):
        """Elimina los acentos, comas y puntos del texto."""
        sin_acentos = ""
        for letra in texto:
            if letra in self.letras_con_acento:
                indice = self.letras_con_acento.index(letra)
                sin_acentos += self.letras_sin_acento[indice]
            elif letra not in [',', '.']:
                sin_acentos += letra
        return sin_acentos

    def eliminar_terminaciones_verbales(self, texto):
        """Elimina las terminaciones verbales."""
        for terminacion in self.terminaciones_verbales:
            if texto.endswith(terminacion):
                texto = texto[:-len(terminacion)]
                break
        return texto

    def eliminar_pronombres_encliticos(self, texto):
        """Elimina los pronombres enclíticos."""
        for pronombre in self.pronombres_encliticos:
            if texto.endswith(pronombre):
                texto = texto[:-len(pronombre)]
                break
        return texto

    def eliminar_desinencias_verbales(self, texto):
        """Elimina las desinencias verbales."""
        for terminacion, desinencias in self.desinencias_verbales.items():
            for desinencia in desinencias:
                if texto.endswith(desinencia):
                    texto = texto[:-len(desinencia)]
                    break
        return texto

    def eliminar_numero_sufijo(self, palabra):
        """Elimina el número del sufijo."""
        if palabra.endswith("s"):
            palabra = palabra[:-1]
        return palabra

    def eliminar_sufijo(self, palabra):
        """Elimina el sufijo."""
        for sufijo in self.sufijos_sustantivos:
            if palabra.endswith(sufijo):
                palabra = palabra[:-len(sufijo)]
                break
        return palabra

    def reducir_vocalica(self, palabra):
        """Realiza la reducción vocálica."""
        for vocal, acentuada in self.sufijos_rv.items():
            palabra = palabra.replace(acentuada, vocal)
        return palabra

#
