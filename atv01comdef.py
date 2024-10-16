# Crie uma função chamada verificar_paridade que receba um número inteiro como argumento e retorne uma mensagem indicando se o número é par ou ímpar.


def verificar_paridades(argumento):
    if argumento % 2 == 0:
        print("O número que você escolheu é par.")
    else:
        print("O número escolhido é impar.")
    return argumento

argumento = int(input("Coloque um número inteiro e direi se ele é impar ou par:"))
print(f"Seu número escolhido é:{verificar_paridades(argumento)}")