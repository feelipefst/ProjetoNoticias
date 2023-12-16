from geral import *
from jornalista import *
from leitor import *

usuarios_cadastrados = []
idmateria = [0]
materias = []
usuario_logado = []

while True:

    print("-" * 30)
    print('|          Opções:           |')
    print("-" * 30)
    print('|      1. Cadastrar Usuário  |')
    print('|      2. Fazer login        |')
    print('|      3. Sair               |')
    print("-" * 30)

    opcao = input('Escolha uma opção: ')

    if (opcao == '1'):
        cadastrar(usuarios_cadastrados)

    elif (opcao == '2'):
        fazer_login(usuarios_cadastrados, materias, idmateria, usuario_logado)

    elif (opcao == '3'):
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")

