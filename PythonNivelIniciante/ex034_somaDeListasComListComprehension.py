#tem q somar
lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [1, 2, 3, 4, 5, 6, 7]
listaSomado = [x + y for x, y in list(zip(lista1, lista2))]
print(listaSomado)