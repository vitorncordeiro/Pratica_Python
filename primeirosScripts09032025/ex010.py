numeroDeTentativas = 0
while True:
    numeroDeTentativas += 1
    palavraSecreta = 'vitor'
    tentativaLetra = input('Insira apenas uma letra que possa compor a palavra secreta: ').lower()
    if len(tentativaLetra) > 1 and tentativaLetra != palavraSecreta:
        print('Insira apenas uma letra por vez')
        continue
    elif tentativaLetra == palavraSecreta:
        print(f'acertou em {numeroDeTentativas} tentativas!')
        break

    if tentativaLetra in palavraSecreta:
        if palavraSecreta.count(tentativaLetra) > 1:
            print(f'{tentativaLetra}, aparece {palavraSecreta.count(tentativaLetra)} vezes')
        else:
            print(f'{tentativaLetra}, aparece {palavraSecreta.count(tentativaLetra)} vez')
        

    else:
        print('*')
    
    print(numeroDeTentativas)
    



