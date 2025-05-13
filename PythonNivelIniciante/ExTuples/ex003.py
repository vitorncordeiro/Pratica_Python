"""
Criar um programa que cadastre locais históricos do mundo com
suas coordenadas fazendo uso de tuplas com parâmetros
nomeados. Dica: usar a função namedtuple().

"""
def namedtuple(nome, coordenada):
    tupla = (nome, coordenada)
    return tupla
while True:
    print('Digite Q para sair!')
    nome = input('Digite o nome do local histórico: ')
    if nome == "Q":
        break
    coordenadas = int(input('Digite as coordenadas do local histórico: '))
    print(namedtuple(nome, coordenadas))
    print("----------------------------")


    