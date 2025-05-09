while True:
    jogadores_e_votos = [[f'Jogador número {i}' for i in range(1, 24)]]
    numeroEscolhido = input("Digite o número da camiseta do jogador que deseja votar: ")
    if numeroEscolhido == "0":
        print('Encerrando...')
        break
    elif numeroEscolhido.isnumeric() == False:
        print('Informe um número ')
    else:
        numeroEscolhido = int(numeroEscolhido)
        if numeroEscolhido > 23 or numeroEscolhido < 0:
            print("Informe um valor entre 1 e 23 ou 0 para sair!")
    jogadores_e_votos[numeroEscolhido]
    
    
        

