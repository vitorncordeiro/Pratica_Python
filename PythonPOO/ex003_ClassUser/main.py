class User:
    def __init__(self, nome, sobrenome, sexo, telefone, email ):
        self.nome = nome
        self.sobrenome = sobrenome
        self.sexo = sexo
        self.telefone = telefone
        self.email = email

    def user_describe(self):
        return print(f'\nNome: {self.nome}\nSobrenome: {self.sobrenome}\nSexo: {self.sexo}\nTelefone: {self.telefone}\nEmail: {self.email}')
    def user_greeting(self):
        return print(f'Saudações {self.nome, self.sobrenome}!')
u1 = User('Vitor', 'Natal Cordeiro', 'Masculino', '(41) 9999999', 'vitornc31@gmail.com')
u2 = User('Marco', 'Aurelio', 'Masculino', '(51) 89898989', 'marcoAurelio@gmail.com')
u3 = User('Gengis', 'Khan', 'Masculino', '(99) 555666666', 'gengiskhan@gmail.com')
usersList = [u1, u2, u3]
for user in usersList:
    user.user_greeting()
    user.user_describe()


