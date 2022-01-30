def crear_matriz(n):
    matriz=[]
    for f in range (n):
        matriz.append([" "]*(n+2*(n//2)))
    return matriz

def cargar_matriz(n,matriz):
    col=(n+2*(n//2))//2
    print(col)
    for i in range(n-1):
        matriz[i][col+i]="*"
        matriz[i][col-i]="*"
    for g in range (n+2*(n//2)):
        matriz[n-1][g]="*"
    
    return matriz
        

def imprimir_matriz(n,matriz):
    for f in range(n):
        for c in range(n+2*(n//2)):
            print(matriz[f][c],end="")
        print ( )

#Programa principal
n=int(input("Ingrese un numero entero impar mayor a 2: "))
while n < 2 or n %2==0:
    print("Incorrecto. Reingrese el numero.")
    n=int(input("Ingrese un numero: "))
matriz=crear_matriz(n)
matriz=cargar_matriz(n,matriz)
imprimir_matriz(n,matriz)  
