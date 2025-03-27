numero_input = input('Digite um número inteiro: ')

if numero_input.isdigit():
    numeroIntFormatado = int(numero_input)
    if numeroIntFormatado % 2 == 0:
        print('O número informado é par')
    else:
        print('O número informado não é par')
else:
    print('O valor informado não é um número inteiro, por favor tente novamente')
