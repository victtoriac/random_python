# 
# Se solicita leer el archivo de alumnos con el formato:
# legajo;nombre;nota1;nota2\n
# y crear un diccionario indicando cantidad de alumnos segun condicion de cursada
# (aprueba, recupera primero, recupera segundo, a final, promciona) segun el régimen de UADE. 
# Mostrar ordenado por cantidad de alumnos de mayor a menor.
# aprueba: son los alumnos con ambos parciales aprobados

def sumaCondicion(dic, nota1, nota2):
    if nota1>=7 and nota2>=7:
        dic['promociona']+=1
        dic['aprueba']+=1
    elif nota1>=4 and nota2>=4:
        dic['a final']+=1
        dic['aprueba']+=1
    else:
        if nota1<4:
            dic['recupera primero']+=1
        if nota2<4:
            dic['recupera segundo']+=1

try:
    arch=open("alumnos.txt", "r")
except OSError:
    print("no se puede crear-abrir archivo")
else:
    dic={'aprueba':0,'recupera primero':0,'recupera segundo':0,'a final':0,'promociona':0}
    for registro in arch:
        campos=registro.split(";")
        sumaCondicion(dic, int(campos[2]), int(campos[3]))
    
    for clave, valor in sorted(dic.items(), key=lambda valor: valor[1], reverse=True):
        print(clave, valor)
        
finally:
    try:
        arch.close()
    except:
        pass