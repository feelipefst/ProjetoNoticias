import getpass  # senha sem exibir os caracteres

# Cria um dicionário vazio para armazenar os usuários
usuarios = {}

# Cria uma lista vazia para armazenar as matérias
materias = []

# Define um contador de IDs para atribuir IDs únicos a cada matéria
id_materia = 1

# Define as constantes para os tipos de usuário
TIPO_JORNALISTA = "jornalista"
TIPO_LEITOR = "leitor"

usuario_logado = None


def cadastrar():
    # Solicita informações do usuário
    nome = input('Digite seu nome: ')

    # Solicita o email do usuário e realiza a verificação
    while True:
        email = input('Digite o email: ')
        if '@' in email and email not in usuarios:
            break
        elif '@' not in email:
            print('Email inválido. Tente novamente')
        else:
            print('Email já cadastrado. Informe outro')

    # Solicita a senha do usuário e realiza a validação
    while True:
        print('----------------------------------------')
        print('Informe uma senha que contenha ao menos 6 caracteres incluindo letras e números')
        senha = getpass.getpass('Digite a senha: ')
        # Solicita o tipo de usuário (comum ou administrador)
        print('Escolha o tipo de usuário: ')
        print("1. Jornalista")
        print("2. Leitor")

        # Valida o tipo de usuario
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

        if (validar_senha(senha)):
            break
        else:
            print('Senha inválida. Digite novamente')

    # Cria um novo usuário com as informações fornecidas
    usuario = {
        'nome': nome,
        'email': email,
        'senha': senha,
        'tipo': tipo_usuario
    }

    # Adiciona o usuário ao dicionário de usuários
    usuarios[email] = usuario
    print('Usuário cadastrado com sucesso')


def escrever_materia(usuario):
    global id_materia

    if usuario['tipo'] == TIPO_JORNALISTA:
        titulo = input('Digite o titulo da matéria: ')
        conteudo = input('Digite o texto: ')
        # Obtém a data atual
        data_materia = input('Digite a data da matéria (no formato DD/MM/AAAA): ')

        materia = {
            'id': id_materia,
            'titulo': titulo,
            'conteudo': conteudo,
            'data': data_materia
        }
        # Incrementa o contador de IDs para a próxima matéria
        id_materia += 1

        materias.append(materia)
        print('Materia escrita com sucesso!')
    else:
        print('Você não tem permissão para escrever matéria')


def fazer_login():
    # Solicita o email do usuário a ser buscado
    global usuario_logado  # Indica que estamos usando a variável global
    email = input('Email: ')
    senha = getpass.getpass('Senha: ')

    # Verifica se o email está no dicionário de usuários
    if email in usuarios and usuarios[email]['senha'] == senha:
        print('Login feito com sucesso')
        print('Bem vindo', usuarios[email]['nome'])
        usuario_logado = usuarios[email]  # Define o usuário logado
        return True
    else:
        print('Credenciais inválidas')
        return False


def validar_senha(senha):
    # Valida a senha com base em regras específicas
    if len(senha) >= 6 and any(char.isalpha() for char in senha) and any(char.isdigit() for char in senha):
        return True
    else:
        return False


def excluir_noticia():
    if len(materias) == 0:
        print('Não há matérias disponíveis para excluir.')
        return

    listar_noticias()  # Mostra a lista de notícias para que o usuário veja os IDs
    id_a_excluir = input('Digite o ID da notícia: ')

    # Verifica se o ID é um número válido
    if not id_a_excluir.isdigit():
        print('ID inválido. Digite um número válido')
        return
    id_a_excluir = int(id_a_excluir)

    # Procura a notícia com base no ID
    for materia in materias:
        if materia['id'] == id_a_excluir:
            materias.remove(materia)
            print(f'Noticia com ID {id_a_excluir} excluida com sucesso.')
            return
    print(f'Noticia com ID {id_a_excluir} não encontrada. ')


def editar_materia():
    global id_materia

    if usuario_logado['tipo'] != TIPO_JORNALISTA:
        print('Você não tem permissão para editar matérias. ')
        return
    if len(materias) == 0:
        print('Não há matérias disponíveis para editar. ')
        return

    listar_noticias()  # Mostra a lista de notícias para que o usuário veja os IDs
    id_a_editar = input('Qual id da matéria a ser editada: ')

    # Verifica se o ID é um número válido
    if not id_a_editar.isdigit():
        print('ID inválido. Digite um número válido.')
        return
    id_a_editar = int(id_a_editar)

    # Procura a matéria com base no ID
    for materia in materias:
        if materia['id'] == id_a_editar:
            print(f'Editando matéria com ID {id_a_editar}.')
            novo_titulo = input('Digite o novo título: ')
            novo_conteudo = input('Digite o novo conteúdo: ')
            nova_data = input('Digite a nova data (no formato DD/MM/AAAA): ')

            materia['titulo'] = novo_titulo
            materia['conteudo'] = novo_conteudo
            materia['data'] = nova_data

            print(f'Matéria com ID {id_a_editar} editada com sucesso.')
            return
    print(f'Matéria com ID {id_a_editar} não encontrada')


def menu_jornalista(usuario):
    while True:
        print('\nOpções: ')
        print('1 - Escrever matéria')
        print('2 - Visualizar matérias')
        print('3 - Excluir matéria')
        print('4 - Editar matéria')
        print('5 - Sair')
        opcao = input('Digite uma opção: ')

        if (opcao == '1'):
            escrever_materia(usuario)
        if (opcao == '2'):
            listar_noticias()
        elif (opcao == '3'):
            excluir_noticia()  # Chamando a função para excluir notícias
        elif (opcao == '4'):
            editar_materia()
        elif (opcao == '5'):
            print('Saindo do sistema')
            break
        else:
            print('Opção inválida. Selecione novamente')


def listar_noticias():
    if len(materias) == 0:
        print('Não há matérias disponíveis no momento')
    else:
        print('Lista de materias:')
        for materia in materias:
            print(f"ID: {materia['id']}")
            print(f"Título: {materia['titulo']}")
            print(f"Data: {materia['data']}")
            print(f"Conteúdo: {materia['conteudo']}\n")


def menu_leitor(usuario_logado):
    while True:
        print('\nOpções: ')
        print('1 - Visualizar matérias')
        print('2 - Sair')
        opcao = input('Digite uma opção: ')

        if (opcao == '1'):
            listar_noticias()
        elif (opcao == '2'):
            print('Saindo do sistema')
            break
        else:
            print('Opção inválida. Selecione novamente')


def main():
    global usuario_logado

    while True:
        print('Escolha uma opção')
        print("1. Cadastrar Usuário")
        print("2. Fazer login")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar()
        elif opcao == '2':
            if fazer_login():
                if usuario_logado['tipo'] == TIPO_JORNALISTA:
                    menu_jornalista(usuario_logado)
                else:
                    menu_leitor(usuario_logado)

        elif opcao == '3':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if _name_ == "_main_":
    main()