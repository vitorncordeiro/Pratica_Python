nome = input('Digite seu nome completo: ')
primeiroNome = nome.split(' ')[0]
print(f'Analisando seu nome...\nSeu nome em maísculo é {nome.upper()}\nSeu nome em minúsculo é {nome.lower()}\nSeu nome tem ao todo ten {len(nome)} letras\nSeu primeiro nome é {primeiroNome} e ele tem {len(primeiroNome)} letras ')
