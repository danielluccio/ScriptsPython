def posicaoLista():
    empty_list = []
    while True:
        entrada = int(input("Entre com valores inteiros: "))
        print("\nPara parar digite 00")
        if entrada:
            empty_list.append(entrada)

        elif entrada == 0:
            break
    return empty_list
    
lista_posicionada = posicaoLista()
for i, j in enumerate(lista_posicionada):
    print(f"Index[{i}], Valor: {j}")

