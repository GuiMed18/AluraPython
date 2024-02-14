### Para acessar o objeto de uma classe
class Pessoa:
    nome = ''
    idade = int
    bloqueado = True

pessoa_guilherme = Pessoa() #Primeiro usamos a variável para instanciar a classe
pessoa_guilherme.nome = 'Guilherme' #Para acessar o objeto, usamos o . e o nome do método definido.
pessoa_guilherme.idade = 23 

# Para verificar os atributos de um objeto, usar a função dir()
print(dir(pessoa_guilherme))

#Sempre que houver um método iniciado e finalizado por 2 _ (__class__), é um método especial

#A função vars permite ver somente os métodos (Exceto booleanos aparentemente)

print(vars(pessoa_guilherme))


