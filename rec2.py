def mostrarNroRec(i=1):
    if i<=3:
        print(i)
        mostrarNroRec(i+1)


mostrarNroRec()