from datetime import date

import geral
from geral import *

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
        print('| 7 - Sair                   |')
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
            geral.comentar_materia(emailusuario, materias, tipo_usuario)
        elif (opcao == '6'):
            comentario = input('Digite o termo para busca: ')
            geral.buscar_materias(materias, tipo_usuario, comentario)
        elif (opcao == '7'):
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
                geral.curtir_materia(emailusuario, materias, tipo_usuario)
                break
            elif (op == 2):
                organizar_mais_curtidas(materias, tipo_usuario)
            elif (op == 3):
                break
            else:
                print('Opção Invalida')

        elif (op == 2):
            minhas_materias()

            print(f'\nDeseja organizar pelas mais curtidas? 1 - Sim | 2 - Não ')
            op = int(input(f'\nDigite uma opção: '))

            if (op == 1):
                organizar_mais_curtidas(materias, tipo_usuario)
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


def exibirComentarios(materias):

    if len(materias['comentarios']) > 0:
            for comentario in materias['comentarios']:

                print(f'Usuário: {comentario["usuario"]}')
                print(f'Comentario: {comentario["comentario"]}')


def exibirCurtidas(materias, tipo_usuario):

    if len(materias['curtidas']) > 0:
        if (tipo_usuario == 'leitor'):
            print(f'Curtidas: {len(materias["curtidas"])}')

        else:
            print(f'Curtidas: {len(materias["curtidas"])}')
            for curtida in materias['curtidas']:
                print(f'Matéria curtida por: {curtida}')

def organizar_mais_curtidas(materias, tipo_usuario):
    for materia in materias:
        n = len(materia['curtidas'])
        print(n)

        for j in range(0, n - 1):
            if materia['curtidas'][j] < materia['curtidas'][j + 1]:
                aux = materias[j]
                print('aqui', aux)
                materias[j] = materias[j + 1]
                materias[j + 1] = aux

        print(materia)
