from jornalista import *
from leitor import *
from geral import *


def curtir_materia(emailusuario, materias, tipo_usuario, usuario_logado):
    geral.listar_materias(materias, tipo_usuario, usuario_logado)
    if len(materias) == 0:
        return
    id_noticia_curtir = input('Digite o ID da notícia que deseja curtir: ')
    if not id_noticia_curtir.isdigit():
        print('ID inválido. Digite um número válido.')
        return
    id_noticia_curtir = int(id_noticia_curtir)
    for materia in materias:
        if materia['id'] == id_noticia_curtir:
            if len(materia['curtidas']) > 0:
                for i in materia['curtidas']:
                    if usuario_logado[0] == i:
                        print(f'Você já curtiu esta notícia anteriormente.')
                        return
                    else:
                        materia['curtidas'].append(usuario_logado[0])
                        print('Curtida adicionada com sucesso')
                        break
            else:
                materia['curtidas'].append(usuario_logado[0])
                print('Curtida adicionada com sucesso')
                break
            break
    else:
        print(f'Matéria com ID {id_noticia_curtir} não encontrada.')


def comentar_materia(emailusuario, materias, tipo_usuario, usuario_logado):
    geral.listar_materias(materias, tipo_usuario, usuario_logado)
    if len(materias) == 0:
        return
    id_a_comentar = input('Digite o id da matéria que deseja comentar: ')
    if not id_a_comentar.isdigit():
        print('ID inválido. Digite um número válido.')
        return
    id_a_comentar = int(id_a_comentar)
    for materia in materias:
        if materia['id'] == id_a_comentar:
            comentario = input('Digite seu comentário: ')
            materia['comentarios'].append({'usuario': emailusuario, 'comentario': comentario})
            print('Comentário adicionado com sucesso.')
            return
    else:
        print(f'Notícia com ID {id_a_comentar} não encontrada.')


def exibirComentarios(materias):
    if len(materias['comentarios']) > 0:
        for comentario in materias['comentarios']:
            print(f'Usuário: {comentario["usuario"]}')
            print(f'Comentario: {comentario["comentario"]}')


def exibirCurtidas(materias, tipo_usuario, usuario_logado):
    if len(materias['curtidas']) > 0:
        if (tipo_usuario == 'leitor'):
            print(f'Curtidas: {len(materias["curtidas"])}')
        else:
            if (materias['autor'] == usuario_logado[0]):
                print(f'Curtidas: {len(materias["curtidas"])}')
                for curtida in materias['curtidas']:
                    print(f'Matéria curtida por: {curtida}')
            else:
                print(f'Curtidas: {len(materias["curtidas"])}')


def organizar_mais_curtidas(materias, tipo_usuario, usuario_logado):
    new_list = sorted(materias, key=lambda materias: len(materias['curtidas']), reverse=True)
    for materia in new_list:
        print('-' * 40)
        print(f"ID: {materia['id']}")
        print(f"Título: {materia['titulo']}")
        print(f"Autor: {materia['autor']}")
        print(f"Data: {materia['data']}")
        print(f"Conteúdo: {materia['conteudo']}")
        exibirComentarios(materia)
        exibirCurtidas(materia, tipo_usuario, usuario_logado)


def organizar_mais_curtidas_user(materias, tipo_usuario, emailusuario, usuario_logado):
    new_list = sorted(materias, key=lambda materias: len(materias['curtidas']), reverse=True)
    for materia in new_list:
        if (materia['autor'] == emailusuario):
            print('-' * 40)
            print(f"ID: {materia['id']}")
            print(f"Título: {materia['titulo']}")
            print(f"Autor: {materia['autor']}")
            print(f"Data: {materia['data']}")
            print(f"Conteúdo: {materia['conteudo']}")
            exibirComentarios(materia)
            exibirCurtidas(materia, tipo_usuario, usuario_logado)