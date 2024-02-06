idade = int(input('Digite sua idade: '))

if 0 < idade <= 12:
    print('Você é criança!')
elif idade <= 18:
    print('Você é adolescente!')
elif idade > 18:
    print('Você é adulto!')
else:
    print('Valor Inválido')