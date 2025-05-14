estoque = {'pao': 10, 'hamburguer': 12, 'tomate': 5, 'bacon': 5, 'ovo': 5}
cardapio = {
'x-burguer': ['pao', 'hamburguer'],
'x-salada': ['pao', 'hamburguer', 'tomate'],
'x-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
'x-egg': ['pao', 'hamburguer', 'ovo'],
'x-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']
}
print(f"Cardápio Boca Feliz")
for chave in cardapio:
    print(chave)
while True:
    pedido = input('O que deseja pedir?(0 para sair)\n')
    if pedido == "0":
        print('Saindo...')
        break
    elif pedido not in cardapio:
        print('Item não localizado no cardápio')
        continue

    pedidoAtual = {'pao': 0, 'hamburguer': 0, 'tomate': 0, 'bacon': 0, 'ovo': 0} 
    
    for ingrediente in cardapio[pedido]:
        if estoque[ingrediente] > 0:
            pedidoAtual[ingrediente] += 1
        else:
            print(f'Infelizmente acabou o {ingrediente}')
    controle = True
    
    for key, qunatidadeIngrediente in pedidoAtual.items():
        if qunatidadeIngrediente <= estoque[key]:
            pass
        else:
            controle = False
    
    if controle == True:
        print(f"um {pedido} saindo no capricho!!!")
        for chave, valor in pedidoAtual.items():
            estoque[chave] -= pedidoAtual[chave] 
        print(estoque)
    else:
        print(f'Infelizmente acabou o {ingrediente}')


