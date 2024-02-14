class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.nome = 'Bistrô'
restaurante_praca.categoria = 'Italiana'

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
restaurante_pizza.ativo = True


categoria = restaurante_praca.categoria
print(categoria)

if restaurante_pizza.categoria == 'Fast Food':
    print(f'O restaurante {restaurante_pizza.nome} é {restaurante_pizza.categoria}')

if not restaurante_pizza.ativo:
    print(f'O restaurante {restaurante_pizza.nome},categoria {restaurante_pizza.categoria} está inativo!')
else:
    print(f'O restaurante {restaurante_pizza.nome},categoria {restaurante_pizza.categoria} está ativo!')

if not restaurante_praca.ativo:
    print(f'O restaurante {restaurante_praca.nome}, categoria {restaurante_praca.categoria} está inativo!')
else:
    print(f'O restaurante {restaurante_praca.nome}, categoria {restaurante_praca.categoria} está ativo!')


lista_restaurantes = [restaurante_praca,restaurante_pizza]