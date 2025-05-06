def multiplicacao(*args):
    total = 1
    for i in args:
        total = total * i
    return total
resultado = multiplicacao(10, 3, 5.7, 10, -0.7)
print(resultado)

def impar(z):
    if z % 2 == 0:
       return 'par'
    else:
       return 'impar'

parOuNao = impar(resultado)
print(parOuNao)
