# Notas do Aluno
notas = [6.0, 7.0, 9.0, 5.0]


# Função para calcular média e verificar situação
def boletim(lista):
    media = sum(lista) / len(lista)

    if media >= 6:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    return (media, situacao)


# Verificando valores da função
print(boletim(notas))
media, situacao = boletim(notas)

# Output da média e da situação do aluno
print(f"O estudante atingiu a média {media} e foi {situacao}")
