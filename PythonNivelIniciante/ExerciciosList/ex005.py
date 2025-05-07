"""Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
Imprima os três vetores."""
#Com list comprehension
numeros = [i for i in range(1, 21)]
pares = [j for j in numeros if j % 2 == 0]
impares = [k for k in numeros if k % 2 != 0]
print(f"Pares: {pares} | Ímpares: {impares}")

#sem list comprehension

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
pares = []
impares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

