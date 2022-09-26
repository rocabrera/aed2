from estruturas import MyQueue


def question6():

    lista = [7,6,3,4,4,2,3,1]
    f1_original = MyQueue(lista)
    f1 = MyQueue(lista)
    f2 = MyQueue()
    
    menu_separator = "#"*32
    menu = f"""{menu_separator}
Digite uma das opções:
1-) Inserir elemento na fila F1.
2-) Apresentar fila F1 original.
3-) Apresentar a fila F1 após a remoção dos números pares.
4-) Apresentar a fila F2 após a inserção dos elementos pares.
5-) Sair do programa.\nEscolha: """

    while True:
        choice = input(menu)
        if choice == '1':
            element = input("Elemento para adicionar: ")
            p1.insert(int(element))
            print("Elemento adicionado.\n")

        elif choice == '2':
            f1_original.show("Fila F1 original: ")

        elif choice == '3':
            temp = MyQueue()
            element = f1.pop()
            while element != "Stop":
                if element%2==0:
                    temp.insert(element)
                else:
                    f2.insert(element)
                element = f1.pop()
            f1 = temp
            f1.show("Pilha P1 após remoção: ")

        elif choice == '4':
            f2.show("Pilha P2: ")
            
        elif choice == '5':
            break

    print("Programa finalizado.")
    

if __name__ == "__main__":
    question6()