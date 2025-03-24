def criarFuncoes(y): #onde x é o número dado pelo user e y é o multiplicador
    def multiplicar(x): #vai definir uma função que pega como argumento o valor que o usuário digitará
        return x * y #multiplica esse valor(dinâmico) pelo Y que é o multiplicador, que ele lembra por causa do closure
    return multiplicar #retorna a função interna
duplicar = criarFuncoes(2) #cria uma função, que recebe o multiplicar que lembra do y=2
triplicar = criarFuncoes(3) #cria uma outra função, que recebe o multiplicar que lembra do y=3
quadruplicar = criarFuncoes(4) #cria a ultima função, que recebe multiplicar que lembra do y=4
userInput = int(input('Digite o número a ser operado: ')) 
print(f'   {duplicar(userInput)}\n {triplicar(userInput)}\n {quadruplicar(userInput)}')#passa como argumento para o multiplicar(), o número que o usuário escreveu

