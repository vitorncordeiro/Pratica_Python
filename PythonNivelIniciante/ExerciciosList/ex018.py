from pathlib import Path
caminho = Path(__file__).parent / 'save.txt'

jogadoresEVotos = []
contadorDeVotos = 0
while True:
    
    numeroEscolhido = input("Número do jogador (0=fim): ")
    if numeroEscolhido.isnumeric() == False:
        print('Informe um número ')
    else:
        numeroEscolhido = int(numeroEscolhido)
        if numeroEscolhido > 23 or numeroEscolhido < 0:
            print("Informe um valor entre 1 e 23 ou 0 para sair!")

    for i in range(1, 24): #criando lista com 23 jogadores
        jogadoresEVotos.append([f'Jogador nº {i}', 0])
    if numeroEscolhido == 0:
        
        print(f'\nResultado da votação:')
        break
    jogadoresEVotos[numeroEscolhido - 1][1] += 1 #somando 1 ponto pro jogador votado
    contadorDeVotos += 1

    
jogadoresVotados = []
for parValores in jogadoresEVotos:
    if parValores[1] > 0:
        jogadoresVotados.append(parValores)
jogadoresVotados.sort(reverse=True, key=lambda a: a[1])
msgFormatada = f"Foram computados {contadorDeVotos} votos.\n\nJogador:        Votos:        %"

def calcularPercentual(nvotos, TotalVotos):
    resultado = nvotos/TotalVotos*100
    return resultado
for jogador in jogadoresVotados:
    msgFormatada = msgFormatada + f"\n{jogador[0]}        {jogador[1]}        {calcularPercentual(jogador[1], contadorDeVotos):.2f}"
jogadorMaisVotado = max(jogadoresVotados, key=lambda a: a[1])    
msgFinal = f"{msgFormatada}\nO melhor jogador foi o {jogadorMaisVotado[0]}, com "\
        f"{jogadorMaisVotado[1]} votos, correspondendo a {calcularPercentual(jogadorMaisVotado[1], contadorDeVotos):.2f}% do total de votos"
print(msgFinal)

with open(caminho, 'w+', encoding='UTF-8') as arquivo:
    arquivo.write(msgFinal)
        
