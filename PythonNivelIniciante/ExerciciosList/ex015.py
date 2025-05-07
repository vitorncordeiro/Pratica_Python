"""Faça um programa que leia um número indeterminado de valores, correspondentes 
a notas, encerrando a entrada de dados quando for informado um valor igual a -1 
(que não deve ser armazenado). Após esta entrada de dados, faça:
a. Mostre a quantidade de valores que foram lidos;
b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
d. Calcule e mostre a soma dos valores;
e. Calcule e mostre a média dos valores;
f. Calcule e mostre a quantidade de valores acima da média calculada;
g. Calcule e mostre a quantidade de valores abaixo de sete;
h. Encerre o programa com uma mensagem;"""
notas = []
while True:
    nota = int(input('Digite uma nota: '))
    if nota == -1:
        break
    notas.append(nota)
print(len(notas))
print(*notas)
notas.reverse()
for nota in notas:
    print(nota)
print(f'Soma: {sum(notas)}')
media = sum(notas)/len(notas)
print(f"Média: {media}")
valoresAcimaDaMedia = []
for nota in notas:
    if nota > media:
        valoresAcimaDaMedia.append(nota)
print(f"{len(valoresAcimaDaMedia)} Valores acima da média")
valoresAbaixoDesete = []
for nota in notas:
    if nota < 7:
        valoresAbaixoDesete.append(nota)
print(f'{len(valoresAbaixoDesete)} Valores abaixo de 7')
print('Encerrando...')
