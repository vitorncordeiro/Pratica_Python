def subtrai(x, y):
    return x - y

def criar_subtracao(funcao, x):
    def interna(y):
        return funcao(x,y)
    return interna

subtrai_10 = criar_subtracao(subtrai, 10)
print(subtrai_10(20))