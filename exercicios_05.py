login_padrao = 'root'
senha_padrao = 'admin'

login_user = input('Digite seu login: ')
senha_user = input('Digite sua senha: ')

if login_user == login_padrao and senha_user == senha_padrao:
    print(f'Acesso liberado, Bem vindo {login_user}!')
else:
    print('Acesso negado.')

