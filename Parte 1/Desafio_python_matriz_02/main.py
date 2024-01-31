def mediana_matrizes_classificadas(matriz1, matriz2):

    # Verifica se as matrizes têm o mesmo tamanho
    if len(matriz1) != len(matriz2):
        raise ValueError("As matrizes devem ter o mesmo tamanho")

    # Matriz combinada
    matriz_combinada = matriz1 + matriz2
    # Matrix ordenada
    matriz_ordenada = sorted(matriz_combinada)
    
    # Calcula o tamanho da matriz
    tamanho = len(matriz_ordenada)

    # Combina as matrizes em uma única matriz
    matriz_combinada = matriz1 + matriz2
    matriz_ordenada = sorted(matriz_combinada)

    print("Matriz Combinada: ", matriz_combinada)
    print("Matriz Ordenada: ", matriz_ordenada)

    # Encontra a mediana da matriz combinada
    mediana = matriz_ordenada[tamanho // 2]

    return mediana


# Exemplo de uso
matriz1 = [1, 3, 5]
matriz2 = [2, 4, 6]

mediana = mediana_matrizes_classificadas(matriz1, matriz2)

print("Matriz A: ", matriz1)
print("Matriz B: ", matriz2)

print("Mediana das matrizes combinadas: ", mediana)

