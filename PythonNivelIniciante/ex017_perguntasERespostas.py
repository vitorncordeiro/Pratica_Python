listasPerguntas = [
    {
        'Pergunta': 'Quanto é 2+2? ',
        'Opcoes': ['1', '2', '3', '4'],
        'Resposta': '4'
    },
    {
        'Pergunta': 'Quanto é 5x5? ',
        'Opcoes': ['25', '3', '10', '125'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Qual o valor aproximado de π? ',
        'Opcoes': ['2,4', '3,14', '1,77', '3,33'],
        'Resposta' : '3,14',
    }
]

def perguntar(pergunta):
    acertos = 0
    print(listasPerguntas[pergunta]['Pergunta'])
    print()
    opcoesFormatadas = listasPerguntas[pergunta]['Opcoes']
    op1, op2, op3, op4 = opcoesFormatadas
    
    print(f'0) {op1}\n1) {op2}\n2) {op3}\n3) {op4}')
    print()
    opcao = listasPerguntas[pergunta]['Opcoes']
    respostaUser = int(input('Escolha uma opção: '))
    if opcao[respostaUser] == listasPerguntas[pergunta]['Resposta']:
        print('Acertou')
        acertos += 1
    else:
        print('Errou')
contador = 0
for i in listasPerguntas:
    perguntar(contador)
    contador = contador + 1
