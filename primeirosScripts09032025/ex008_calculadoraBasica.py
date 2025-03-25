#Pedir 2 numeros e uma operação, executar a operação
while True:
    sair = input('Deseja sair? [S] [N]: ').upper().startswith('S')
    if sair:
        break
    numeroUm = input('Digite o primeiro número: ')
    numeroDois = input('Digite o segundo número: ')
    operacao = input('Digite o operador que deseja utilizar(+-*/): ')
    operacoesvalidas = ["+", "-", "*", "/"]

    if numeroUm.isdigit() and numeroDois.isdigit():  #checa se o usuário digitou números válidos ou letras e retorna no print caso seja alguma letra
        numeroUm = float(numeroUm)
        numeroDois = float(numeroDois)
    else:
        print('Por favor, digite números válidos')
        continue

    if operacao not in operacoesvalidas:
        print('Por favor, digite uma operação válida')
        continue
    
    if operacao == "+":
        resultadoOperacao = numeroUm + numeroDois
        print(f'O resultado da operação é {resultadoOperacao}')
    elif operacao == "-":
        resultadoOperacao = numeroUm - numeroDois
        print(f'O resultado da operação é {resultadoOperacao}')
    elif operacao == "*":
        resultadoOperacao = numeroUm * numeroDois
        print(f'O resultado da operação é {resultadoOperacao}')
    else:
        resultadoOperacao = numeroUm / numeroDois
        print(f'O resultado da operação é {resultadoOperacao}')


