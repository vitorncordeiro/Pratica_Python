"""Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada 
informação no seu respectivo vetor.
Imprima a idade e a altura na ordem inversa a ordem lida"""
dados = []
for i in range(5):
    print(f'Pessoa nº{i+1}')
    idade = int(input('Digite sua idade: '))
    altura = float(input('Digite sua altura em metros: '))
    dados.append([idade, altura])
for dado in dados:
    dado.sort()
print(*dados)
