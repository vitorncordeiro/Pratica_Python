"""Faça um Programa que leia um vetor de 10 caracteres, e diga quantas 
consoantes foram lidas. Imprima as consoantes"""
caracteres = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
VOGAIS = ["a", "e", "i", "o", "u"]
consoantesVetor = []
for caracter in caracteres:
    if caracter not in VOGAIS:
        consoantesVetor.append(caracter)
print(f"Quantidade de consoantes lidas: {len(consoantesVetor)} | Consoantes lidas:", *consoantesVetor)

        