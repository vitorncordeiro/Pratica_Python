class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, open=False):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.open = open
        self.clientesAtuais = 0
    def open_restaurant(self): 
        if self.open:
            print('Já está aberto')
            return
        print(f'Abrindo o restaurante {self.restaurant_name}\n')
        self.open = True
    def describe_restaurante(self):
        if self.open == True:
            status = 'Aberto'
        else:
            status = 'Fechado'
        return print(f'Nome do restaurante: {self.restaurant_name}\nTipo do restaurante: {self.cuisine_type}\nStatus: {status}')
    
    def show_number_served(self):
        print(f'Número de clientes sendo atendidos em {self.restaurant_name}: {self.clientesAtuais}')
    def increment_number_served(self, numberAcc):
        self.clientesAtuais = self.clientesAtuais + numberAcc
        print(f'Número de clientes sendo atendidos em {self.restaurant_name}: {self.clientesAtuais}')
    def decrement_number_served(self, numberDec):
        if numberDec <= self.clientesAtuais:
            self.clientesAtuais = self.clientesAtuais - numberDec
            self.show_number_served()
        else:
            raise Exception
    

Madero = Restaurant('Madero', 'Hamburgueria')
Kikuti = Restaurant('Kikuti', 'Japonês')
OneHundredBeer = Restaurant('100Bear', 'Bar e Pizzaria')
listaRestaurantes = [Madero, Kikuti, OneHundredBeer]

for restaurante in listaRestaurantes:
    restaurante.open_restaurant()
    restaurante.describe_restaurante()
    print() 


Madero.increment_number_served(100)
print('###########################')
Madero.increment_number_served(400)
print('###########################')
Madero.decrement_number_served(50)
