from abc import ABC, abstractmethod
class Eletrodomestico:
    def __init__(self, nome, ligado=False):
        self._nome = nome
        self.ligado = ligado
    @property
    def nome(self):
        return self._nome
    @abstractmethod
    def ligar(self):
        self.ligado = True
class InterfaceUSB:
    def __init__(self, conectarUSB=False):
        self.conectarUSB = conectarUSB
    @abstractmethod
    def conectar(self):
        self.conectarUSB = True
class SmartSpeaker(Eletrodomestico, InterfaceUSB):
    def __init__(self, nome):
        super().__init__(nome)
    def ligar(self):
        self.ligado = True
        print('Objeto ligado')
    def conectar(self):
        self.conectarUSB = True
        print('USB conectado')
Alexa = SmartSpeaker('Alexa')
print(Alexa.nome)
JBL = SmartSpeaker('JBL')
print(JBL.nome)
Alexa.ligar()
Alexa.conectar()
