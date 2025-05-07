"""Faça um Programa que leia um vetor A com 10 números inteiros, calcule e 
mostre a soma dos quadrados dos elementos do vetor."""
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
somaDoQuadrado = 0
for numero in A:
    numero = numero**2
    somaDoQuadrado += numero
print(somaDoQuadrado)