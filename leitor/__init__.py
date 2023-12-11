from geral import *
from jornalista import *
import interacoes

def menu_leitor(emailusuario, materias, tipo_usuario):
    while True:

        print("-" * 30)
        print('|          Opções:           |')
        print("-" * 30)
        print('| 1 - Visualizar matérias    |')
        print('| 2 - Comentar notícia       |')
        print('| 3 - Curtir notícia         |')
        print('| 4 - Buscar matérias        |')
        print('| 5 - Sair                   |')
        print("-" * 30)
        opcao = input('Digite uma opção: ')

        if (opcao == '1'):
            geral.listar_materias(materias, tipo_usuario)
        elif (opcao == '2'):
            interacoes.comentar_materia(emailusuario, materias, tipo_usuario)
        elif (opcao == '3'):
            interacoes.curtir_materia(emailusuario, materias, tipo_usuario)
        elif (opcao == '4'):
            comentario = input('Digite o termo para busca: ')
            geral.buscar_materias(materias, tipo_usuario, comentario)
        elif (opcao == '5'):
            print('Saindo do sistema')
            break
        else:
            print('Opção inválida. Selecione novamente')
