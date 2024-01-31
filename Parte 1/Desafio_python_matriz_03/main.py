def mediana_matrizes_classificadas(matriz1, matriz2):

    # Combina as matrizes em uma única matriz
    matriz_combinada = matriz1 + matriz2
    matriz_ordenada = sorted(matriz_combinada)

    print("Matriz ordenada: ", matriz_ordenada)

    # Calcula o tamanho da matriz
    tamanho = len(matriz_ordenada)

    # Encontra o índice do elemento central da matriz combinada
    indice_central = tamanho // 2

    # Se o tamanho da matriz for ímpar, a mediana é o elemento central
    if tamanho % 2 == 1:
        return matriz_ordenada[indice_central]

    # Se o tamanho da matriz for par, a mediana é a média dos dois elementos centrais
    else:
        return (matriz_ordenada[indice_central] + matriz_ordenada[indice_central - 1]) / 2


# Exemplo de uso
matriz1 = [9,11,16]
matriz2 = [7, 2]

mediana = mediana_matrizes_classificadas(matriz1, matriz2)

print("Matriz A: ", matriz1)
print("Matriz B: ",matriz2)

print("Mediana das matrizes combinadas: ", mediana)

