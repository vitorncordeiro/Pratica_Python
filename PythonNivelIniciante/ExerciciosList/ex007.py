"""Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a 
multiplicação e os números"""
numeros = [1, 2, 3, 4, 5]
soma = 0
multiplicacao = 1
for numero in numeros:
    soma += numero
    multiplicacao *= numero
print(*numeros, f"| Soma: {soma} | Multiplicação: {multiplicacao}")