#funcion recursiva sumar todos los valores de una lista.
# return suma

def sumaRec(lista, i=0):
    
    if i == len(lista):
        return 0
    else:
        return lista[i] + sumaRec(lista, i+1)


lista=[10,2,23]
suma= sumaRec(lista)
print("La suma es:", suma)