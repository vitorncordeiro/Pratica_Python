from copy import deepcopy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
copiaTotal = deepcopy(produtos)
for i in copiaTotal:
    i['preco'] *= 1.1
# Ordene os produtos por nome decrescente (do maior para menor)
copiaTotal.sort(key=lambda item: item['nome'], reverse=True)
print(*copiaTotal, sep='\n')


# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)



# Ordene os produtos por preco crescente (do menor para maior)
copiaTotal.sort(key=lambda preco: preco['preco'])
print(*copiaTotal, sep='\n')


# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

