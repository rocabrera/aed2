from estruturas import MyArray

def question4():

    """
    Supõem-se que só podemos inserir elementos no final do array.
    """
    array = MyArray([1,2,3])
    menu_separator = "#"*32
    menu = f"""{menu_separator}
Digite uma das opções:
1-) Inserir elemento no array.
2-) Apresentar array.
3-) Informar elemento a ser buscado.
4-) Sair do programa.\nEscolha: """

    while True:
        choice = input(menu)
        if choice == '1':
            element = input("Elemento para adicionar: ")
            array.insert(int(element))
            print("Elemento adicionado.\n")
        elif choice == '2':
            array.show("Lista: ")
        elif choice == '3':
            element = input("Elemento procurado: ")
            search = array.binary_search(int(element))
            msg = f"Indice: {search}" if search is not None else "Not found"
            print(msg)
        elif choice == '4':
            break

    print("Programa finalizado.")
    

if __name__ == "__main__":
    question4()