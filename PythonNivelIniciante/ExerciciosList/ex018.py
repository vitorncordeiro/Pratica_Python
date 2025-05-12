from pathlib import Path
caminho = Path(__file__).parent / 'save.txt'

jogadores_e_votos = []
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
        jogadores_e_votos.append([f'Jogador nº {i}', 0])
    if numeroEscolhido == 0:
        
        print(f'\nResultado da votação:')
        break
    jogadores_e_votos[numeroEscolhido - 1][1] += 1 #somando 1 ponto pro jogador votado
    contadorDeVotos += 1

    
jogadores_votados = []
for parValores in jogadores_e_votos:
    if parValores[1] > 0:
        jogadores_votados.append(parValores)
jogadores_votados.sort(reverse=True, key=lambda a: a[1])
msgFormatada = f"Foram computados {contadorDeVotos} votos.\n\nJogador:        Votos:        %"

def calcularPercentual(nvotos, TotalVotos):
    resultado = nvotos/TotalVotos*100
    return resultado
for jogador in jogadores_votados:
    msgFormatada = msgFormatada + f"\n{jogador[0]}        {jogador[1]}        {calcularPercentual(jogador[1], contadorDeVotos):.2f}"
jogadorMaisVotado = max(jogadores_votados, key=lambda a: a[1])    
msgFinal = f"{msgFormatada}\nO melhor jogador foi o {jogadorMaisVotado[0]}, com "\
        f"{jogadorMaisVotado[1]} votos, correspondendo a {calcularPercentual(jogadorMaisVotado[1], contadorDeVotos):.2f}% do total de votos"
print(msgFinal)

with open(caminho, 'w+', encoding='UTF-8') as arquivo:
    arquivo.write(msgFinal)
        
