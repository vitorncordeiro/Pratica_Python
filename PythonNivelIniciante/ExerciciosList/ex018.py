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
for par in jogadores_e_votos:
    if par[1] > 0:
        jogadores_votados.append(par)
#falta formatar a mensagem pra ficar igual no código exemplo
msgFormatada = f"Foram registrados {contadorDeVotos} votos.\n"
    
        

