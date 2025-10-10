import time as tm
import numpy as np

matriz_adyacencia = np.array([
    [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, 140, 118,   0,   0,  75], # Arad
    [0,   0,   0,   0,   0, 211,  90,   0,   0,   0,   0,   0,   0, 101,   0,   0,   0,  85,   0,   0], # Bucarest
    [0,   0,   0, 120,   0,   0,   0,   0,   0,   0,   0,   0,   0, 138, 146,   0,   0,   0,   0,   0], # Craiova
    [0,   0, 120,   0,   0,   0,   0,   0,   0,   0,  75,   0,   0,   0,   0,   0,   0,   0,   0,   0], # Drobeta
    [0,   0,   0,   0,   0,   0,   0,  86,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0], # Eforie
    [0, 211,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  99,   0,   0,   0,   0], # Fagaras
    [0,  90,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0], # Giurgiu
    [0,   0,   0,   0,  86,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  98,   0,   0], # Hirsova
    [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  87,   0,   0,   0,   0,   0,   0,  92,   0], # Iasi
    [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  70,   0,   0,   0,   0,   0, 111,   0,   0,   0], # Lugoj
    [0,   0,   0,  75,   0,   0,   0,   0,   0,  70,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0], # Mehadia
    [0,   0,   0,   0,   0,   0,   0,   0,  87,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0], # Neamt
    [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, 151,   0,   0,   0,  71], # Oradea
    [0, 101, 138,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  97,   0,   0,   0,   0,   0], # Pitesti
    [0,   0, 146,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  97,   0,  80,   0,   0,   0,   0], # R. Vilcea
    [140, 0,   0,   0,   0,  99,   0,   0,   0,   0,   0,   0, 151,   0,  80,   0,   0,   0,   0,   0], # Sibiu
    [118, 0,   0,   0,   0,   0,   0,   0,   0, 111,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0], # Timisoara
    [0,  85,   0,   0,   0,   0,   0,  98,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, 142,   0], # Urziceni
    [0,   0,   0,   0,   0,   0,   0,   0,  92,   0,   0,   0,   0,   0,   0,   0,   0, 142,   0,   0], # Vaslui
    [75,  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  71,   0,   0,   0,   0,   0,   0,   0]  # Zerind
])

#Leyendo la hora:
def pedir_hora():
    hora = float(input("Ingresa la hora en formato HH.MM (ej: 14.30): "))
    hh = int(hora)
    mm = round((hora - hh) * 100)
    hora_decimal = hh + mm / 60
    return hora_decimal

#
def calculo_tiempo(salida_horaria):
    if 0 <= salida_horaria <= 5.983:  # Hasta 5:59 → 5 + 59/60 = 5.983
            new_matrix = matriz_adyacencia * 1
            print("De 00:00 a 05:59 → Se mantienen los datos originales.")

    elif 6 <= salida_horaria <= 15.983:  # Hasta 15:59
        new_matrix = matriz_adyacencia * 2
        print("De 06:00 a 15:59 → Se multiplica por 2 el tiempo.")

    elif 16 <= salida_horaria <= 23.983:  # Hasta 23:59
        new_matrix = matriz_adyacencia * 1.5
        print("De 16:00 a 23:59 → Se multiplica por 1.5 el tiempo.")

    else:
        print("Hora ingresada no válida.")
        return


def main():
    salida_horaria = pedir_hora()

    print("\nNueva matriz de tiempos:")

main()
