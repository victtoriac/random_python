  
'''
Desarrollar un programa principal para ingresar dos palabras por teclado e
informar las letras poseen en común. Permitir ingresar varias veces dos
palabras hasta que la primera que se ingrese sea vacía. Para el ingreso de
palabras, generar y gestionar una excepcion si se ingresan numeros, espacios
o símbolos, aceptar solo palabras con caractgeres alfabeticos.
'''



letrasencomun=lambda cad1,cad2: list(set(cad1.lower()) & set(cad2.lower()))
'devuelve lista con las letras en comun entre dos cadenas'


def ingresarpalabra(texto):
    'valida solo letras'
    while True:
        try:
            palabra=input(texto)
            for letra in palabra:
                if letra.isdigit():
                    raise ValueError('no se permiten digitos')
                elif not letra.isalpha():
                    raise ValueError('no se permiten simbolos')
            break
        except ValueError as error:
            print(f' \n palabra invalida {error}')
    
    return palabra

#programa
def __main__():
    while True:
        try:
            palabra1=ingresarpalabra("ingrese primera palabra: ")
            if not palabra1:
                raise KeyboardInterrupt
            palabra2=ingresarpalabra("ingrese segunda palabra: ")
            encomun=letrasencomun(palabra1,palabra2)
            if encomun:
                print(f"Las letras comunes entre {palabra1} y {palabra2} son: {', '.join(encomun)}")
            else:
                print('Las palabras no comparten ninguna letra')
        except KeyboardInterrupt:
            print('abandono programa')
            break
if __name__ == "__main__":
    __main__()
            

                
            
            
        
    