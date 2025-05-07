"""Altere o programa anterior, intercalando 3 vetores de 10 elementos cada."""
A = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
B = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
C = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]
D = []
for i in range(len(C)):
    D.append(A[i])
    D.append(B[i])
    D.append(C[i])
print(D)
