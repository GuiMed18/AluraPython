print(f' {'#' :#^5} Plano Cartesiano {'#' :#^5}') 

coord_x = float(input('Digite a coordenada X: ').replace(',','.'))
coord_y = float(input('Digite a coordenada Y: ').replace(',','.'))

print(type(coord_x))

if coord_x > 0 and coord_y > 0:

    print('O ponto está no primeiro quadrante!')

elif coord_x < 0 and coord_y > 0:

     print('O ponto está no segundo quadrante!')

elif coord_x < 0 and coord_y < 0:
     
      print('O ponto está no terceiro quadrante!')

elif coord_x > 0 and coord_y < 0:
     
      print('O ponto está no quarto quadrante!')

else:
     
      print('O ponto está no eixo ou origem!')


