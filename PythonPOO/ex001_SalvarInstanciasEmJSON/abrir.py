import json

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

caminho = 'ex001_SalvarInstanciasEmJSON\\save.json'
with open(caminho, 'r+') as arq:
    listaDePessoas = json.load(arq)
    p1 = Pessoa(**listaDePessoas[0])
    p2 = Pessoa(**listaDePessoas[1])
    p3 = Pessoa(**listaDePessoas[2])
    print(p1.nome, p2.nome, p3.nome)


