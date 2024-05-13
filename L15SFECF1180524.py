#área def de funciones
import math
def menu():
    print("Elija una opción:")
    print("a. Área de triángulo")   
    print("b. Área de cuadrado")
    print("c. Área de rectángulo")
    print("d. Área de círculo")
    opcion=input()
    return opcion

def Obteneráreadeltriangulo(base, altura):
    area=(base*altura)/2
    return area

def Obteneráreadelcuadrado(lado):
    return lado**2

def Obteneráreadelrectangulo(base, altura):
    return base*altura

def Obteneráreadelcirculo(radio):
    return math.pi*radio**2

#área de interacción con el usuario
print("Semana No. 15: Ejercicio 1")
match(menu()):
    case "a":
        print("El área del traingulo es: ",Obteneráreadeltriangulo(float(input("Ingrese la base del triángulo: "),float(input("Ingrese la altura del triángulo: ")))))
    case "b":
        print("El área del cuadrado es: ",Obteneráreadelcuadrado(float(input("Ingrese el lado del cuadrado: "))))
    case "c":
        print("El área del rectangulo es: ",Obteneráreadelrectangulo(float(input("Ingrese la base del rectangulo: "),float(input("Ingrese la altura del rectangulo: ")))))
    case "d":
        print("El área del circulo es: ",round(Obteneráreadelcirculo(float(input("Ingrese el radio del circulo: "))),3))