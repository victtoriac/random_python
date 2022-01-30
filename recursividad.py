def contarvocales(palabra, diccVoc=None):
    mapVocales = {"a":"a", "e":"e", "i":"i", "o":"o", "u":"u", "ü":"u", "á":"a", "é":"e", "í":"i", "ó":"o", "ú":"u"}    
    if diccVoc == None:
        diccVoc = {}
    if len(palabra) == 0:
        return diccVoc
    else:
        letra = palabra[0].lower()
        if letra in mapVocales:
            if mapVocales[letra] in diccVoc:
                diccVoc[mapVocales[letra]] += 1
            else:
                diccVoc[mapVocales[letra]] = 1
        
        return contarvocales(palabra[1:], diccVoc)