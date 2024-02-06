import os

restaurantes = [{'nome':'Campina Burger','categoria':'Lanches','ativo':False},
                {'nome':'BigSfiha','categoria':'Árabe','ativo':True},
                {'nome':'Ponto da Pizza','categoria':'Pizza','ativo':False}]

def exibe_nome():
       print("""

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def listar_menu():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def voltar_ao_menu_principal():
   input('\nDigite qualquer tecla para voltar ao início: ')
   executa_script()

def opcao_invalida():
   exibir_subtitulo('Você escolheu uma opção inválida')   
   voltar_ao_menu_principal()

def exibir_subtitulo(subtitulo):
     os.system('cls')
     print(f'{subtitulo}\n')

def cadastra_restaurante():
    exibir_subtitulo('Cadastro de restaurantes')    

    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    
    dados_do_restaurante = {'nome':nome_restaurante,'categoria':categoria,'ativo':False}

    restaurantes.append(dados_do_restaurante)
   

    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')

    voltar_ao_menu_principal()
     
def listar_restaurante():  
    exibir_subtitulo('Lista de restaurantes')   

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']

        print(f' - {nome_restaurante} | {categoria} | {ativo}')

    voltar_ao_menu_principal()

def alterar_estado_restaurante():
   exibir_subtitulo('Ativar/Desativar restaurante')

   nome_restaurante = input('Digite o nome do restaurante que deseja ativar/desativar: ')
   
   restaurante_encontrado = False

   for restaurante in restaurantes:
       
         if restaurante['nome'] == nome_restaurante:
         
          restaurante_encontrado = True     
          restaurante['ativo'] = not restaurante['ativo']

          mensagem = f'O restaurante {nome_restaurante} foi ativado!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi Desativado!'

          print(mensagem)
 
   if not restaurante_encontrado:
          
    print(f'O restaurante {nome_restaurante} não foi encontrado')
        
   voltar_ao_menu_principal()


def processa_opcoes_match():
   try:         
      opcao_escolhida = int(input('Escolha uma opção: '))
      match opcao_escolhida:
         case 1:
            cadastra_restaurante()
         case 2:
            listar_restaurante()
         case 3:
            alterar_estado_restaurante()
         case 4:
            finalizar_app()      
         case _: #O _ corresponde a qualquer alternativa que não se encaixar aos outros cases, como se fosse um else.
            opcao_invalida()
   except:
     opcao_invalida()

def finalizar_app():    
      exibir_subtitulo('Finalizando o App')   

def executa_script():
    exibe_nome()
    listar_menu()    
    processa_opcoes_match()


if __name__ == '__main__':
    executa_script()