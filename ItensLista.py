def contaItens() -> int:
    empty_list = []
    while True:
        entrada = int(input("Digite um numero inteiro: "))
        empty_list.append(entrada)
        if entrada == 00:
            break
    return len(empty_list)

contador = contaItens()
print(f"Quantidade de valores Inseridos: {contador - 1}")