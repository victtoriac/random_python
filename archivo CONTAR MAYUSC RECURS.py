'''

Leer las frases del archivo frases.txt y crear un nuevo archivo con las frases
seguido de dos puntos (:) y la cantidad de letras mayúsculas que posee. Contar
las letras mayúsculas de una cadena mediante una función recursiva.
'''

def contarmayusc(texto):
    if len(texto)==0:
        return 0
    else:
        mayusc=texto[0]
        if mayusc.isupper():
            return 1+contarmayusc(texto[1:])
        else:
            return 0+contarmayusc(texto[1:])
        
try:
    entrada=open("frases.txt","r")
    salida=open("nuevofrases.txt","w")
    for frase in entrada:
        frase=frase.rstrip()
        mayusc=contarmayusc(frase)
        salida.write(frase+f':{mayusc}\n')
except IOError:
    print('Ocurrio un error al abrir los archivos.')
except Exception as error:
    print(f'Ocurrio un error inesperado {error}')
    
finally:
    try:
        entrada.close()
        salida.close()
    except:
        pass