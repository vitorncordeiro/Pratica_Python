from contas import ContaCorrente, ContaPoupanca, listaContas
from users import Cliente, listaClientes
class Banco:
    def __init__(self, agencias, contas, clientes):
        self.agencias = agencias or []
        self.contas = contas or [] 
        self.clientes = clientes or []
    def autenticar_agencia(self, conta):
        if (conta.agencia in self.agencias):    
            print('A agência é desse banco')
            return True
        else:
             print('A agência não é desse banco')
             return False
    def autenticar_cliente(self, cliente):
        if cliente in self.clientes:
            print('O cliente é desse banco')
            return True
        else:
            print('O cliente não é desse banco')
            return False
    def autenticar_conta(self, conta):
        if conta in self.contas:
            print('A conta é desse banco')
            return True
        else:
            print('A conta não é desse banco')
            return False
listaAgencias = [43210, 98765, 13579, 02468, 02468]
if __name__ == '__main__':
    itau = Banco(listaAgencias, listaContas, listaClientes)
    for conta in listaContas:
        itau.autenticar_conta(conta)
        itau.autenticar_agencia(conta)
    
    for cliente in listaClientes:
    
        itau.autenticar_cliente(cliente)
    
