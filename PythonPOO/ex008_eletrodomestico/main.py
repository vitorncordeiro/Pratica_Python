from abc import ABC, abstractmethod
class Eletrodomestico:
    def __init__(self, nome, ligado=False):
        self._nome = nome
        self.ligado = ligado
        self.interfaceTomada = None
    @property
    def nome(self):
        return self._nome
    @abstractmethod
    def ligar(self):
        pass
class InterfaceUSB:
    def __init__(self, conectarUSB=False):
        self.conectarUSB = conectarUSB
    @abstractmethod
    def conectar(self):
        self.conectarUSB = True
class IotProduct(Eletrodomestico, InterfaceUSB):
    def __init__(self, nome):
        super().__init__(nome)
    def ligar(self):
        self.ligado = True
        print(f'Objeto {self.nome} ligado')
    def conectar(self):
        self.conectarUSB = True
        print('USB conectado')
    def desconectar(self):
        self.concectarUSB = False
        print('USB desconectado')
class Geladeira(Eletrodomestico):
    def __init__(self, nome):
        super().__init__(nome)
        self.interfaceTomada = False
    def ligar(self):
        self.ligado = True
        print(f'Objeto {self.nome} ligado')
    def conectarTomada(self):
        self.interfaceTomada = True
        print(f'Tomada de {self.nome} conectada')
    def desconectarTomada(self):
        self.interfaceTomada = False
    
Alexa = IotProduct('Alexa')
print(Alexa.nome)
JBL = IotProduct('JBL')
Eletrolux = Geladeira('Eletrolux')
Eletrolux.conectarTomada()
Eletrolux.ligar()
print(JBL.nome)
Alexa.ligar()
Alexa.conectar()
JBL.ligar()
JBL.conectar()
