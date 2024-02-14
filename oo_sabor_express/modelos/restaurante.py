class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_nosso_pao = Restaurante()
restaurante_nosso_pao.nome = 'Nosso Pão'
restaurante_nosso_pao.categoria = 'Padaria'

restaurante_vovozinha = Restaurante()

lista_restaurantes = [restaurante_nosso_pao,restaurante_vovozinha]

print(lista_restaurantes)