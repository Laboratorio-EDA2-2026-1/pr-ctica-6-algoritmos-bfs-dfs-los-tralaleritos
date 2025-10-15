import numpy as np
from collections import deque

#Matriz de adyacencia ya creada con clases anteriores
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

lista_ciudades_disponibles = [
    "Arad", "Bucarest", "Craiova", "Drobeta", "Eforie", "Fagaras", "Giurgiu", 
    "Hirsova", "Iasi", "Lugoj", "Mehadia", "Neamt", "Oradea", "Pitesti", 
    "R. Vilcea", "Sibiu", "Timisoara", "Urziceni", "Vaslui", "Zerind"
]

lista_franjas_horarias = [
    #Escribimos las franjas como:
    #Hora de inicio, Hora final, Multiplicador a Aplicar
    (0, 6, 1.0),
    (6, 16, 2.0),
    (16, 24, 1.5)
]

def get_multiplicador(minutos_desde_medianoche):
    #Verificamos en que parte del trayecto nos encontramos para extraer de alli el multiplicador
    #Ya sea 1, 1.5, o 2, el cual se lo aplicaremos al tiempo original del trayecto que esta marcado en la matriz de adyacencia
    hora_actual = (minutos_desde_medianoche / 60) % 24
    for inicio, fin, multiplicador in lista_franjas_horarias:
        if inicio <= hora_actual < fin:
            #si la hora actual es mayor que la de inicio y menor que la de fin, regresamos el multiplicador indicado, el cual seria el 3ro en aparecer
            return multiplicador
    #Si esto no ocurre, solo regresamos 1, ya que significa que deberiamos mantener el multiplicador de 1
    return 1.0

def bfs(matriz, inicio, fin):
    #Algoritmo BFS implementado
    #El BFS guarda una cola de caminos parciales, donde en cada paso toma un camino
    #crea nuevas versiones más largas yendo a cada vecino posible, y las vuelve a meter en la cola para revisarlas después.
    cola = deque([[inicio]])
    visitados = {inicio}
    
    while cola:
        ruta_actual = cola.popleft()
        ultima_ciudad = ruta_actual[-1]
        
        if ultima_ciudad == fin:
            return ruta_actual
            
        for vecina, tiempo_base in enumerate(matriz[ultima_ciudad]):
            if tiempo_base > 0 and vecina not in visitados:
                visitados.add(vecina)
                nueva_ruta = list(ruta_actual)
                nueva_ruta.append(vecina)
                cola.append(nueva_ruta)
                
    return []

def main():
    #Enlistando las ciudades que hay para viajar
    for i, ciudad in enumerate(lista_ciudades_disponibles):
        print(f"[{i}] {ciudad}\n", end="  ")
    
    #Pidiendo al usuario de que lugar a que lugar desea viajar
    origen = int(input("Ingrese el número de la ciudad de ORIGEN: "))
    destino = int(input("Ingrese el número de la ciudad de DESTINO: "))
    
    #Pidiendo hora de salida
    hora_str = input("Ingrese la hora de inicio del viaje (formato HH:MM, ej: 05:00): ")
    
    #quitamos los caracteres inecesarios como el :
    h, m = map(int, hora_str.split(':'))
    #Pasamos a minutos la hora y minutomde salida
    hora_inicio_minutos = h * 60 + m
    
    #Utilizaremos BFS para tener una idea de como sera la ruta que se tomara
    #Esta variable sera una lista o arreglo, que guarda los indices de cada parada, es decir [6,1,17], que nos indicaria que pasa de Giurgu a Bucharest
    #Y de bucharest a urziceni
    ruta_indices = bfs(matriz_adyacencia, origen, destino)
    #Matriz de adyacencia, lugar de origen, lugar del destino
    
    print("\nRESULTADOS DE LA APLICACION DE BFS")
    if not ruta_indices:
        print("No se encontró una ruta entre las ciudades seleccionadas.")
        return

    tiempo_total_real = 0
    hora_actual_minutos = hora_inicio_minutos

    print(f"Ruta encontrada por BFS: {' → '.join([lista_ciudades_disponibles[i] for i in ruta_indices])}\n")

    for i in range(len(ruta_indices) - 1):
        #Toma por ejemplo de la ruta [6, 1 ,17], al valor 6
        ciudad_origen_tramo = ruta_indices[i]
        #De la ruta [6, 1 ,17], toma al valor que le sigue al 6 el cual es 1
        ciudad_destino_tramo = ruta_indices[i+1]
        
        #Buscamos en la matriz el tiempo en que se encuentra apoyandonos de los indices, ya que 6 sera el indicado para Giurgu, el 1 para bucarest
        tiempo_base = matriz_adyacencia[ciudad_origen_tramo][ciudad_destino_tramo]
        
        #tomamos el multiplicador que se usara gracias a la funcion que nos dira los minutos en que estamos
        #importante obtener el multiplicador primero, yua que este sera con base a la hora de salida, la inicial vaya
        multiplicador = get_multiplicador(hora_actual_minutos)
        
        #Creamos variable tiempo real, la cual sera el tiempo base, por el multiplicador obtenido
        tiempo_real_del_tramo = tiempo_base * multiplicador

        #La hora de llegada del tramo sera simplemente sumar la hora actual en que nos encontramos, mas la del tramo 
        hora_llegada_tramo = hora_actual_minutos + tiempo_real_del_tramo
        
        # Muestra el tramo actual del viaje, ej: "Giurgiu → Bucarest".
        print(f"Tramo: {lista_ciudades_disponibles[ciudad_origen_tramo]} → {lista_ciudades_disponibles[ciudad_destino_tramo]}")
        # Muestra a qué hora arranca este tramo y el factor de tráfico que se le aplica.
        print(f"  - Inicia a las: {int(hora_actual_minutos//60):02d}:{int(hora_actual_minutos%60):02d}. Multiplicador aplicado a la matriz de adyacencia: x{multiplicador}")
        # Muestra cuánto va a durar este pedazo del viaje en minutos.
        print(f"  - Duración real del tramo: {int(tiempo_real_del_tramo)} minutos.")
        # Calcula y muestra a qué hora se llega al final de este tramo.
        print(f"  - Llegada a {lista_ciudades_disponibles[ciudad_destino_tramo]} a las: {int(hora_llegada_tramo//60)%24:02d}:{int(hora_llegada_tramo%60):02d}")
        print()

        #Sumamos 
        hora_actual_minutos += tiempo_real_del_tramo
        tiempo_total_real += tiempo_real_del_tramo
    
    #imprimimos la llegada al destino utilizando la misma logica de dividir entre 60 para obtener el entero de la hora
    #Y el modulo se usa para obtener el minutero, ya que es dividir entre 60 y lo q sobre
    print(f"Llegada al destino: {int(hora_actual_minutos//60)%24:02d}:{int(hora_actual_minutos%60):02d}")

main()
