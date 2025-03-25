def create_phone_number(n):
    novoI = ''
    for i in n:
        novoI += str(i)
    strNumerosJuntos = ''.join(novoI) #transforma a lista em uma str unica com os numeros
    DDD = strNumerosJuntos[0:2]
    parteUm = strNumerosJuntos[2:7]
    parteDois = strNumerosJuntos[7:]
    return f'({DDD}) {parteUm}-{parteDois}'
print(create_phone_number([4, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
        