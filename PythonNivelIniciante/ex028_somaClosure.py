#Crie uma função cria_multiplicador(fator) que retorne uma nova função. Essa função interna deverá receber um número e retorná-lo multiplicado pelo fator fornecido.
def cria_multiplicador(x):
    def interna(y):
        return y * x
    return interna
mult3 = cria_multiplicador(3)
print(mult3(5))