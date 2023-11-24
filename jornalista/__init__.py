from datetime import date

import geral
from geral import *

data_atual = date.today()


def menu_jornalista(emailusuario, materias, idmateria):
    while True:
        print("-" * 30)
        print('|          Opções:           |')
        print('| 1 - Escrever matéria       |')
        print('| 2 - Visualizar matérias    |')
        print('| 3 - Excluir matéria        |')
        print('| 4 - Editar matéria         |')
        print('| 5 - Comentar matérias      |')
        print('| 6 - Sair                   |')
        print("-" * 30)
        opcao = input('Digite uma opção: ')

        if (opcao == '1'):
            escrever_materia(emailusuario, materias, idmateria)
        elif (opcao == '2'):
            geral.listar_materias(materias)
        elif (opcao == '3'):
            excluir_materia(emailusuario, materias)
        elif (opcao == '4'):
            editar_materia(emailusuario, materias)
        elif (opcao == '5'):
            geral.comentar_materia(emailusuario, materias)
        elif (opcao == '6'):
            print('Saindo do sistema')
            break
        else:
            print('Opção inválida. Selecione novamente')


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


def excluir_materia(emailusuario, materias):
    if len(materias) == 0:
        print('Não há matérias disponíveis para excluir.')
        return

    geral.listar_materias(materias)

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


def editar_materia(emailusuario, materias):

    geral.listar_materias(materias)

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


def exibirComentarios(materias):

    if len(materias['comentarios']) > 0:
            for comentario in materias['comentarios']:

                print(f'Usuário: {comentario["usuario"]}')
                print(f'Comentario: {comentario["comentario"]}')


def exibirCurtidas(materias):

    if len(materias['curtidas']) > 0:
            for curtida in materias['curtidas']:
                print(f'Matéria curtida por: {curtida}')
