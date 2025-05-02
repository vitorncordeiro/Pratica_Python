from contas import ContaCorrente, ContaPoupanca
class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
    def __repr__(self):
        return(f'{type(self).__name__}({self.nome!r}, {self.idade!r})')
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, novoNome):
        self._nome = novoNome
    @property
    def idade(self):
        return self._idade
    @idade.setter
    def idade(self, novaIdade):
        self._idade = novaIdade

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.contaC = None
        self.contaP = None
if __name__ == '__main__':
    p1 = Cliente('Vitor', 18)
    print(p1)
    p1.contaC = ContaCorrente(12345, 54321, 10, 1000)
    print(p1.contaC)
    p1.contaP = ContaPoupanca(56789, 98765, 10)
    print(p1.contaP)
