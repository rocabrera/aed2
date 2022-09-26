from estruturas import MyArray

def question3():

    """
    Supõem-se que só podemos inserir elementos no final do array.
    """
    array = MyArray([1,2,3])
    menu_separator = "#"*32
    menu = f"""{menu_separator}
Digite uma das opções:
1-) Inserir elemento no array.
2-) Apresentar array original.
3-) Apresentar array invertido.
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
            array.invert_show("Lista invertida: ")
        elif choice == '4':
            break

    print("Programa finalizado.")
    

if __name__ == "__main__":
    question3()