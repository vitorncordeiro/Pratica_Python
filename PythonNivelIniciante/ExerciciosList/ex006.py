""" Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene 
num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0."""
Alunos = []
for i in range(10):
    print(f'Cadastrando nota do aluno nº{i+1}')
    notas = []
    for j in range(4):
        notaAtual = int(input(f'Digite a {j+1}ª nota: '))
        notas.append(notaAtual)
    media = sum(notas) / len(notas)
    Alunos.append([f'Aluno {i+1}', media])
#Média maior que 7 com list comprehension
ListaAprovados = [i for i in Alunos if i[1] >= 7]
#Sem list comprehension
ListaAprovados = []
for i in Alunos:
    if i[1] >= 7:
        ListaAprovados.append(i)
        
print(len(ListaAprovados))

        
