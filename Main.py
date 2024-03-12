"""
Created on Mon Mar 11 22:02:23 2024

@author: Bren Guzmán
"""

#%% LIBRERÍAS
from NLP import Lematizador

#%% TEXTO 
texto_ejemplo = '''
Con estos fines, la Dirección de Gestión y Control Financiero monitorea
la posición de capital del Banco y utiliza los mecanismos para hacer un
eficiente manejo del capital.
'''

#%% LEMATIZACIÓN
lematizador = Lematizador()
texto_lematizado = lematizador.lematizar_texto_completo(texto_ejemplo)
print(texto_lematizado)

#%% STEMMING
