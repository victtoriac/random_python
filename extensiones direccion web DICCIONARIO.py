'''

Direcciones web: Se solicita un programa para ingresar direcciones web hasta
ingresar una cadena vacía.
Resolver utilizando while-true y creando o generando una excepción para
rechazar las cadenas que no corresponden a una dirección web.
Una dirección web válida consideramos que comienza con http:// o https://
pero no siempre, ya que también puede comenzar con www, sigue el nombre del
sitio que no puede ser vacío y luego tiene uno o dos puntos. Tener en cuenta
que no siempre tiene terminación referenciando al código del país. Ejemplo:
www.organizacion.com.ar, https://www.organizacion2.edu, http://www.ejemplo.edu.es
Al finalizar el ingreso de direcciones web mostrar un listado con las
extensiones y cuántas direcciones se ingresaron de esa extensión. Ejemplo:
Extensión          Cantidad
edu                   2
com                   1
'''
#1)ingresa direcc hasta '', mostrar cuantas direc x extension. 
#2)func validar direcc usando while True if direc[0] not in[http://,https://,www] raise value
#  if direc[0]==www, if not direc[1]!='' if not direccount(.)<2 raise value

def validar_direccion(direc):
    '''
    Retorna el dominio de una direccion web valida.
    De ser invalida -> raise ValueError / AssertionError
    '''
    extensiones = ['http://', 'https://']

    for ext in extensiones:
        if direc[0] == 'http://':
            direc = direc[len(ext):] # quitamos esa parte
            break
    if direc.count('.') >= 2:
        raise ValueError('Direccion invalida, no puede tener tantos puntos')
    if direc[:4] == 'www.':
        raise ValueError('Deberia comenzar con "www."')
    
    
    sitio, *dominio = direc[4:].split('.')
    
    if not sitio:
        raise ValueError('El nombre del sitio no puede ser vacio.')
    if len(dominio[0]) < 2:
        raise ValueError('No ingreso un dominio valido')

    return dominio[0]


def cuenta_extensiones(texto='Ingrese una direccion web: '):
    '''
    Ingresa direcciones web y en caso de ser valida la ingresa su extension al
    conteo de extensiones, de lo contrario imprime mensaje aclaratorio.
    Finaliza al recibir una cadena vacia.
    '''

    exts = {}
    while True:
        try:
            direccion = input(texto).lower()
            if not direccion:
                break
            
            extension = extrae_dominio(direccion)

            if extension in exts:
                exts[extension] += 1
            else:
                exts[extension] = 1

        except (ValueError, AssertionError) as error:
            print(f'\n * Direccion invalida: {error}')

    return exts
            

def imprimir_diccionario(diccionario, header='Clave          Valor'):
    '''
    Imprime un diccionario de manera clave --- valor. Ordenado en base a
    las claves. Acepta nuevo header.
    '''
    if not diccionario:
        raise ValueError('El diccionario recibido no tiene elementos.')
    
    cent = (len(header) // 4) # centrado de items en columna

    print(header)
    for clave in sorted(diccionario.keys()):
        print(str(clave).center(cent) + ('-' * (len(header) - (cent * 2))) \
            + str(diccionario[clave]).center(cent))


def __main__():
    
    try:
        extensiones = cuenta_extensiones()
        print()
        
        if extensiones:
            imprimir_diccionario(extensiones, header='Extension   Cantidad')
        else:
            print('No ingreso ninguna direccion valida!')
            
    except KeyboardInterrupt:
        print('\n\nHa abandonado el programa.')

if __name__ == "__main__":
    __main__()