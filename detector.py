class Detector(object):

    def __init__(self):
        pass

    def detectar(self, senal_generada, senal_reflejada):
        
        import numpy as np

        mean = np.mean(senal_generada.data)
        std = np.std(senal_generada.data)

        for i in range(0, len(senal_reflejada.data)):
            if np.abs(senal_reflejada.data[i] - senal_generada.data[i]) > mean + 2 * std:
                 # el criterio es de hallar un blanco es alejarse bastante del valor medio de la senal generada
                 return "Blanco encontrado"
        
