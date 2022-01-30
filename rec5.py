#funcion recursiva sumar todos los valores de una lista.
# return suma

def sumaRec(lista):
    
    if len(lista)==0:
        return 0
    else:
        return lista[0] + sumaRec(lista[1:])


lista=[10,2,23]
suma= sumaRec(lista)
print("La suma es:", suma)