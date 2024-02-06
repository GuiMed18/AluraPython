import os

os.system('cls')

dados_pessoa = [{'nome':'Karol','cidade':'Montreal','idade':22},
                {'nome':'Guilherme','cidade':'Vancouver','idade':23},
                {'nome':'Ret','cidade':'Sidney','idade':3}
                ]

nome_pessoa = input('Digite o nome da pessoa a ser atualizada: ')

nome_encontrado = False

try:
 for pessoa in dados_pessoa:
   
    if pessoa['nome'] == nome_pessoa:

        nome_encontrado = True
        pessoa['idade'] = int(input(f'Digite a idade de {nome_pessoa}: '))
        pessoa['profissao'] = input(f'Digite a profissão de {nome_pessoa}: ')       
        del pessoa('cidade')
        idade = pessoa['idade']
        profissao = pessoa['profissao']        

        os.system('cls')
        print(f'Segue os dados atualizados do(a) {nome_pessoa}')
        print(f'{nome_pessoa} tem {idade} anos e é {profissao}')
        
except:
    print('Algo não funcionou corretamente, verifique os dados fornecidos')

if not nome_encontrado:
        print('Pessoa não encontrada')