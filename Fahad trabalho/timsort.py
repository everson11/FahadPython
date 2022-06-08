def timSort(lista):
    for i in range(len(lista)):
        for j in range(i):
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista