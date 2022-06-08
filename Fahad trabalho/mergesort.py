def mergeSort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]
        mergeSort(esquerda)
        mergeSort(direita)
        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1
        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1
        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1
    return lista

