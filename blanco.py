class Blanco(object):
    """
    Define un blanco a ser detectado por un radar
    """

    def __init__(self, amplitud, tiempo_inicial, tiempo_final):
        self.amplitud = amplitud
        self.tiempo_inicial = tiempo_inicial
        self.tiempo_final = tiempo_final

    def reflejar(self, senal):

        muestra_inicial_blanco = (self.tiempo_inicial - senal.tiempo_inicial).seconds * senal.frecuencia_muestreo
        muestra_final_blanco = (self.tiempo_final - senal.tiempo_inicial).seconds * senal.frecuencia_muestreo
        muestra_final_senal = (senal.tiempo_final - senal.tiempo_inicial).seconds * senal.frecuencia_muestreo
        
        if self.tiempo_inicial > senal.tiempo_inicial and self.tiempo_final < senal.tiempo_final:
            for i in range(muestra_inicial_blanco, muestra_final_blanco):
                senal.data[i] = senal.data[i] * self.amplitud        

        elif self.tiempo_inicial > senal.tiempo_inicial and self.tiempo_final > senal.tiempo_final:
            for i in range(muestra_inicial_blanco, muestra_final_senal):
                senal.data[i] = senal.data[i] * self.amplitud
       
        elif self.tiempo_inicial < senal.tiempo_inicial and self.tiempo_final < senal.tiempo_final:
            for i in range(0, muestra_final_blanco):
                senal.data[i] = senal.data[i] * self.amplitud
       
        elif self.tiempo_inicial < senal.tiempo_inicial and self.tiempo_final > senal.tiempo_final:
            for i in range(0, muestra_final_senal):
                senal.data[i] = senal.data[i] * self.amplitud


       
