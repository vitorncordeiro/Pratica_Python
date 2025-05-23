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
    ingredientesUsados = {'pao': 0, 'hamburguer': 0, 'tomate': 0, 'bacon': 0, 'ovo': 0}
    faltantes = []
    pedidosaiu = True
    for ingrediente in cardapio[pedido]:
        if estoque[ingrediente] > 0:
            estoque[ingrediente] -= 1
            ingredientesUsados[ingrediente] += 1
            
        else:
            faltantes.append(ingrediente)
            for chave, valor in ingredientesUsados.items():
                estoque[chave] += valor
                ingredientesUsados[chave] -= valor
            pedidosaiu = False
            break
    if pedidosaiu:        
        print(f"{pedido} saindo no capricho!!!") 
    else:
        for ing in faltantes:
            print(f"Infelizmente acabou o {ing}")
    print(estoque)
    
    
