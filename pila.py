#cree e inicializ pila
import random
from metodos import apilar,mostrarpila
def inicializarpila():
    '''permite inic la estructura de la pila'''
    pila=[]
    return pila
pila=inicializarpila()

#cargue pila con valores aleatorios
for i in range(10):
    dato=random.randint(1,10)
    apilar(pila,dato)
    
#muestre pila
mostrarpila(pila)
print()

#invierta los elementos de la pila
pilainvertida=inicilizarpila()
while not pilavacia(pila):
    apilar(pilainvertida,tope(pila))
    desapilar(pila)
#muestre pila
mostrarpila(pilainvertida)
print()