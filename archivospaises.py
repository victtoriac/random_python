# Escribir un programa que lea un archivo de texto conteniendo un conjunto de
# apellidos y nombres en formato "Apellido, Nombre" y guarde en el archivo
# ARMENIA.TXT los nombres de aquellas personas cuyo apellido terminan con la
# cadena "IAN", en el archivo ITALIA.TXT los terminados en "INI" y en el archivo
# ESPAÑA.TXT los terminados en "EZ". Descartar el resto. Ejemplo:
# Arslanian, Gustavo –> ARMENIA.TXT
# Rossini, Giuseppe –> ITALIA.TXT
# Pérez, Juan –> ESPAÑA.TXT
# Smith, John –> descartar
# El archivo de entrada puede ser creado mediante el Block de Notas o el IDLE. No
# escribir un programa para generarlo.


def LeerArch():
    arch=None
    try:
        arch=open("apellidos.txt","rt")
        arch1=open("armenia.txt","wt")
        arch2=open("italia.txt","wt")
        arch3=open("españa.txt","wt")
        linea=arch.readline()
        while linea:
            linea=linea.replace("\n","")

            if linea.upper().find("IAN,")!=-1:
                arch1.write(linea.title()+"\n")
            elif linea.upper().find("INI,")!=-1:
                arch2.write(linea.title()+"\n")
            elif linea.upper().find("EZ,")!=-1:
                arch3.write(linea.title()+"\n")
            else:
                print("Descatar-->",linea)                
            linea=arch.readline()
    except IOError:
        print("No se puede crear el archivo")
    finally:
        try:            
            arch.close()
            arch1.close()
            arch2.close()
            arch3.close()
        except:
            pass


def main():
    LeerArch()
main()