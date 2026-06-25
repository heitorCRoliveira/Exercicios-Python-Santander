def media(lista: list = [0]) -> float:

    calculo = sum(lista) / len(lista)

    if len(lista) > 4:
        raise ValueError("A lista náo pode possuir mais de quatro notas")

    return calculo


try:
    notas = [6, 7, 8, 9, 10]

    resultado = media(notas)
except TypeError:
    print(
        "Não foi possível calculas a média do estudante. Só são aceitos valores numéricos!"
    )


except ValueError as e:

    print(e)
else:
    print(resultado)
finally:
    print("A consulta foi encerrada!")
