import random

listaNomes = ['Vitor', 'Suellen', 'Lauren', "Ivy"]
for i in range(4):
    input('Nome: ')
    listaNomes.append(nome)
random.shuffle(listaNomes)
print(random.sample(listaNomes, k=2))


