from jornalista import *
from geral import *
from jornalista import *

def menu_leitor(emailusuario, materias):
    while True:

        print("-" * 30)
        print('|          Opções:           |')
        print("-" * 30)
        print('| 1 - Visualizar matérias    |')
        print('| 2 - Comentar notícia       |')
        print('| 3 - Curtir notícia         |')
        print('| 4 - Sair                   |')
        print("-" * 30)
        opcao = input('Digite uma opção: ')

        if (opcao == '1'):
            geral.listar_materias(materias)
        elif (opcao == '2'):
            geral.comentar_materia(emailusuario, materias)
        elif (opcao == '3'):
            geral.curtir_materia(emailusuario, materias)
        elif (opcao == '4'):
            print('Saindo do sistema')
            break
        else:
            print('Opção inválida. Selecione novamente')
