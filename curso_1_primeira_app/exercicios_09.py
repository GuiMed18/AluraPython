numero = float(input('Digite um número: ').replace(',','.'))

for multiplicador in range(1,11):
    multiplicacao = numero * multiplicador
    print(f'{numero} X {multiplicador} = {multiplicacao}')