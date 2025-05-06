nomeUser = input('Escreva seu nome: ')
comprimentoNomeUser = len(nomeUser)
if comprimentoNomeUser <= 4:
    print('Seu nome é curto')
elif comprimentoNomeUser > 4 and comprimentoNomeUser <= 6:
    print('Seu nome é normal')
elif comprimentoNomeUser > 6:
    print('Seu nome é muito grande')
