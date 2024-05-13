print("Semana No. 11: ejercicio uno")
N=0
while N<=0:
    N=int(input("Ingrese un numero mayor que 0: "))
    print()
    if N<=0: 
        print("El valor ingresado debe ser mayor a 0")
        print()
#El valor N ha sido leido
A=0
B=1
C=0
i=2
resultado=""
resultado=str(A)
if N>1:
    resultado+=(", "+str(B))
    while i<N:
        C=A+B
        resultado+=(", "+str(C))
        A=B
        B=C
        i=i+1
    print(resultado)
else:
    print(resultado)