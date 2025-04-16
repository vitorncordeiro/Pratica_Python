import json

arqPath = 'ex001_SalvarInstanciasEmJSON\\save.json'

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome 
        self.sobrenome = sobrenome

pessoa1 = Pessoa('Vitor', 'Natal Cordeiro')
pessoa2 = Pessoa('Suellen', 'Martins')
pessoa3 = Pessoa('Ivy', 'Rafaelo')
listaPessoas = [pessoa1.__dict__, pessoa2.__dict__, pessoa3.__dict__]

def salvar():
    with open(arqPath, 'r+') as arquivo:
        json.dump(listaPessoas, arquivo)
salvar()