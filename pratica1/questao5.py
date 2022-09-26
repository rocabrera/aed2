from estruturas import MyStack


def transfer_stack(temp_stack: MyStack, new_stack: MyStack):
    
    element = temp_stack.pop()
    while element != "Stop":
        new_stack.insert(element)
        element = temp_stack.pop()


def question5():

    lista = [5,6,3,4,2,1,7]
    p1_original = MyStack(lista)
    p1 = MyStack(lista)
    p2 = MyStack()
    
    menu_separator = "#"*32
    menu = f"""{menu_separator}
Digite uma das opções:
1-) Inserir elemento na pilha P1.
2-) Apresentar pilha P1 original.
3-) Apresentar a pilha P1 após a remoção dos números
pares.
4-) Apresentar a pilha P2 após a inserção dos elementos pares.
5-) Sair do programa.\nEscolha: """

    while True:
        choice = input(menu)
        if choice == '1':
            element = input("Elemento para adicionar: ")
            p1.insert(int(element))
            print("Elemento adicionado.\n")

        elif choice == '2':
            p1_original.show("Pilha P1 original: ")

        elif choice == '3':
            even_stack = MyStack()
            odd_stack = MyStack()

            element = p1.pop()
            while element != "Stop":
                if element%2==0:
                    even_stack.insert(element)
                else:
                    odd_stack.insert(element)
                element = p1.pop()

            transfer_stack(odd_stack, p1)
            transfer_stack(even_stack, p2)
            
            p1.show("Pilha P1 após remoção: ")

        elif choice == '4':
            p2.show("Pilha P2: ")
            
        elif choice == '5':
            break

    print("Programa finalizado.")
    

if __name__ == "__main__":
    question5()