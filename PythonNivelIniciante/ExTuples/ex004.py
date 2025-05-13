"""Criar um programa que efetua cadastro de produtos e preços. Caso o
produto já existe, pergunta se o usuário pretende atualizar o valor.
Imprimir o dicionário ao final do programa em formato de lista.
"""
produtos = {}
while True:
    produto = input('Digite o nome do produto (Q para sair): ')
    if produto == "Q":
        break
    preco = input('Digite o preço do produto: ')
    
    if produto in produtos :
        decisao = input('O produto cadastrado já existe. Deseja atualizar o valor?(s/n)')
        if decisao == 's':
            produtos[produto] = preco
        else:
            continue
    produtos[produto] = preco

print(produtos)
    
