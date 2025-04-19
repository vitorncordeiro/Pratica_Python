import json
caminho = "E:\\Documentos\\Trabalhos vitor - faculdade\\práticaEmPython\\PythonPOO\\ex004_Cadastroviagem\\listaviagens.json"
with open(caminho, 'r+', encoding='UTF-8') as arquivo:
    viagens = json.load(arquivo)
class Viagem:
    def __init__(self, destino, preco):
        self.destino = destino
        self.preco = preco
    def adicionarViagem(self):
        dicio = {self.destino: self.preco}
        viagens.append(dicio)
if __name__ == '__main__':
    while True:
        comando = input('Digite um comando: [C]adastrar Viagem [S]air\n').upper()
        if comando.startswith('C'):
            destino = input('Digite o destino da viagem: ')
            preco = int(input('Digite o preco da viagem: '))
            viagem1 = Viagem(destino, preco)
            viagem1.adicionarViagem()
        elif comando.startswith('S'):
            break
    with open(caminho, 'r+', encoding='UTF-8') as arquivo:
        viagens = json.dump(viagens, arquivo)





 