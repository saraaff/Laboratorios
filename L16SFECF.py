import random
print("Semana 16: ejercicio uno")
A=[]
for i in range(10):
    r=random.randint(1,100)
    A.append(r)
prom=0
for num in A:
    prom+=num
prom=prom/len(A)
print(A)
print(len(A))
print("El promedio es:", prom)

sumapar=0
sumaimpar=0
for i in range(len(A)):
    if i%2==0:
        sumapar+=A[i]
    else:
        sumaimpar+=A[i]
print("La suma par es:", sumapar)
print("La suma impar es:", sumaimpar)

print("\n Semana 16: ejericio dos")
filas=int(input("Ingrese la cantidad de filas: "))
columnas=int(input("Ingrese la cantidad de columnas: "))
B=[[]]
for i in range (filas):
    temporal=[]
    for j in range (columnas):
        r=random.randint(0,1001)
        temporal.append(r)
    B.append(temporal)

def mayor(arreglo):
    mayor=arreglo[0][0]
    for i in range(len(arreglo)):
        for j in range(len(arreglo[i])):
            if arreglo [i][j]>mayor:
                mayor=arreglo[i][j]
    return mayor

def menor(arreglo):
    menor=arreglo[0][0]
    for i in range(len(arreglo)):
        for j in range(len(arreglo[i])):
            if arreglo [i][j]<menor:
                menor=arreglo[i][j]
    return menor

def pares(arreglo):
    pares=arreglo[0][0]
    for i in range(len(arreglo)):
        for j in range(len(arreglo[i])):
            if arreglo[i][j]%2==0:
                pares+=1
    return pares

def impares(arreglo):
    impares=arreglo[0][0]
    for i in range(len(arreglo)):
        for j in range(len(arreglo[i])):
            if arreglo[i][j]%2!=0:
                impares+=1
    return impares

print(B)
print("El numero mayor es: ", mayor(B))
print("El numero menor es: ", menor(B))
print("cantidad de numeros pares: ", pares(B))
print("cantidad de numeros impares: ", impares(B))