# import numpy as np

def n_rainhas(n):
    if n <= 0:
        raise ValueError("O tamanho do tabuleiro deve ser maior ou igual a 1")

    # Cria uma matriz vazia para representar o tabuleiro
    matriz = [[False for i in range(n)] for j in range(n)]

    # Inicializa o vetor de colunas disponíveis
    colunas_disponiveis = [True] * n

    # Contador de soluções
    numero_solucoes = 0

    # Busca por soluções
    for linha in range(n):
        # Se não houver colunas disponíveis, não há mais soluções
        if not any(colunas_disponiveis):
            break

        # Tenta colocar uma rainha na linha atual
        for coluna in range(n):
            # Se a rainha pode ser colocada na linha e na coluna atuais,
            if pode_colocar_rainha(matriz, linha, coluna):
                # Coloca a rainha na linha e na coluna atuais
                matriz[linha][coluna] = True

                # Remove a coluna atual das colunas disponíveis
                colunas_disponiveis[coluna] = False

                # Incrementa o contador de soluções
                numero_solucoes += 1

                # Recursão
                n_rainhas(matriz, linha + 1, colunas_disponiveis)

                # Remove a rainha da linha e da coluna atuais
                matriz[linha][coluna] = False
                # Adiciona a coluna atual às colunas disponíveis
                colunas_disponiveis[coluna] = True

    return numero_solucoes


def pode_colocar_rainha(matriz, linha, coluna):
    # Verifica se há outra rainha na mesma linha
    for i in range(n):
        if i != linha and matriz[i][coluna]:
            return False

    # Verifica se há outra rainha na mesma coluna
    for i in range(n):
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
    while i < n and j < n:
        if matriz[i][j]:
            return False
        i += 1
        j += 1

    return True

def main():
    numero_solucoes = n_rainhas(8)
    print(numero_solucoes)

if __name__ == "__main__":
    main()

