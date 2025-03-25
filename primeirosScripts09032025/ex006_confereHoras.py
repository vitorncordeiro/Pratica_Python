horaInput = input('Informe que horas são: ')
if horaInput.isdigit():
    horaInput = int(horaInput)
    if horaInput >= 0 and horaInput <= 11:
        print('Bom dia')
    elif horaInput >= 12 and horaInput <= 17:
        print('Boa tarde')
    elif horaInput >= 18 and horaInput <= 23:
        print('Boa noite')
    else:
        print('Parece que você não digitou uma hora válida, por favor tente novamente')
else:
    print('Parece que você não digitou um número. Por favor tente novamente')

