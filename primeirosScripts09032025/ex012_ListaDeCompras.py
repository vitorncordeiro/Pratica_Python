listaDeCompras = []

while True:
    comandoInicializador = input('Selecione uma opção:\n[i]nserir [a]pagar [l]istar [s]air\n')
    if comandoInicializador.startswith('s'):
        print('Você saiu com sucesso')
        break
    if comandoInicializador.startswith('i'):
        novoItemDaLista = input('Digite o item que queira adicionar na lista: ')
        listaDeCompras.append(novoItemDaLista)
        print (listaDeCompras)
        continue
    elif comandoInicializador.startswith('a'):
        itemQueSeraRemovido = input('Digite o item que queira remover da lista: ')
        if itemQueSeraRemovido in listaDeCompras:
            listaDeCompras.pop(listaDeCompras.index(itemQueSeraRemovido))
            print(listaDeCompras)
            continue
        else:
            print('Você não pode excluir este item, pois ele não faz parte da sua lista')
            continue
    elif comandoInicializador.startswith('l'):
        indexDaLista = int(input("Digite o item que você deseja consultar: "))
        try:
            print(listaDeCompras[indexDaLista])
        except IndexError:
            print('Você não pode consultar esse item da lista, pois este índice é inexistente na sua lista')
        