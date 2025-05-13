"""Criar um programa que solicita valor de vendas e o mês onde
cada venda ocorreu. Independente de repetição de meses, o
aplicativo deve totalizar por mês todas as vendas cadastradas.
Ao final deve informar o valor de vendas de todos os meses do
ano. Obs.: se for digitado errado o nome do mês, informar que o
mês é inválido.
"""
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril',\
         'Maio', 'Junho', 'Julho', 'Agosto',
         'Setembro', 'Outubro', 'Novembro', 'Dezembro']
dictMesesValores = {}
contadorVendas = 0
while True:
    mes = input('Digite o mês: ')
    if mes == "Q":
        break
    if mes not in meses:
        print('Digite um mês válido!')
        continue
    
    valorVenda = int(input('Digite o valor da venda: '))

    dictMesesValores[mes] = valores.append(valorVenda)

print(dictMesesValores)