def crear_tablero():
    # Crear una matriz 8x8 para representar el tablero de ajedrez.
    return [['' for _ in range(8)] for _ in range(8)]

def posicion_a_indice(posicion):
    # Convertir una posición en notación ajedrecística a índices de matriz.
    col = ord(posicion[0]) - ord('a')
    fila = 8 - int(posicion[1])
    return fila, col

def posicion_valida(posicion):
    # Validar que una posición esté dentro de los límites del tablero.
    if len(posicion) != 2:
        return False
    col, fila = posicion[0], posicion[1]
    return col in 'abcdefgh' and fila in '12345678'

def agregar_pieza(tablero, pieza, color, posicion):
    # Agregar una pieza al tablero si la posición es válida y está libre.
    if posicion_valida(posicion):
        fila, col = posicion_a_indice(posicion)
        if tablero[fila][col] == '':
            tablero[fila][col] = f'{color[0].upper()}{pieza[0].upper()}'
            return True
    return False

def obtener_movimientos_caballo(tablero, posicion, color_caballo):
    # Obtener los movimientos válidos del caballo, evitando posiciones con piezas del mismo color.
    fila, col = posicion_a_indice(posicion)
    movimientos = [
        [fila + 2, col + 1], [fila + 2, col - 1],
        [fila - 2, col + 1], [fila - 2, col - 1],
        [fila + 1, col + 2], [fila + 1, col - 2],
        [fila - 1, col + 2], [fila - 1, col - 2]
    ]
    movimientos_validos = []
    for f, c in movimientos:
        if 0 <= f < 8 and 0 <= c < 8:
            pieza = tablero[f][c]
            if pieza == '' or pieza[0] != color_caballo[0].upper():
                movimientos_validos.append((f, c))
    return movimientos_validos

def imprimir_tablero(tablero):
    # Imprimir el tablero con formato simétrico utilizando ASCII art.
    letras = '    a    b    c    d    e    f    g    h  '
    borde_superior = '  +---+---+---+---+---+---+---+---+---+---+'
    borde_inferior = '  ++---+---+---+---+---+---+---+---+---+---+'

    print(letras)
    print(borde_superior)
    for i, fila in enumerate(tablero):
        linea = f'{8 - i} | ' + ' | '.join(pieza if pieza else '  ' for pieza in fila) + ' |'
        print(linea)
        print(borde_inferior)

def obtener_input_valido(mensaje, validacion):
    # Obtener input del usuario y validar hasta que sea correcto.
    while True:
        entrada = input(mensaje)
        if validacion(entrada):
            return entrada
        else:
            print("Entrada inválida. Intente de nuevo.")

def validar_entero_positivo(entrada):
    # Validar que la entrada sea un número entero positivo.
    return entrada.isdigit() and int(entrada) > 0

def validar_tipo_pieza(pieza):
    # Validar que el tipo de pieza sea válido.
    return pieza in ['alfil', 'peon', 'caballo', 'torre', 'rey', 'reina']

def validar_color(color):
    # Validar que el color sea válido.
    return color in ['blanco', 'negro']

def main():
    # Función principal que coordina la ejecución del programa.
    tablero = crear_tablero()
    piezas = int(obtener_input_valido("Ingrese la cantidad de piezas a agregar: ", validar_entero_positivo))
    for _ in range(piezas):
        pieza = obtener_input_valido("Ingrese el tipo de pieza (alfil, peon, caballo, torre, rey, reina): ", validar_tipo_pieza)
        color = obtener_input_valido("Ingrese el color de la pieza (blanco/negro): ", validar_color)
        posicion = obtener_input_valido("Ingrese la posición de la pieza (ej., a1): ", posicion_valida)
        while not agregar_pieza(tablero, pieza, color, posicion):
            print("Posición inválida o ya ocupada. Inténtelo de nuevo.")
            posicion = obtener_input_valido("Ingrese la posición de la pieza (ej., a1): ", posicion_valida)

    pos_caballo = obtener_input_valido("Ingrese la posición del caballo a evaluar (ej., e4): ", posicion_valida)
    color_caballo = obtener_input_valido("Ingrese el color del caballo (blanco/negro): ", validar_color)
    fila, col = posicion_a_indice(pos_caballo)
    while tablero[fila][col] != '':
        print("La posición ya está ocupada por otra pieza. Inténtelo de nuevo.")
        pos_caballo = obtener_input_valido("Ingrese la posición del caballo a evaluar (ej., e4): ", posicion_valida)
        fila, col = posicion_a_indice(pos_caballo)

    movimientos_caballo = obtener_movimientos_caballo(tablero, pos_caballo, color_caballo)
    print("Movimientos posibles para el caballo:")
    for f, c in movimientos_caballo:
        pos = f'{chr(c + ord("a"))}{8 - f}'
        info_pieza = tablero[f][c]
        if info_pieza == '':
            print(f"{pos}: vacía")
        else:
            print(f"{pos}: {info_pieza[1]} de color {info_pieza[0]}")

    print("\nTablero:")
    imprimir_tablero(tablero)

if __name__ == "__main__":
    main()