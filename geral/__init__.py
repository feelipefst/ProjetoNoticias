from jornalista import *
from leitor import *


TIPO_JORNALISTA = 'jornalista'
TIPO_LEITOR = 'leitor'


def fazer_login(usuarios_cadastrados, materias, idmateria):
    email = input('Email: ')
    senha = input('Senha: ')

    for usuario in usuarios_cadastrados:
        if not usuario['email'] == email and usuario['senha'] == senha:
            continue

        if (usuario['email'] == email and usuario['senha'] == senha):

            if (usuario['tipo'] == TIPO_JORNALISTA):
                menu_jornalista(email, materias, idmateria)

            elif (usuario['tipo'] == TIPO_LEITOR):
                menu_leitor(email, materias)

        else:
            print('Credenciais inválidas')


def comentar_materia(emailusuario, materias):

    listar_materias(materias)

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


def curtir_materia(emailusuario, materias):

    listar_materias(materias)

    if len(materias) == 0:
        return

    id_noticia_curtir = input('Digite o ID da notícia que deseja curtir: ')

    #if 'curtidas' in emailusuario:
    #   print('Você já curtiu esta notícia anteriormente.')
    #  return

    if not id_noticia_curtir.isdigit():
        print('ID inválido. Digite um número válido.')
        return
    id_noticia_curtir = int(id_noticia_curtir)

    for materia in materias:
        if emailusuario in materia['curtidas']:
            print(f'Você já curtiu esta notícia anteriormente.')
        else:
            materia['curtidas'].append(emailusuario)
    else:
        print(f'Matéria com ID {id_noticia_curtir} não encontrada.')

        #
        # for i in materia['curtidas']:
        #     if(i == emailusuario):
        #         print(f'Você já curtiu esta notícia anteriormente.')
        #         return
        #
        # if(materia['id'] == id_noticia_curtir):
        #     materia['curtidas'].append(emailusuario)
        #     print('Curtida adicionada com sucesso')
        #     break



def listar_materias(materias):

    if len(materias) == 0:
        print('Não há matérias disponíveis no momento')
        return

    else:
        print(f'\n\nLista de matérias:')
        for materia in materias:
            print('-' * 40)
            print(f"ID: {materia['id']}")
            print(f"Título: {materia['titulo']}")
            print(f"Autor: {materia['autor']}")
            print(f"Data: {materia['data']}")
            print(f"Conteúdo: {materia['conteudo']}\n")

            exibirComentarios(materia)
            exibirCurtidas(materia)


def cadastrar(usuarios_cadastrados):
    print("-" * 30)
    while True:
        nome = input('Nome: ')
        if nome.strip():  # Verifica se a string não está vazia após remover espaços em branco
            break
        else:
            print('Não pode ficar vazio tente novamente')

    while True:
        email = input('Email: ')
        if '@' in email and email.endswith('.com') and email not in usuarios_cadastrados:
            break
        elif '@' not in email:
            print('Email deve conter o caractere @. Tente novamente')
        elif not email.endswith('.com'):
            print("O email deve terminar com '.com' ")
            print('Exemplo: seu_email@dominio.com')
        else:
            print('Email já cadastrado. Informe outro')

    senha = None
    while True:
        print('Informe uma senha que contenha 6 caracteres (letras e números)')
        senha = input('Senha: ')
        if validar_senha(senha):
            break
        else:
            print('Senha não atende aos critérios.')
    confirmacao_senha = None
    while True:
        confirmacao_senha = input('Confirme a senha: ')
        if senha == confirmacao_senha:
            break
        else:
            print('As senhas não coincidem. Tente novamente')

    print("-" * 30)
    print('| Escolha o tipo de usuário: |')
    print('| 1. Jornalista              |')
    print('| 2. Leitor                  |')
    print("-" * 30)

    while True:
        tipo_usuario = input("Digite o número correspondente ao tipo de usuário: ")
        if tipo_usuario == '1':
            tipo_usuario = TIPO_JORNALISTA
            break
        elif tipo_usuario == '2':
            tipo_usuario = TIPO_LEITOR
            break
        else:
            print("Opção inválida. Tente novamente.")

    novo_usuario = {
        'nome': nome,
        'email': email,
        'senha': senha,
        'tipo': tipo_usuario
    }

    cadastrar_novo_usuario(usuarios_cadastrados, novo_usuario)


def validar_senha(senha):
    if len(senha) >= 6 and any(char.isalpha() for char in senha) and any(char.isdigit() for char in senha):
        return True
    else:
        return False


def cadastrar_novo_usuario(usuarios_cadastrados, novo_usuario):
    for usuario in usuarios_cadastrados:
        if (usuario['email'] == novo_usuario['email']):
            print('email existente')
            return

    usuarios_cadastrados.append(novo_usuario)
    print('Usuário cadastrado')