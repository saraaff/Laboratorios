#variables
y=0
x=0
#area def funciones
def Moverhaciaarriba():
    global y
    y=+1

def Moverhaciaabajo():
    global y
    y=-1

def Moverhaciladerecha():
    global x
    x=+1

def Moverhacilaizquiera():
    global x
    x=-1
    
#area interacción con el usuario
print("Semana No. 15: Ejercicio 2")

while True:
        print("Opciones:")
        print("a. Sube")
        print("b. Baja")
        print("c. Izquierda")
        print("d. Derecha")
        print("e. Salir")
        
        opcion = input("Seleccione una opción: ").lower
        
        match opcion:
            case "a":
                Moverhaciaarriba()
            case "b":
                Moverhaciaabajo()
            case "c":
                Moverhaciladerecha()
            case "d":
                Moverhacilaizquiera()
            case "e":
                print("Coordenadas del personaje:", x, ",", y)
                break