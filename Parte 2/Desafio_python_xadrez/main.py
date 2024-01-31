def n_rainhas(n):

    # Verifica se o tamanho do tabuleiro é válido
    if n < 1:
        raise ValueError("O tamanho do tabuleiro deve ser maior ou igual a 1")

    # Cria uma matriz vazia para representar o tabuleiro
    matriz = [[False for i in range(n)] for j in range(n)]

    # Chama a função recursiva para resolver o quebra-cabeça
    numero_solucoes = n_rainhas_recursiva(matriz, 0)

    return numero_solucoes


def n_rainhas_recursiva(matriz, coluna):

    # Se todas as colunas estiverem preenchidas, encontramos uma solução
    if coluna == len(matriz):
        return 1

    # Para cada linha possível, tentamos colocar uma rainha na coluna atual
    numero_solucoes = 0
    for linha in range(len(matriz)):
        # Verifica se a rainha pode ser colocada na linha e na coluna atuais
        if pode_colocar_rainha(matriz, linha, coluna):
            # Coloca a rainha na linha e na coluna atuais
            matriz[linha][coluna] = True

            # Chama a função recursiva para resolver o quebra-cabeça para as próximas colunas
            numero_solucoes += n_rainhas_recursiva(matriz, coluna + 1)

            # Remove a rainha da linha e da coluna atuais
            matriz[linha][coluna] = False

    return numero_solucoes


def pode_colocar_rainha(matriz, linha, coluna):

    # Verifica se há outra rainha na mesma linha
    for i in range(len(matriz)):
        if i != linha and matriz[i][coluna]:
            return False

    # Verifica se há outra rainha na mesma coluna
    for i in range(len(matriz)):
        if i != coluna and matriz[linha][i]:
            return False

    # Verifica se há outra rainha na diagonal principal
    i = linha - 1
    j = coluna - 1
    while i >= 0 and j >= 0:
        if matriz[i][j]:
            return False
        i -= 1
        j -= 1

    # Verifica se há outra rainha na diagonal secundária
    i = linha + 1
    j = coluna + 1
    while i < len(matriz) and j < len(matriz):
        if matriz[i][j]:
            return False
        i += 1
        j += 1

    return True


def main():
    n = int(input("Informe o tamanho do tabuleiro: "))
    numero_solucoes = n_rainhas(n)
    print("Numero de soluções: ", numero_solucoes)

if __name__ == "__main__":
    main()


