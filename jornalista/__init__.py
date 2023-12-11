from datetime import date

import geral
from geral import *
import interacoes

data_atual = date.today()


def menu_jornalista(emailusuario, materias, idmateria, tipo_usuario):
    while True:
        print("-" * 30)
        print('|          Opções:           |')
        print('| 1 - Escrever matéria       |')
        print('| 2 - Visualizar matérias    |')
        print('| 3 - Excluir matéria        |')
        print('| 4 - Editar matéria         |')
        print('| 5 - Comentar matérias      |')
        print('| 6 - Buscar matérias        |')
        print('| 7 - Salvar arquivo         |')
        print('| 8 - Sair                   |')
        print("-" * 30)
        opcao = input('Digite uma opção: ')

        if (opcao == '1'):
            escrever_materia(emailusuario, materias, idmateria)
        elif (opcao == '2'):
            sub_materias(emailusuario, materias, tipo_usuario)
        elif (opcao == '3'):
            excluir_materia(emailusuario, materias, tipo_usuario)
        elif (opcao == '4'):
            editar_materia(emailusuario, materias, tipo_usuario)
        elif (opcao == '5'):
            interacoes.comentar_materia(emailusuario, materias, tipo_usuario)
        elif (opcao == '6'):
            comentario = input('Digite o termo para busca: ')
            geral.buscar_materias(materias, tipo_usuario, comentario)
        elif (opcao == '7'):
            geral.salvar_arquivo(materias, emailusuario, tipo_usuario)
        elif (opcao == '8'):
            print('Saindo do sistema')
            break
        else:
            print('Opção inválida. Selecione novamente')


def sub_materias(emailusuario, materias, tipo_usuario):
    while True:

        print("-" * 42)
        print('|              Opções:                   |')
        print('| 1 - Visualizar todas as matérias       |')
        print('| 2 - Visualizar apenas minhas matérias  |')
        print('| 3 - Sair                               |')
        print("-" * 42)
        op = int(input('Digite uma opção: '))

        if (op == 1):
            geral.listar_materias(materias, tipo_usuario)

            print("-" * 36)
            print('| 1 - Curtir notícia               |')
            print('| 2 - Organizar por mais curtidas  |')
            print('| 3 - Sair                         |')
            print("-" * 36)

            op = int(input(f'\nDigite uma opção: '))

            if (op == 1):
                interacoes.curtir_materia(emailusuario, materias, tipo_usuario)
                break
            elif (op == 2):
                interacoes.organizar_mais_curtidas(materias, tipo_usuario)
            elif (op == 3):
                break
            else:
                print('Opção Invalida')

        elif (op == 2):
            minhas_materias(materias, tipo_usuario, emailusuario)

            print(f'\nDeseja organizar pelas mais curtidas? 1 - Sim | 2 - Não ')
            op = int(input(f'\nDigite uma opção: '))

            if (op == 1):
                interacoes.organizar_mais_curtidas_user(materias, tipo_usuario, emailusuario)
                break
            elif (op == 2):
                break
            else:
                print('Opção Invalida')

        elif (op == 3):
            break

        else:
            print('Opção Invalida')


def escrever_materia(email, materias, idmateria):
    titulo = input('Digite o titulo da matéria: ')
    conteudo = input('Digite o texto: ')
    data_materia = '{}/{}/{}'.format(data_atual.day, data_atual.month, data_atual.year)

    idmateria[0] += 1

    materia = {
        'id': idmateria[0],
        'titulo': titulo,
        'conteudo': conteudo,
        'data': data_materia,
        'autor': email,
        'comentarios': list(),
        'curtidas': list()
    }

    materias.append(materia)

    print('Matéria escrita com sucesso!')


def excluir_materia(emailusuario, materias, tipo_usuario):
    if len(materias) == 0:
        print('Não há matérias disponíveis para excluir.')
        return

    geral.listar_materias(materias, tipo_usuario)

    id_a_excluir = input('Digite o ID da notícia: ')

    if not id_a_excluir.isdigit():
        print('ID inválido. Digite um número válido')
        return
    id_a_excluir = int(id_a_excluir)

    for materia in materias:
        if materia['id'] == id_a_excluir:
            if emailusuario == materia['autor']:
                materias.remove(materia)
                print(f'Noticia com ID {id_a_excluir} excluida com sucesso.')
            else:
                print('Você não tem permissão para excluir esta matéria')
            return
    print(f'Noticia com ID {id_a_excluir} não encontrada. ')


def editar_materia(emailusuario, materias, tipo_usuario):

    geral.listar_materias(materias, tipo_usuario)

    id_a_editar = input('Qual id da matéria a ser editada: ')

    if not id_a_editar.isdigit():
        print('ID inválido. Digite um número válido.')
        return
    id_a_editar = int(id_a_editar)

    for materia in materias:
        if materia['id'] == id_a_editar and emailusuario == materia['autor']:

            print(f'Editando matéria com ID {id_a_editar} .')
            novo_titulo = input('Digite o novo título: ')
            novo_titulo = (f'Editada - {novo_titulo}')
            novo_conteudo = input('Digite o novo conteúdo: ')
            nova_data = '{}/{}/{}'.format(data_atual.day, data_atual.month, data_atual.year)

            materia['titulo'] = novo_titulo
            materia['conteudo'] = novo_conteudo
            materia['data'] = nova_data

            print(f'Matéria com ID {id_a_editar} editada com sucesso.')
            break

        else:
            print('Você não tem permissão para editar esta matéria')
            break
    else:
        print(f'Matéria com ID {id_a_editar} não encontrada')


def minhas_materias(materias, tipo_usuario, emailusuario):

    for materia in materias:
        if (materia['autor'] == emailusuario):

            print('-' * 40)
            print(f"ID: {materia['id']}")
            print(f"Título: {materia['titulo']}")
            print(f"Autor: {materia['autor']}")
            print(f"Data: {materia['data']}")
            print(f"Conteúdo: {materia['conteudo']}")

            interacoes.exibirComentarios(materia)
            interacoes.exibirCurtidas(materia, tipo_usuario)

        else:
            print('Nenhuma materia a ser exibida')