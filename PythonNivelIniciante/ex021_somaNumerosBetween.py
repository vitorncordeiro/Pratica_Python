def get_sum(a,b):
    if a > b: a, b = b, a
    lista = [numero for numero in range(a, b + 1)]#Loop pra adicionar na lista todos os numeros inteiros entre a e b
    return sum(lista)
print(get_sum(-1, 3))