from copy import deepcopy

produtos = [
    {'nome': 'Produto a', 'preco': 10.00},
    {'nome': 'Produto b', 'preco': 22.32},
    {'nome': 'Produto c', 'preco': 10.11},
    {'nome': 'Produto d', 'preco': 105.87},
    {'nome': 'Produto e', 'preco': 69.90},
]
produtosOrdenadosPNome = deepcopy(produtos)
for i in produtosOrdenadosPNome:
    i['preco'] *= 1.1
# Ordene os produtos por nome decrescente (do maior para menor)
produtosOrdenadosPNome.sort(key=lambda item: item['nome'], reverse=True)
print('\n Produtos ordenados pelo nome em ordem decrescente: \n')
print(*produtosOrdenadosPNome, sep='\n')


# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)



# Ordene os produtos por preco crescente (do menor para maior)
produtosOrdenadosPorPreco = deepcopy(produtos)
produtosOrdenadosPorPreco.sort(key=lambda preco: preco['preco'])
print('\n Produtos ordenados pelo Preço: \n')
print(*produtosOrdenadosPorPreco, sep='\n')

print(f'\nTabela original:\n')
print(*produtos, sep='\n')

# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
