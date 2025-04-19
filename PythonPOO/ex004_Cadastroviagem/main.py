#Fazer um cadastro de viagem (Deve pedir o nome do viajante, dar as opções de destino e imprimir a selecionada)
from listaviagens import viagens
nomeCompleto = input('Digite seu nome: ').split()
nome = nomeCompleto.pop(0)
sobrenome = ''
for i in nomeCompleto:
    sobrenome = sobrenome + ' ' + i
print(f'{nome}{sobrenome}')

class User:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

class Viagem:
    def __init__(self, destino, preco):
        self.destino = destino
        self.preco = preco
    def escolherViagem(self):
        ...
def fazerInstancia(**dict):
    tupla = tuple(dict.items())
    instancia = Viagem(tupla[0][0], tupla[0][1])
    return instancia
viagem1 = fazerInstancia(**viagens[0])
viagem2 = fazerInstancia(**viagens[1])
viagem3 = fazerInstancia(**viagens[2])




 