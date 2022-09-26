from estruturas import MyArray

def question7():

    """
    Supõem-se que só podemos inserir elementos no final do array.
    """
    array = MyArray([1,2,3,2,2,3,4,1,1,2])
    menu_separator = "#"*32
    menu = f"""{menu_separator}
Digite uma das opções:
1-) Inserir elemento no array.
2-) Apresentar array.
3-) Apresentar a moda e informar quantas vezes ela se repete no array.
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
            key, value = array.find_mode()
            print(f"Moda: {key}; Amount: {value}\n")
        elif choice == '4':
            break

    print("Programa finalizado.")
    

if __name__ == "__main__":
    question7()