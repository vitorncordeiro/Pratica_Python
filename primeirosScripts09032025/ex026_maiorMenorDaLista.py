listaValores = []
while True:
    perguntaInicial = input('Deseja inserir um valor? [S] [N]\n').upper()
    if perguntaInicial.startswith('S'):
        valor = int(input('Digite um valor: '))
        listaValores.append(valor)
    elif perguntaInicial.startswith('N'):
        break
    else:
        print('Selecione uma opção válida!')
        continue
        
print(f'MAIOR: {max(listaValores)}\nMENOR: {min(listaValores)}')