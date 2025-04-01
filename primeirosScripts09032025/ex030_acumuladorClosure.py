#   Crie uma função acumulador(valor_inicial) que retorne outra função. Essa função 
#   interna deve receber um número e somá-lo a um valor acumulado, retornando o total 
#   atualizado a cada chamada.
def acumulador(valor_inicial):
    valorAcumulado = valor_inicial
    def interna(x):
        nonlocal valorAcumulado
        valorAcumulado += x
        return valorAcumulado  
    
    return interna

acum = acumulador(0)
for i in range(11):
    print(acum(2*i))

