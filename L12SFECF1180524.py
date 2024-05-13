print("Semana 12: Ejercicio 1")
print("a. sumatoria")
print("b. Factorial")
print("c. Tablas de multiplicar")
print("d. Número perfecto")

opcion=input("Elija una de las opciones a calcular: ")
match opcion:
    case "a":
        N=0
        while(N<=0):
            N=int(input("Ingrese un numero entero positivo: "))
            if N<=0:
                print("El numero ingresado debe ser mayor a 0")
        sumatoria=0
        for cont in range(1,N+1):
            sumatoria+=cont #sumatoria=sumatoria+cont
            print("La sumatoria es: ", sumatoria)
    case "b":
        N=0
        while(N<=0):
            N=int(input("Ingrese un numero entero positivo: "))
            if N<=0:
                print("El numero ingresado debe ser mayor que 0")
        factorial=1
        for cont in range(1,N+1):
            factorial*=cont
        print("La factorial es: ", factorial)
    case "c":
        for i in range(1,11):
            for j in range(1,11):
                print(i*j, end= '')
            print()
    case "d":
        N=0
        while(N<=0):
            N=int(input("Ingrese un numeto entero positivo: "))
            if N<=0:
                print("El numero ingresado debe ser mayor a 0.")
        sumatoria=0
        for factor in range(1,N):
            if N%factor==0:
                sumatoria+=factor
        if sumatoria==N:
            print("El numero es perfecto")
        else:
            print("El numero no es perfecto")
    case _:
        print("Ingrese una opcion valida")