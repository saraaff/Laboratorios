print("Semana 10: ejercicio 1")

mes=int(input("Ingrese un número entre 1 y 12: "))

if mes<1 or mes>12:
    print("Error: El número a ingresar debe ser entre 1 y 12: ")
else: 
   if mes==1:
       print("Mes: Enero")
    elif mes==2: 
       print("Mes: Febrero")
    
     

match(mes):
    case 1:
        print("Mes: Enero")
    case 2:
        print("Mes: Febrero")
    case 3:
        print("Mes: Marzo")


print("Semana 10: ejercicio 2")
