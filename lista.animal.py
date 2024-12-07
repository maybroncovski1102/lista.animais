def mostrar_animais(animais):
    """
    Exibe a lista de animais cadastrados.
    """
    if not animais:
        print("\nNenhum animal na lista.")
    else:
        print("\nLista de Animais:")
        for i, animal in enumerate(animais, 1):
            print(f"{i}. {animal['nome']} - {animal['descricao']}")

def adicionar_animal(animais):
    """
    Adiciona um novo animal à lista.
    """
    nome = input("\nDigite o nome do animal: ").strip()
    descricao = input("Digite a descrição do animal: ").strip()
    
    if nome and descricao:
        animal = {"nome": nome, "descricao": descricao}
        animais.append(animal)
        print(f"\nAnimal '{nome}' adicionado com sucesso!")
    else:
        print("\nErro: Nome e descrição não podem estar em branco.")

def editar_animal(animais):
    """
    Edita as informações de um animal existente na lista.
    """
    mostrar_animais(animais)
    if not animais:
        return
    
    try:
        indice = int(input("\nDigite o número do animal que deseja editar: ")) - 1
        if 0 <= indice < len(animais):
            animal = animais[indice]
            print(f"\nEditando: {animal['nome']} - {animal['descricao']}")
            
            novo_nome = input("Novo nome (deixe em branco para manter o atual): ").strip()
            nova_descricao = input("Nova descrição (deixe em branco para manter a atual): ").strip()
            
            if novo_nome:
                animal["nome"] = novo_nome
            if nova_descricao:
                animal["descricao"] = nova_descricao

            print(f"\nAnimal editado com sucesso! Novo cadastro: {animal['nome']} - {animal['descricao']}")
        else:
            print("\nErro: Número inválido.")
    except ValueError:
        print("\nErro: Entrada inválida. Digite um número válido.")

def excluir_animal(animais):
    """
    Exclui um animal da lista.
    """
    mostrar_animais(animais)
    if not animais:
        return

    try:
        indice = int(input("\nDigite o número do animal que deseja excluir: ")) - 1
        if 0 <= indice < len(animais):
            animal = animais.pop(indice)
            print(f"\nAnimal '{animal['nome']}' excluído com sucesso!")
        else:
            print("\nErro: Número inválido.")
    except ValueError:
        print("\nErro: Entrada inválida. Digite um número válido.")

def menu():
    """
    Exibe o menu principal e gerencia as opções.
    """
    animais = []  # Lista de animais
    
    while True:
        print("\nMenu de Opções:")
        print("1. Mostrar lista de animais")
        print("2. Adicionar um novo animal")
        print("3. Editar um animal existente")
        print("4. Excluir um animal")
        print("5. Sair")
        
        opcao = input("Escolha uma opção (1-5): ").strip()
        
        if opcao == "1":
            mostrar_animais(animais)
        elif opcao == "2":
            adicionar_animal(animais)
        elif opcao == "3":
            editar_animal(animais)
        elif opcao == "4":
            excluir_animal(animais)
        elif opcao == "5":
            print("\nSaindo do programa... Até logo!")
            break
        else:
            print("\nErro: Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()