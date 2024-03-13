"""
Created on Mon Mar 11 22:02:23 2024

@author: BRENDA ITZEL GUZMÁN BONILLA, BRENDA GARCÍA BRIONES, MARÍA JOSÉ MERINO PÉREZ, MARLY GRACIELA MÁRQUEZ YÁÑEZ 
"""

#%% LIBRERÍAS
from NLP import Lematizador, Stemmer
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import spacy

#%% TEXTO 
texto_ejemplo = '''
Con estos fines, la Dirección de Gestión y Control Financiero monitorea
la posición de capital del Banco y utiliza los mecanismos para hacer un
eficiente manejo del capital.
'''

#%% LEMATIZACIÓN
lematizador = Lematizador()
texto_lematizado = lematizador.lematizar_texto_completo(texto_ejemplo)
print('\nTexto original:')
print(texto_ejemplo)
print('\n\nTexto lematizado:\n')
print(texto_lematizado)

#%% STEMMING
stemmer = Stemmer()
texto_procesado = stemmer.stem(texto_ejemplo)
print('\nTexto original:')
print(texto_ejemplo)
print('\n\nTexto derivado:\n')
print(texto_procesado)

#%% LEMATIZACIÓN OCUPANDO LIBRERÍAS
# Descargar el modelo si no está disponible
try:
    spacy.load('es_core_news_sm')
except OSError:
    import subprocess
    subprocess.run(["python", "-m", "spacy", "download", "es_core_news_sm"])

class Lemmatizer:
    def __init__(self):
        self.nlp = spacy.load('es_core_news_sm')

    def lemmatize_text(self, text):
        doc = self.nlp(text)
        lemmatized_words = [token.lemma_ for token in doc]
        return ' '.join(lemmatized_words)

def main():
    text = "Con estos fines, la Dirección de Gestión y Control Financiero monitorea la posición de capital del Banco y utiliza los mecanismos para hacer un eficiente manejo del capital."

    lemmatizer = Lemmatizer()
    lemmatized_text = lemmatizer.lemmatize_text(text)

    print("Texto original:")
    print(text)
    print("\nTexto procesado:")
    print(lemmatized_text)

if __name__ == "__main__":
    main()

#%% STEMMING OCUPANDO LIBRERÍAS
nltk.download('punkt')
class Stemmer:
    def __init__(self):
        self.stemmer = PorterStemmer()

    def stem_text(self, text):
        words = word_tokenize(text)
        stemmed_words = [self.stemmer.stem(word) for word in words]
        return ' '.join(stemmed_words)

def main():
    text = "Con estos fines, la Dirección de Gestión y Control Financiero monitorea la posición de capital del Banco y utiliza los mecanismos para hacer un eficiente manejo del capital."

    stemmer = Stemmer()
    stemmed_text = stemmer.stem_text(text)

    print("Texto original:")
    print(text)
    print("\nTexto procesado:")
    print(stemmed_text)

if __name__ == "__main__":
    main()
  
