#Para chamar o aplicação em python
print('python app.py \n')
#Para copiar linhas
print('shift + alt + seta pra baixo \n')
#Seguir as convenções de escrita para linguagem (camelCase, PascalCase, Kebab-Case, snake_case)
print('Link nos favoritos - aba artigos') 
#Aspas duplas, unicas e triplas são definidas no começo do projeto
print(""" Aspas triplas dispensam formatação \n
      olha só """)
#O uso da f string é melhor para interpolação de variáveis
ex = 19
print(f"O número é {ex}!")
#Para verificar o tipo de um valor, basta usar a função type
ex = 1
print(type(ex))
#O print pode fazer validações também
print(ex == 1)
#Para definir funções, utilizar a chamada def
def funcao():
    print('É assim que se chama uma função')
#O Python tem algumas libs que é necessário chamá-las, pra isso usamos o import
import os
#A lib os permite que nós executemos comandos de terminal do sistema operacional, podemos tanto limpar a tela usando os.system('cls') como manipular diretorios
#Para impedir que um código python seja importado, deve se fazer o seguinte.
if __name__ == '__main__':
    funcao()
#Toda vez que o código é executado, é criado a variável __name__, por padrão, a execução direto no arquivo vai ser __main__, se for diferente, é puxada de outro arq
    
#Try e except
#Try é como se fosse a seguinte lógica = Tente executar esse bloco de código, se não conseguir, use o except e retorne algum comando.
#Isso evita que o código retorne erros
    
try:
    divisao = 15 / 0
except Exception as e: #Exception pega o erro registrado e é inserido na variável e
    print(e)
    
#Quando estiver escrevendo uma função ou loops, se não for colocar nenhum conteudo, adicionar o método pass, para ele ignorar aquele código
def ex_pass():
    pass

#Para adicionar um conteudo no fim da lista, usar o append
lista_compras = []
lista_compras.append('Goiaba')

#Len coleta a quantidade de conteudos em uma lista
print(len(lista_compras))

#Dicionários
#Funcionam como identificadores de conteúdo dentro de uma lista, sempre começando e terminando por {}.
lista_funcionario = [
    {'nome':'Ana','idade':23,'País':'Canada'}
    ]
#Operador not
#Esse operador inverte o resultado de um boolean
nome = False

if not nome:
    print('É true que nome é false, Nome é vazio')

#Operador Ternário
mensagem = f'O restaurante {nome} foi ativado!' if not nome else f'O restaurante {nome} foi Desativado!'
#A primeira mensagem vai ser exibida se a condição do if for verdadeira, se não, a outra é exibida

# É possível incluir operadores matemáticos com strings, por exemplo

cidade = 'Pindamonhangaba'
linha = '*' * len(cidade)

print(linha)
print(cidade)
print(linha)

#Aqui, o elemento '*' foi multiplicado pela quantidade de letras que a cidade possui.