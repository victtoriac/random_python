  
'''
Contraseñas! En general las contraseñas a crear deben cumplir reglas por
seguridad para que sean válidas. Desarrolle un programa que ingrese
contraseñas hasta ingresar una contraseña vacía. A medida que se ingresan
verifique e informe si cumple con las reglas:
    a. No puede comenzar con número.
    b. Debe contener al menos dos números. Contar la cantidad de numeros
      de una cadena mediante una función recursiva.
Resolver utilizando exclusivamente manejo de excepciones y estructura While-True,
creando una nueva excepción o generando una existente (ValueError) cuando no
cumpla alguno de las dos reglas, mostrar mensaje aclaratorio correspondiente en
cada caso
'''

#1)ingresar contras hasta !=''
#2)if contra[0].isdigit() raise valueerror, dig=contardig(contra), if dig<2 raise valueerror. FUNCION VALIDACION CONTRA
#3)funcion contar dig de una cadena RECURSIVA

def contardig(contra,i=0):
    numero=int(contra[i].isdigit())
    if len(contra[i:])==1:
        return numero
    else:
        return numero+contardig(contra,i+1)
    
    


def validarcontra(contra):
    if contra[0].isdigit():
        raise ValueError("no puede empezar con numeros")
    if contardig(contra)<2:
        raise ValueError("debe tener min dos numeros")       

#PROGRAMA
while True:
    try:
        contra=input("ingrese contra: ")
        if contra=='':
            print("abandono el programa")
            raise KeyboardInterrupt

        validarcontra(contra)
        print("contrasena ok")
    except ValueError as error:
        print(f'ERROR! {error}')
    except KeyboardInterrupt:
        break

    

        
    
    