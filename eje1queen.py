"""
(El siguiente script es un esqueleto que se sugiere para sus implementaciones, pueden hacer todas las modificaciones que consideren necesarias. Se incluyen referencias a la documentacion de Python.)
Práctica DFS — Problema de las N reinas
-----------------------
Completa los TODO para implementar búsquedas en profundidad (DFS) con retroceso (backtracking).

Convenciones del problema:
- Representamos una solución como una lista P de tamaño N.
  P[c] = r significa: en la columna c colocamos una reina en el renglón r.
- Las columnas se recorren de 0 a N-1.
- Para el ejercicio 2 (con obstáculos), A es una lista de longitud 0..N.
  Interpretación: si A[j] existe, el renglón A[j] en la columna j está BLOQUEADO.
  (Ejemplo: A = [1,3,0,2] bloquea (col=0,row=1), (1,3), (2,0), (3,2).)
"""

from typing import List, Optional


# --------------------------------------------------------
# Función auxiliar para verificar conflictos entre reinas
# --------------------------------------------------------


def en_conflicto(parcial: List[int], fila: int, col: int) -> bool:
    """
    Regresa True si colocar una reina en (fila, col) entra en conflicto
    con alguna reina ya colocada en el arreglo parcial (columnas 0..col-1).

    Conflictos:
      - misma fila
      - misma diagonal (|Δfila| == |Δcol|)

    TODO: implementar las condiciones de conflicto.

     Referencia: https://docs.python.org/3/tutorial/datastructures.html
    """
    for c_prev, r_prev in enumerate(parcial):
        # misma fila
        if r_prev == fila:
            return True
        # misma diagonal
        if abs(r_prev - fila) == abs(c_prev - col):
            return True
        pass  # TODO: reemplazar por return True si hay conflicto
    return False


# --------------------------------------------------------
# Ejercicio 1 — DFS para encontrar UNA solución
# --------------------------------------------------------
def nreinas(N: int) -> Optional[List[int]]:
    """
    Regresa una solución válida P (lista de tamaño N) o None si no existe.

    Estrategia:
      - DFS por columnas: intenta colocar en cada columna una fila válida.
      - Usa backtracking: si una elección no lleva a solución, deshaz y prueba otra.

     Concepto: El backtracking es una búsqueda en profundidad (DFS)
    que explora todas las combinaciones posibles, retrocediendo cuando
    una elección lleva a un callejón sin salida.
    """
    parcial: List[int] = []

    def dfs(col: int) -> bool:
        if col == N:
            return True  # se colocaron N reinas

        for fila in range(N):
            if not en_conflicto(parcial, fila, col):
                parcial.append(fila)  # elegir
                if dfs(col + 1):  # explorar
                    return True
                parcial.pop()  # deshacer (retroceso)
        return False

    if N < 1:
        return None

    if dfs(0):
        return parcial
    return None


def posibles(N: int) -> List[List[int]]:
        
   
    """
    Devuelve una lista con todas las soluciones posibles P (listas de tamaño N)
    o una lista vacía si no existen soluciones.

    Método:
      - Se utiliza una búsqueda en profundidad (DFS) por columnas.
      - En cada columna, se intenta colocar una pieza en una fila válida.
      - Si una colocación no conduce a una solución, se retrocede (backtracking)
        y se prueban otras opciones.
    """
  
    posibles = [] # Lista para almacenar todas las soluciones encontradas
        

    def dfs(col: int, parcial: List[int]) -> None:
        if col == N:
            posibles.append(parcial.copy()) # se encontro una solución
            return
        for fila in range(N):
            if not en_conflicto(parcial, fila, col):
                parcial.append(fila) # elegir
                dfs(col + 1, parcial)  # explorar
                parcial.pop() # deshacer (retroceso)

    dfs(0, []) # Inicia el DFS desde la columna 0 con una lista parcial vacía
    return posibles if posibles else "No hay solución para N = {N}"



def ejecutar():
    N = int(input("Ingrese el número de reinas (N) : "))
    todas = posibles(N)
    print(f"Todas las soluciones para N={N}: {todas}")  






# --------------------------------------------------------
#  Pistas conceptuales
# --------------------------------------------------------
# - DFS (Depth-First Search) recorre todas las posibilidades posibles en un árbol de decisiones.
# - El retroceso (backtracking) se logra con recursión: probar → explorar → deshacer.
# - Conflictos en N reinas: misma fila o diagonales.
# - En Python, las listas son mutables; usa copy() si vas a guardar estados intermedios.

#  Referencias oficiales:
# - Listas y operaciones: https://docs.python.org/3/tutorial/datastructures.html
# - Tipos (typing): https://docs.python.org/3/library/typing.html
# - Recursión y funciones: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# --------------------------------------------------------


if __name__ == "__main__":
    
    ejecutar()
