def exibirAlfabeto(listaCadastro):
    ordenado=sorted(listaCadastro)
    print(ordenado)

def verificaUsuario(Nome):
    backup = listaNomes 
    if Nome in backup:
        print(Nome,"Está na lista")
    else:
         print("Não encontrado")
        



listaNomes = ['bela','agatha','gloria','carlo']

exibirAlfabeto(listaNomes)

verificaUsuario("bela")