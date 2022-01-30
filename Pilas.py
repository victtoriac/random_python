# Pila Estatica
class PilaEstatica:
    __arr = None
    __inx = 0
        
    def inicializar_pila(self):
        self.__arr = [0]*100
        self.__inx = 0
    
    def apilar(self, dato):
        self.__arr[self.__inx] = dato
        self.__inx += 1
        
    def desapilar(self):
        self.__inx -= 1
    
    def tope(self):
        return self.__arr[self.__inx-1]
    
    def pila_vacia(self):
        return self.__inx == 0

# Pila Dinámica
class PilaDinamica:
    class Nodo:
        info = None
        sig = None
        
    __primero = None
        
    def inicializar_pila(self):
        """ inicializa la pila, dejandola vacía """
        self.__primero = None
    
    def apilar(self, dato):
        """ agrega un elemento al tope de la pila """
        nuevo = self.Nodo()
        nuevo.valor = dato
        nuevo.sig = self.__primero
        self.__primero = nuevo
        
    def desapilar(self):
        """ remueve el elemento al tope de la pila """
        self.__primero = self.__primero.sig
    
    def tope(self):
        """ verifica si la pila esta vacía """
        return self.__primero.valor
    
    def pila_vacia(self):
        """ devuelve el valor del primer elemento de la cola """
        return self.__primero == None