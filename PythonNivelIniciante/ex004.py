nomeUser = input('Digite seu nome: ')
idadeUser = input('Digite sua idade: ')


if (nomeUser and idadeUser) and idadeUser.isdigit():
    ultimaLetra = nomeUser[len(nomeUser) - 1]
    primeiraLetra = nomeUser[0]
    nomeInvertido = nomeUser[-1: - len(nomeUser) - 1:-1]
    print(f'Seu nome é: {nomeUser}')
    print(f'Seu nome invertido é: {nomeInvertido}')
    if " " in nomeUser:
        print(f"Seu nome contém espaço")
    else:
        print(f'Seu nome não contém nenhum espaço')
    print(f'Seu nome possui {len(nomeUser)} letras')
    print(f'A primeira letra do seu nome é {primeiraLetra}')
    print(f'A última letra do seu nome é {ultimaLetra}')
elif nomeUser == False or idadeUser == False:
    print('Desculpe, parece que você deixou um dos campos vazios, tente novamente')
else:
    print('Desculpe, parece que você não informou um número como sua idade, tente novamente')

        

