def extrae_dominio(direccion):
    '''
    Retorna el dominio de una direccion web valida.
    De ser invalida -> raise ValueError / AssertionError
    '''
    protocolos = ['http://', 'https://']

    for prot in protocolos:
        if direccion[:len(prot)] == prot:
            direccion = direccion[len(prot):] # quitamos esa parte
            break
    assert (direccion.count('.') >= 2), 'No ingreso una direccion con formato valido.'
    assert (direccion[:4] == 'www.'), 'La direccion no comienza con "www."'
    
    sitio,*dominio = direccion[4:].split('.')
   
    
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