"""Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que 
determine quantos alunos com mais de 13 anos possuem altura inferior à média de 
altura desses alunos."""
listaAlturasEIdades = [[13, 1.6], [14, 1.8], [18, 1.6]]
alunosBaixos = []
soma = 0
for lista in listaAlturasEIdades:
    soma += lista[1]
mediaAltura = soma / len(listaAlturasEIdades)

for lista in listaAlturasEIdades:
    if lista[0] > 13 and lista[1] < mediaAltura:
        alunosBaixos.append(lista)
print(alunosBaixos)