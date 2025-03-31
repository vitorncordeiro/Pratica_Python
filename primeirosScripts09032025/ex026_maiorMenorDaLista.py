setValores = set()
while True:
    perguntaInicial = input('Deseja inserir um valor? [S] [N]\n').upper()
    if perguntaInicial.startswith('S'):
        valor = int(input('Digite um valor: '))
        setValores.add(valor)
    elif perguntaInicial.startswith('N'):
        break
    else:
        print('Selecione uma opção válida!')
        continue
totalCrescente = sorted(list(setValores))
print(f'MAIOR: {max(setValores)}\nMENOR: {min(setValores)}\nTOTAL: {totalCrescente}')
