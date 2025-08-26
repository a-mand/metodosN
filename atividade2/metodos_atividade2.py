import sys


def imprimir_matriz(matriz):
    """Imprime a matriz formatada."""
    for linha in matriz:
        print(" ".join([f"{x:8.2f}" for x in linha]))
    print("-" * 40)

def trocar_linhas(matriz, l1, l2):
    """Troca duas linhas da matriz."""
    matriz[l1], matriz[l2] = matriz[l2], matriz[l1]

def escalonar(matriz, m, n):
    """
    Reduz a matriz à forma escalonada.
    """
    matriz_temp = [list(linha) for linha in matriz]  # Cria uma cópia para não modificar a original
    linha_pivo = 0
    
    for coluna in range(n):
        if linha_pivo >= m:
            break
        
        # 2.1) Encontrar pivô não nulo e trocar as linhas
        if matriz_temp[linha_pivo][coluna] == 0:
            encontrar_linha_nao_nula = -1
            for i in range(linha_pivo + 1, m):
                if matriz_temp[i][coluna] != 0:
                    encontrar_linha_nao_nula = i
                    break
            
            if encontrar_linha_nao_nula != -1:
                trocar_linhas(matriz_temp, linha_pivo, encontrar_linha_nao_nula)
            else:
                continue # Pular para a próxima coluna se todos os elementos abaixo forem zero
        
        if matriz_temp[linha_pivo][coluna] == 0:
            continue

        # 2.2) e 2.5) Eliminar elementos abaixo do pivô
        for i in range(linha_pivo + 1, m):
            if matriz_temp[i][coluna] != 0:
                fator = matriz_temp[i][coluna] / matriz_temp[linha_pivo][coluna]
                for j in range(coluna, n + 1):
                    matriz_temp[i][j] = matriz_temp[i][j] - fator * matriz_temp[linha_pivo][j]

        # 2.3) Verificar inconsistência
        # Se um pivô se tornou zero durante a eliminação e o termo constante não é
        # zero, o sistema é inconsistente.
        if matriz_temp[linha_pivo][coluna] == 0 and matriz_temp[linha_pivo][n] != 0:
            print("Sistema inconsistente detectado!")
            return None # Retorna None para indicar que não há solução
        
        print(f"Matriz após processar coluna {coluna}:")
        imprimir_matriz(matriz_temp)
        
        linha_pivo += 1
    
    # 2.4) Remover linhas nulas
    matriz_limpa = []
    inconsistente = False
    for linha in matriz_temp:
        # Verifica se a linha é inconsistente (0...0 | b), com b != 0
        if all(abs(x) < 1e-9 for x in linha[:-1]) and abs(linha[-1]) > 1e-9:
            inconsistente = True
            break
        # Adiciona a linha se não for toda zero
        if any(abs(x) > 1e-9 for x in linha):
            matriz_limpa.append(linha)

    if inconsistente:
        print("Sistema inconsistente detectado!")
        return None

    print("Matriz escalonada final:")
    imprimir_matriz(matriz_limpa)

    return matriz_limpa

def canonizar(matriz_escalonada, m, n):
    """
    Reduz a matriz escalonada para a forma canônica.
    """
    r = len(matriz_escalonada)
    matriz_canonizada = [list(linha) for linha in matriz_escalonada]

    for i in range(r - 1, -1, -1):
        pivo_j = -1
        for j in range(n):
            if abs(matriz_canonizada[i][j]) > 1e-9:
                pivo_j = j
                break
        
        if pivo_j != -1:
            # Normalizar o pivô para 1
            fator_normalizacao = matriz_canonizada[i][pivo_j]
            for j in range(pivo_j, n + 1):
                matriz_canonizada[i][j] /= fator_normalizacao
            
            # Anular elementos acima do pivô
            for k in range(i - 1, -1, -1):
                fator_eliminacao = matriz_canonizada[k][pivo_j]
                for j in range(pivo_j, n + 1):
                    matriz_canonizada[k][j] -= fator_eliminacao * matriz_canonizada[i][j]

    print("Matriz na forma canônica:")
    imprimir_matriz(matriz_canonizada)
    return matriz_canonizada

def analisar_solucao(matriz_canonizada, n):
    """
    Analisa a matriz na forma canônica e imprime a solução.
    """
    r = len(matriz_canonizada)
    
    if r == n:
        print("O sistema tem uma única solução.")
        solucao = [linha[n] for linha in matriz_canonizada]
        print(f"Solução: {solucao}")
    else:
        print("O sistema tem infinitas soluções.")
        variaveis_livres = n - r
        print(f"Quantidade de variáveis livres: {variaveis_livres}")
        
        pivos = [next((j for j, val in enumerate(linha) if abs(val) > 1e-9), -1) for linha in matriz_canonizada]
        
        solucao_geral = [""] * n
        letras = [f"t{i+1}" for i in range(variaveis_livres)]
        letra_idx = 0
        
        variavel_is_pivo = [False] * n
        for p in pivos:
            if p != -1:
                variavel_is_pivo[p] = True
        
        for j in range(n):
            if not variavel_is_pivo[j]:
                solucao_geral[j] = letras[letra_idx]
                letra_idx += 1
        
        for i in range(r):
            pivo_j = pivos[i]
            expressao = f"{matriz_canonizada[i][n]:.2f}"
            for j in range(pivo_j + 1, n):
                if abs(matriz_canonizada[i][j]) > 1e-9:
                    if matriz_canonizada[i][j] < 0:
                        expressao += f" + {-matriz_canonizada[i][j]:.2f}*{solucao_geral[j]}"
                    else:
                        expressao += f" - {matriz_canonizada[i][j]:.2f}*{solucao_geral[j]}"
            solucao_geral[pivo_j] = expressao

        print("Solução geral:")
        for idx, val in enumerate(solucao_geral):
            print(f"x{idx+1} = {val}")

def main():
    try:
        m = int(input("Digite o número de equações (m): "))
        n = int(input("Digite o número de incógnitas (n): "))
        matriz = []
        print("Digite os elementos da matriz aumentada (linha por linha):")
        for i in range(m):
            linha = list(map(float, input(f"Linha {i+1}: ").split()))
            if len(linha) != n + 1:
                print(f"Erro: A linha deve ter {n+1} elementos. Tente novamente.")
                sys.exit(1)
            matriz.append(linha)
        
        matriz_escalonada = escalonar(matriz, m, n)
        
        if matriz_escalonada:
            matriz_canonizada = canonizar(matriz_escalonada, m, n)
            analisar_solucao(matriz_canonizada, n)
            
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números.")

if __name__ == "__main__":
    main()