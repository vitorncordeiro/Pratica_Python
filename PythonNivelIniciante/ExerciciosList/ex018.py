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

    for i in range(1, 24):
        jogadores_e_votos.append([f'Jogador nº {i}', 0])

    jogadores_e_votos[numeroEscolhido - 1][1] + 1
    contadorDeVotos += 1

    if numeroEscolhido == 0:
        
        print(f'\nResultado da votação:\n {jogadores_votados}')
        break
jogadores_votados = []
for lista in jogadores_e_votos:
    if lista[1] > 0:
        for i in range(len(jogadores_e_votos)):
            jogadores_votados.append(jogadores_e_votos[i])
    
    
    
        

