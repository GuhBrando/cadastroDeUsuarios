def exibirMenu():
    print("----- Opções de procedimento -----")
    print("1 - Cadastrar novos usuários.")
    print("2 - Exibir usuários cadastrados.")
    print("3 - Procurar um usuário cadastrado.")
    print("4 - Remover usuário do sistema.")
    print("5 - Alterar nome de usuário cadastrado.")
    print("6 - Finalização programa.")

def cadastrarUsuario():
    listaTemp = []
    nomeUsuario = input('Digite o nome do usuario: ').capitalize()
    emailUsuario = input('Digite o email do usuario: ')
    dadosUsuario = (nomeUsuario,emailUsuario)
    listaTemp.append(list(dadosUsuario))
    print('Usuario Adicionado')
    return listaTemp

def exibirUsuariosCadastrados(listaUsuarios):
    for registro in listaUsuarios:
        print("Nome: " + registro[0][0] + " | Email do usuário cadastrado: " + registro[0][1])

def exibirUsuariosEmOrdemAlfabetica(listaUsuarios):
    listaOrdenada=sorted(listaUsuarios)
    for registro in listaOrdenada:
        print("Nome: " + registro[0][0] + " | Email do usuário cadastrado: " + registro[0][1])

def pesquisarUsuario(pesquisaUsuario, listaUsuarios):
    for registro in listaUsuarios:
        if pesquisaUsuario.lower() == registro[0][0].lower():
            print(pesquisaUsuario,"está na cadastrado(a)")
            return
        else:
            print("Usuário não encontrado ou não cadastrado no sistema")

def deletarUsuario(registroDelecao, listaUsuariosCadastratros):
    count = 0
    while count < len(listaUsuariosCadastratros):
        for registro in listaUsuariosCadastratros:
            if registroDelecao.lower() == registro[0][1].lower():
                listaUsuariosCadastratros.pop(count)
                print("Usuario " + registroDelecao + " deletado")
                return
            count += 1
    print("Usuário não encontrado ou não cadastrado no sistema")

def alterarUsuarioCadastrado(registroAlteracao, listaUsuariosCadastratros):
    count = 0
    for registro in listaUsuariosCadastratros:
        if registroAlteracao == registro[count][1]:
            novoNome = input("Digite o Novo Nome: ")
            registro[count][0] = novoNome
            print("Usuário alterado com sucesso.")
            return
    print("Usuário não encontrado ou não cadastrado no sistema")

def main():
    listaUsuariosCadastratros = []
    print("Bem vindo ao sistema de cadastro de usuário da UAM.")
    opçãoProcedimento = 0
    while opçãoProcedimento != 6:
        opçãoProcedimento = 0
        try:
            exibirMenu()
            opçãoProcedimento = int(input("Digite o procedimento que gostaria de executar: "))
        except:
            opçãoProcedimento == 0
        if opçãoProcedimento == 1:
            #H1
            listaUsuariosCadastratros.append(cadastrarUsuario())
        elif opçãoProcedimento == 2:
            formaDeExibicaoUsuariosCadastrados = 0
            print("1 - Exibir em ordem de cadastro")
            print("2 - Ordem Alfabetica")
            while formaDeExibicaoUsuariosCadastrados != 1 and formaDeExibicaoUsuariosCadastrados != 2:
                try:
                    formaDeExibicaoUsuariosCadastrados = 0
                    formaDeExibicaoUsuariosCadastrados = int(input("Digite a opção desejada: "))
                except:
                    formaDeExibicaoUsuariosCadastrados = 0
                if formaDeExibicaoUsuariosCadastrados == 1:
                    #H2
                    exibirUsuariosCadastrados(listaUsuariosCadastratros)
                elif formaDeExibicaoUsuariosCadastrados == 2:
                    #H3
                    exibirUsuariosEmOrdemAlfabetica(listaUsuariosCadastratros)
                else:
                    print("Opção inválida, digite novamente.")
        elif opçãoProcedimento == 3:
            #H4
            procuraUsuario = input("Digite o nome do usuário que deseja procurar: ")
            pesquisarUsuario(procuraUsuario, listaUsuariosCadastratros)
        elif opçãoProcedimento == 4:
            #H5
            delecaoUsuario = input("Digite o EMAIL do usuário que deseja deletar: ")
            deletarUsuario(delecaoUsuario, listaUsuariosCadastratros)
        elif opçãoProcedimento == 5:
            #H6
            alterarRegistroUsuario = input("Para alterar o nome de um usuário, digite o EMAIL desejado: ")
            alterarUsuarioCadastrado(alterarRegistroUsuario, listaUsuariosCadastratros)
        elif opçãoProcedimento == 6:
            print("Fim do programa.")
            print("Universidade Anhembi Morumbi agradece!")
        else:
            print("Opção Invalida, digite novamente.")

if __name__ == "__main__":
    main()