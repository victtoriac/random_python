#funcion recursiva sumar todos los valores de una lista.
# return suma

def sumaRec(lista, suma=0, i=0):
    
    if i == len(lista):
        return suma
    else:
        suma = suma + lista[i]
        sumaRec(lista, suma, i+1)


lista=[10,2,23]
suma= sumaRec(lista)
print("La suma es:", suma)