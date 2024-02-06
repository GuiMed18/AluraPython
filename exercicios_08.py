numeros = [1,2,3,4,5,6,7,8,9,10]

nomes = ['Karol','Guilherme','Retinho','AirFryer']

anos = [2000,2024]



def exibe_numeros_impares(numeros):
    soma_numeros_impares = 0
    for numero in numeros:
        if numero % 2 != 0:
           soma_numeros_impares += numero
    print(f'A soma dos números ímpares é {soma_numeros_impares}')          


def exibe_listas(nome_lista):
    for nome in nome_lista:
        print(f'{nome}')

print('#### Exibindo Números ####')
exibe_listas(numeros)
print('#### Exibindo Nomes ####')
exibe_listas(nomes)
print('#### Exibindo Anos ####')
exibe_listas(anos)
print('#### Exibindo Números ímpares ####')
exibe_numeros_impares(numeros)
