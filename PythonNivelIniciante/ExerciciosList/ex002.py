"""Faça um Programa que leia um vetor de 10 números reais e mostre-os 
na ordem inversa."""
lista = [i for i in range(10, 101, 10)]
lista.sort(reverse=True)
print(*lista)