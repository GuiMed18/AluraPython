print('Pomodoro')
tempo = int(input('Digite um tempo entre 25-45 Minutos: '))

if 25 <= tempo <= 45:
    print('Programado para',tempo,'minutos')
else:
    print('Horário fora do determinado, tente inserir um entre 25 a 45 minutos')
