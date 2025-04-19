from main import viagens
nomeCompleto = input('Digite seu nome: ').split()
nome = nomeCompleto.pop(0)
sobrenome = ''

for i in nomeCompleto:
    sobrenome = sobrenome + ' ' + i

class User:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    def mostrarUser(self):
        print(f'Nome: {self.nome} | Sobrenome: {self.sobrenome}')
    def mostrarViagens(self):
        print('As viagens disponíveis e seus preços são, respectivamente: ')
        for posicao, valor in enumerate(viagens):
            for chave, valorDict in valor.items():
                print(f"Viagem Nº[{posicao+1}] | Destino: {chave} | Preço: {valorDict}")
    def escolherViagem(self):
        self.mostrarViagens()
        numeroViagem = int(input('Informe o número da viagem escolhida: ')) - 1
        viagemEscolhida = viagens[numeroViagem]
        for chave, valorDict in viagemEscolhida.items():
            print(f"Destino Escolhido: {chave} | Preço da viagem escolhida: {valorDict}")
u1 = User(nome, sobrenome)

while True:
    comando = input('Digite um comando: [S]air [M]ostrar Viagens [E]scolher viagem [I]nformações do Usuário\n').upper()
    if comando.startswith('S'):
        print('Saindo...')
        break
    elif comando.startswith('M'):
        u1.mostrarViagens()
    elif comando.startswith('E'):
        u1.escolherViagem()
    elif comando.startswith('I'):
        u1.mostrarUser()
    else:
        print('Digite um comando válido')
    
    