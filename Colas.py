# Cola Estatica
class ColaEstatica:
    __arr = None
    __inx = 0
    
    def inicializar_cola(self):
        self.__arr = [0] * 100
        self.__inx = 0
    
    def acolar(self, dato):
        self.__arr[self.__inx] = dato
        self.__inx += 1
    
    def desacolar(self):
        for i in range(self.__inx-1):
            self.__arr[i] = self.__arr[i+1]
        self.__inx -= 1
        
    def cola_vacia(self):
        return self.__inx == 0
    
    def primero(self):
        return self.__arr[0]

# Cola Dinámica
class ColaDinamica:
    class Nodo:
        info = None
        sig = None
        
    __primerNodo = None
    __ultimo = None
    
    def inicializar_cola(self):
        """ inicializa la cola, dejandola vacía """
        self.__primerNodo = None
        self.__ultimo = None
    
    def acolar(self, dato):
        """ agrega un elemento al final de la cola """
        nuevo = self.Nodo()
        nuevo.info = dato
        nuevo.sig = None
        if self.__ultimo != None: self.__ultimo.sig = nuevo
        self.__ultimo = nuevo
        if self.__primerNodo == None: self.__primerNodo = self.__ultimo
    
    def desacolar(self):
        """ remueve el primer elemento de la cola """
        self.__primerNodo = self.__primerNodo.sig
        if self.__primerNodo == None: self.__ultimo = None
        
    def cola_vacia(self):
        """ verifica si la cola esta vacía """
        return self.__ultimo == None
    
    def primero(self):
        """ devuelve el valor del primer elemento de la cola """
        return self.__primerNodo.info