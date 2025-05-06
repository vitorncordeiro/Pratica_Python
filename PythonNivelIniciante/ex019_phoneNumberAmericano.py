def create_phone_number(n):
    novoI = ''
    for i in n:
        novoI += str(i)
    strNumerosJuntos = ''.join(novoI) #transforma a lista em uma str unica com os numeros
    DDD = strNumerosJuntos[0:3]
    trechoTresD = strNumerosJuntos[3:6]
    trechoQuatroD = strNumerosJuntos[6:]
    return f'({DDD}) {trechoTresD}-{trechoQuatroD}'
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
        