class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self._motor = None 
        self._fabricante = None
    @property
    def motor(self):
        return self._motor 
    @motor.setter
    def motor(self, valor):
        self._motor = valor
    @property
    def fabricante(self):
        return self._fabricante 
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor
class Motor:
    def __init__(self, nomeMotor):
        self.nomeMotor = nomeMotor

class Fabricante:
    def __init__(self, nome):
        self.nomeFabricante = nome
palio = Carro('Palio')
fiat = Fabricante('Fiat')
motor = Motor('1.8R')
palio.motor = motor
palio.fabricante = fiat
print(palio.modelo, palio.motor.nomeMotor, palio.fabricante.nomeFabricante)

Picasso = Carro('Picasso')
citroen = Fabricante('Citroen')
motorPicasso = Motor('2.0')
Picasso.fabricante = citroen
Picasso.motor = motorPicasso
print(Picasso.modelo, Picasso.motor.nomeMotor,Picasso.fabricante.nomeFabricante )