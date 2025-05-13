"""
Criar um programa que cadastre funcionário de um empresa e
seus dependentes. O funcionário deve ser cadastrado com
matrícula, nome e dependentes. Os dependentes devem ser
inseridos dinamicamente em uma tupla. Dica: usar o operador
+=
"""
funcionarios = []
while True:
    listaFuncionario = {"nome": input('Digite o nome do funcionário: '), "matricula": input('Digite o número de matrícula: ')}
    dependentes = tuple()
    while True:
        dependente = (input('Digite o nome do dependente (Q para sair): '),)
        if dependente == ("Q",):
            break
        dependentes += dependente
    listaFuncionario['Dependentes'] = dependentes
    print(listaFuncionario)




                        