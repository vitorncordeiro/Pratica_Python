# Exercício - Unir listas
 # Crie uma função zipper (como o zipper de roupas)
 # O trabalho dessa função será unir duas
 # listas na ordem.
 # Use todos os valores da menor lista.
 # Ex.:
 # ['Salvador', 'Ubatuba', 'Belo Horizonte']
 # ['BA', 'SP', 'MG', 'RJ']
 # Resultado
 # [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
listaCidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
listaEstados = ['BA', 'SP', 'MG', 'RJ', ]
novalista = []
if len(listaCidades) > len(listaEstados):
    menorlista = listaEstados
    maiorLista = listaCidades
else:
    menorlista = listaCidades
    maiorLista = listaEstados
def zipper():
    for posicao, valor in enumerate(menorlista):
        tupla = (valor, maiorLista[posicao])
        novalista.append(tupla)
    print(novalista)
zipper()
