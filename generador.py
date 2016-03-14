"""
Un generador de senal es el responsable de generar una senal portadora.

"""
class Signal(object):
     
    def __init__(self, amplitud, fase, frecuencia):
        self.amplitud = amplitud
        self.fase = fase
        self.frecuencia = frecuencia

        # muestras por segundo
        self.frecuencia_muestreo = frecuencia * 3


class Generador(object):

    def __init__(self):
        pass
        
    def generar(self, amplitud, fase, frecuencia, tiempo_inicial, tiempo_final):

        import math
        import random as rnd

        signal = Signal(amplitud, fase, frecuencia)

        signal.tiempo_inicial = tiempo_inicial
        signal.tiempo_final = tiempo_final

        cantidad_muestras = (tiempo_final - tiempo_inicial).seconds * signal.frecuencia_muestreo

        muestras = range(cantidad_muestras)
        
        signal.data = []

        for i in muestras:
            signal.data.append(signal.amplitud * math.sin(2.00 * math.pi * signal.frecuencia* i * (1.00/ cantidad_muestras) + signal.fase) + rnd.random())

        return signal
