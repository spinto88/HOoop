import radar
import medio
import blanco
import generador
import datetime
import detector


# DISCLAMER!!
# todo esta en castellano por razones didacticas
# pero DEBEN programar en INGLES
# uno nunca sabe quien puede leer su codigo

def main():

    # Intervalo de tiempo en el que vamos a medir
    tiempo_inicial = datetime.datetime(2016, 3, 5, 1)
    tiempo_final = datetime.datetime(2016, 3, 5, 10)

    import math
    # parametros del generador de senales
    amplitud = 0.2
    fase = 1
    frecuencia = 20

    gen = generador.Generador()
    detect = detector.Detector()
    rad = radar.Radar(gen, detect)

    senal = rad.generador.generar(amplitud, fase, frecuencia, tiempo_inicial, tiempo_final)

    # parametros para un blanco
    amplitud_de_frecuencia_del_blanco = amplitud + 100
    tiempo_inicial_del_blanco = datetime.datetime(2016, 3, 5, 2)
    tiempo_final_del_blanco = datetime.datetime(2016, 3, 5, 4)
    
    blc = blanco.Blanco(amplitud_de_frecuencia_del_blanco, tiempo_inicial_del_blanco, tiempo_final_del_blanco)

    md = medio.Medio(blc)

    senal_reflejada = md.reflejar(senal)
 
    rad.detector.detectar(senal, senal_reflejada)

    import matplotlib.pyplot as plt
    plt.plot(senal_reflejada.data)
    plt.show()

    
if __name__ == "__main__":
    main()
