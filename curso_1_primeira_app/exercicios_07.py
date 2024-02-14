projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for projeto in projetos:
    if(projeto):
     print(f'{projeto}\n')
    else:
     print('Projeto não disponível\n')