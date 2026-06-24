entrada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

tabuada = int(input("Digite qual tabuada você quer visualizar: "))


resultado = map(lambda x: x * tabuada, entrada)

resultado = list(resultado)

print(
    f"A tabuada de {tabuada} é: {resultado[0]}, {resultado[1]}, {resultado[2]}, {resultado[3]}, {resultado[4]}, {resultado[5]},{resultado[6]} ,{resultado[7]} ,{resultado[8]}, {resultado[9]}"
)
