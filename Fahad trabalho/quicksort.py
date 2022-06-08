def quicksort(lista):
    if len(lista) > 1:
        pivo = lista[0]
        menores = [x for x in lista[1:] if x <= pivo]
        maiores = [x for x in lista[1:] if x > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)
    return lista

lista = [54,26,93,17,77,31,44,55,20]
print(quicksort(lista))