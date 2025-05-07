"""Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro
vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos 
intercalados dos dois outros vetores."""
A = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
B = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
C = []
for i in range(len(B)):
    C.append(B[i])
    C.append(A[i])
print(C)