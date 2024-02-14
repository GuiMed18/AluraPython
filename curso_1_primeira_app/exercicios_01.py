##Escreva a frase: Python na Escola de Programação da Alura.
print('Python na Escola de Programação da Alura.')
## Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.
nome = 'Guilherme'
idade = 23
print(f'Meu nome é {nome} e tenho {idade} anos!')
## Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha
#Temos várias formas de fazer isso, a que consome menos linhas é usando aspas simples
print(' A \n L \n U \n R \n A')
#Temos também a opção de usar aspas triplas, mas que utiliza muitas linhas de código
print("""   
 A
 L
 U
 R
 A
""")
#Utilizando o parâmetro SEP
print('A','L','U','R','A',sep='\n')

## Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável e arredondado para apenas duas casas decimais.

pi = 3.14159
print(f'O valor arredondado de PI é {pi:.2f}')

departamento = input('Digite o nome do departamento: ')
responsavel = input('Digite o nome do responsavel: ')
print('O responsável do departamento ' + departamento + ' é o líder: ' + responsavel + '.')