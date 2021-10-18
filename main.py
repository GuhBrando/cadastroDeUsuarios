def exibirMenu():
    print("----- Opções de procedimento -----")
    print("1 - Cadastrar novos usuários.")
    print("2 - Exibir usuários cadastrados.")
    print("3 - Procurar um usuário cadastrado.")
    print("4 - Remover usuário do sistema.")
    print("5 - Alterar nome de usuário cadastrado.")
    print("6 - Finalização programa.")

def exibirUsuariosCadastrados():
    print(usuarios)

def cadastrarUsuario():
    usuario_nome = input('Digite o nome do usuario: ')
    usuario_email = input('Digite o email do usuario: ')
    usuario_dados = (usuario_nome,usuario_email)
    usuarios.append(usuario_dados)
    print(usuarios)
    print('Usuario Adicionado')

def exibirUsuariosEmOrdemAlfabetica(listaCadastro):
    ordenado=sorted(listaCadastro)
    print(ordenado)

def procurarUsuario(Nome):
    backup = listaNomes 
    if Nome in backup:
        print(Nome,"Está na lista")
    else:
         print("Não encontrado")
    
def main():
    print("Bem vindo ao sistema de cadastro de usuário da UAM.")
    opçãoProcedimento = 0
    while opçãoProcedimento != 6:
        try:
            exibirMenu()
            opçãoProcedimento = int(input("Digite o procedimento que gostaria de executar: "))
        except:
            opçãoProcedimento == 0
        if opçãoProcedimento == 1:
            #H1
            cadastrarUsuario()
        elif opçãoProcedimento == 2:
            formaDeExibicaoUsuariosCadastrados = 0
            print("1 - Exibir em ordem de cadastro")
            print("2 - Ordem Alfabetica")
            while formaDeExibicaoUsuariosCadastrados != 1 and formaDeExibicaoUsuariosCadastrados != 2:
                try:
                    formaDeExibicaoUsuariosCadastrados = int(input("Digite a opção desejada: "))
                except:
                    formaDeExibicaoUsuariosCadastrados = 0
                if formaDeExibicaoUsuariosCadastrados == 1:
                    #H2
                    exibirUsuariosCadastrados()
                elif formaDeExibicaoUsuariosCadastrados == 2:
                    #H3
                    exibirUsuariosEmOrdemAlfabetica()
                else:
                    print("Opção inválida, digite novamente.")
        elif opçãoProcedimento == 3:
            #H4
            procurarUsuario()
        elif opçãoProcedimento == 4:
            #H5
            #deletarUsuario()
            print("H5")
        elif opçãoProcedimento == 5:
            #H6
            #alterarUsuarioCadastrado()
            print("H6")
        elif opçãoProcedimento == 6:
            print("Fim do programa.")
            print("Universidade Anhembi Morumbi agradece!")
        else:
            print("Opção Invalida, digite novamente.")

if __name__ == "__main__":
    main()
