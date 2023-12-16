from jornalista import *
from leitor import *
import interacoes
import webbrowser


TIPO_JORNALISTA = 'jornalista'
TIPO_LEITOR = 'leitor'


def fazer_login(usuarios_cadastrados, materias, idmateria, usuario_logado):
    email = input('Email: ')
    senha = input('Senha: ')
    for usuario in usuarios_cadastrados:
        if not usuario['email'] == email and usuario['senha'] == senha:
            continue
        if (usuario['email'] == email and usuario['senha'] == senha):
            usuario_logado.append(usuario['email'])
            if (usuario['tipo'] == TIPO_JORNALISTA):
                menu_jornalista(email, materias, idmateria, usuario['tipo'], usuario_logado)
            elif (usuario['tipo'] == TIPO_LEITOR):
                menu_leitor(email, materias,usuario['tipo'], usuario_logado)
        else:
            print('Credenciais inválidas')
            break


def listar_materias(materias, tipo_usuario, usuario_logado):
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
            print(f"Conteúdo: {materia['conteudo']}")
            interacoes.exibirComentarios(materia)
            interacoes.exibirCurtidas(materia, tipo_usuario, usuario_logado)


def buscar_materias(materias, tipo_usuario, comentario, usuario_logado):
    if len(materias) == 0:
        print('Não há matérias disponíveis no momento')
        return
    else:
        print(f'\n\nLista de matérias:')
        for materia in materias:
            if (comentario in materia['titulo'] or comentario in materia['conteudo']):
                print('-' * 40)
                print(f"ID: {materia['id']}")
                print(f"Título: {materia['titulo']}")
                print(f"Autor: {materia['autor']}")
                print(f"Data: {materia['data']}")
                print(f"Conteúdo: {materia['conteudo']}")
                interacoes.exibirComentarios(materia)
                interacoes.exibirCurtidas(materia, tipo_usuario, usuario_logado)


def cadastrar(usuarios_cadastrados):
    print("-" * 30)
    while True:
        nome = input('Nome: ')
        if nome.strip():
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


def salvar_arquivo(materias, emailusuario):
    f = open(f'save-{emailusuario}.txt', 'w')
    for materia in materias:
        if (materia['autor'] == emailusuario):
            f.write('-' * 40)
            f.write(f"\nID: {materia['id']}\n")
            f.write(f"Titulo: {materia['titulo']}\n")
            f.write(f"Autor: {materia['autor']}\n")
            f.write(f"Data: {materia['data']}\n")
            f.write(f"Conteudo: {materia['conteudo']}\n")
            if materia['comentarios'] > []:
                f.write('------COMENTARIO(S)------')
                for comentarios in materia['comentarios']:
                    f.write(f"\nUsuario: {comentarios['usuario']}\n")
                    f.write(f"Comentario: {comentarios['comentario']}\n")
            if materia['curtidas'] > []:
                f.write(f'\n------CURTIDA(S)------')
                cont = 0
                for i in materia['curtidas']:
                    cont += 1
                f.write(f"\nCurtidas: {cont}\n")
                for curtidas in materia['curtidas']:
                    f.write(f"\nUsuarios: {curtidas}")
    f.close()
    print('Arquivo salvo')
    webbrowser.open(f"file:///D:/Area de Trabalho/projeto/save-{emailusuario}.txt")


def imprimir_arquivo(materias, emailusuario):
    f = open(f'print-{emailusuario}.txt', 'w')
    for materia in materias:
            f.write('-' * 40)
            f.write(f"\nID: {materia['id']}\n")
            f.write(f"Titulo: {materia['titulo']}\n")
            f.write(f"Autor: {materia['autor']}\n")
            f.write(f"Data: {materia['data']}\n")
            f.write(f"Conteudo: {materia['conteudo']}\n")
            if materia['comentarios'] > []:
                f.write('------COMENTARIO(S)------')
                for comentarios in materia['comentarios']:
                    f.write(f"\nUsuario: {comentarios['usuario']}\n")
                    f.write(f"Comentario: {comentarios['comentario']}\n")
            if materia['curtidas'] > []:
                f.write(f'\n------CURTIDA(S)------')
                cont = 0
                for i in materia['curtidas']:
                    cont += 1
                f.write(f"\nCurtidas: {cont}\n")
                for curtidas in materia['curtidas']:
                    f.write(f"\nUsuarios: {curtidas}")
    f.close()
    webbrowser.open(f"file:///D:/Area de Trabalho/projeto/print-{emailusuario}.txt")