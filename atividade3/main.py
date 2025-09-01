import numpy as np
from metodos_edo import rk_fehlberg
import matplotlib.pyplot as plt
from metodos_edo import (
    euler, heun_nao_iterativo, heun_iterativo, ponto_medio,
    nystrom, ralston, rk3, rk4
)

# Funções de auxílio para formatação e exibição
def print_table(x, y, y_exato, h_val, title, show_all=False):
    """Função para imprimir uma tabela formatada dos resultados"""
    print("-" * 80)
    print(f"| {title:<76} |")
    print("-" * 80)
    print(f"| h = {h_val:<73} |")
    print("-" * 80)
    print(f"| {'x':<10} | {'y (Método)':<20} | {'y (Exato)':<20} | {'Erro (%)':<15} |")
    print("-" * 80)
    
    display_points = np.arange(0, x[-1] + 0.1, 0.1)

    for i in range(len(x)):
        if show_all or np.isclose(x[i], display_points).any():
            y_true = y_exato(x[i])
            if y_true != 0:
                erro_percentual = abs((y[i] - y_true) / y_true) * 100
            else:
                erro_percentual = 0
            
            print(f"| {x[i]:<10.2f} | {y[i]:<20.8f} | {y_true:<20.8f} | {erro_percentual:<15.6f} |")

    print("-" * 80)

def plot_results(f, x0, y0, x_final, h, methods_to_plot, y_exata=None, title='Comparação de Métodos de EDO'):
    """Função para plotar os resultados"""
    plt.figure(figsize=(12, 8))
    
    if y_exata:
        x_true = np.linspace(x0, x_final, 500)
        y_true = y_exata(x_true)
        plt.plot(x_true, y_true, label='Solução Exata', color='black', linestyle='--')

    markers = ['o', 's', '^', 'x', '*', '+']
    
    for i, (method_name, method_func) in enumerate(methods_to_plot.items()):
        x_vals, y_vals = method_func(f, x0, y0, h, x_final)
        plt.plot(x_vals, y_vals, label=method_name, marker=markers[i], markersize=4, linestyle='-')
        
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

# ------------------------------------------------------------------------------------------------
# Aplicações (Exercícios)
# ------------------------------------------------------------------------------------------------

## 3.1) Reproduzir a Tabela 32-1 e estender até x=2.0
## 3.4) Resolver com o Método de Ralston
def problema_3_1_e_3_4():
    def f(x, y):
        return y - x
    def y_exata(x):
        return np.exp(x) + x + 1

    x0, y0 = 0, 2.0
    x_final = 2.0
    h_values = [0.1, 0.05, 0.01]

    # Item 3.1: Reproduzir a Tabela 32-1 (Método de Euler)
    print("--- 3.1) Reproduzindo Tabela 32-1 com Método de Euler (até x=2.0) ---")
    for h in h_values:
        x, y = euler(f, x0, y0, h, x_final)
        show_all = h == 0.1
        print_table(x, y, y_exata, h, "Método de Euler", show_all)

    # Item 3.4: Resolver o mesmo problema com Ralston
    print("\n--- 3.4) Resolvendo com o Método de Ralston (até x=2.0) ---")
    for h in h_values:
        x, y = ralston(f, x0, y0, h, x_final)
        show_all = h == 0.1
        print_table(x, y, y_exata, h, "Método de Ralston", show_all)

## 3.2) Reproduzir a Tabela 32-4 e estender até x=2.0
def problema_3_2():
    def f(x, y):
        return y - x
    def y_exata(x):
        return np.exp(x) + x + 1

    x0, y0 = 0, 2.0
    x_final = 2.0
    h_values = [0.1, 0.05, 0.01]
    
    print("\n--- 3.2) Reproduzindo Tabela 32-4 com Método de Heun (não iterativo) (até x=2.0) ---")
    for h in h_values:
        x, y = heun_nao_iterativo(f, x0, y0, h, x_final)
        show_all = h == 0.1
        print_table(x, y, y_exata, h, "Método de Heun", show_all)

## 3.3) Reproduzir a Tabela 32-8 e estender até x=2.0
def problema_3_3():
    def f(x, y):
        return y - x
    def y_exata(x):
        return np.exp(x) + x + 1

    x0, y0 = 0, 2.0
    x_final = 2.0
    h_values = [0.1, 0.05, 0.01]
    
    print("\n--- 3.3) Reproduzindo Tabela 32-8 com Método de Nystrom (até x=2.0) ---")
    for h in h_values:
        x, y = nystrom(f, x0, y0, h, x_final)
        show_all = h == 0.1
        print_table(x, y, y_exata, h, "Método de Nystrom", show_all)

## 3.5) Plotar um gráfico com os resultados
def problema_3_5():
    # EDO do problema 3.1, 3.2, 3.3 e da Figura 25.11
    def f(x, y):
        return -2*x**3 + 12*x**2 - 20*x + 8.5
    
    # Solução exata para essa EDO
    def y_exata(x):
        return -0.5*x**4 + 4*x**3 - 10*x**2 + 8.5*x + 1

    x0, y0 = 0, 1.0 # Condição inicial y(0)=1 para este problema
    x_final = 4.0 # A figura vai até x=4
    h = 0.01
    
    methods = {
        'Euler': euler,
        'Heun': heun_nao_iterativo,
        'Nystrom': nystrom,
        'Ralston': ralston
    }

    print("\n--- 3.5) Gerando gráfico de acordo com a FIGURA 25.11 ---")
    plot_results(f, x0, y0, x_final, h, methods, y_exata=y_exata, title="Comparação de Métodos de EDO")

## 3.6) Reproduzir as Tabelas 33-1 e 33-2
def problema_3_6():
    def f_33_1(x, y):
        return y - x
    def y_exata_33_1(x):
        return np.exp(x) + x + 1

    def f_33_2(x, y):
        return y
    def y_exata_33_2(x):
        return np.exp(x)

    x_final = 2.0
    h = 0.01

    print("\n--- 3.6) Reproduzindo Tabela 33-1 com RK3 (até x=2.0) ---")
    x, y = rk3(f_33_1, 0, 2.0, h, x_final)
    print_table(x, y, y_exata_33_1, h, "Método de RK3")

    print("\n--- 3.6) Reproduzindo Tabela 33-2 com RK4 (até x=2.0) ---")
    x, y = rk4(f_33_2, 0, 1.0, h, x_final)
    print_table(x, y, y_exata_33_2, h, "Método de RK4")

## 3.7) Plotar gráfico para as tabelas 33-1 e 33-2
def problema_3_7():
    def f_33_1(x, y):
        return y - x
    def y_exata_33_1(x):
        return np.exp(x) + x + 1

    def f_33_2(x, y):
        return y
    def y_exata_33_2(x):
        return np.exp(x)

    x_final = 2.0
    h = 0.01

    print("\n--- 3.7) Gerando gráfico comparativo para y' = y - x com RK3 e RK4 ---")
    methods_1 = {
        'RK3': rk3,
        'RK4': rk4
    }
    plot_results(f_33_1, 0, 2.0, x_final, h, methods_1, y_exata=y_exata_33_1, title="Comparação de Métodos para Tábua 33-1")
    
    print("\n--- 3.7) Gerando gráfico comparativo para y' = y com RK3 e RK4 ---")
    methods_2 = {
        'RK3': rk3,
        'RK4': rk4
    }
    plot_results(f_33_2, 0, 1.0, x_final, h, methods_2, y_exata=y_exata_33_2, title="Comparação de Métodos para Tábua 33-2")

## 3.8) Resolver os problemas 25.1 a 25.6 (exemplos)
def problema_3_8():
    """
    Resolve os problemas de 25.1 a 25.6 do livro de métodos numéricos.
    Apresenta os resultados em tabelas e gráficos.
    """
    print("\n--- 3.8) Resolvendo problemas 25.1 a 25.6 ---")
    
    # Problema 25.1: dy/dx = yx^2 - 1.1y, y(0)=1
    # Solução Exata: y = exp(x^3/3 - 1.1x)
    def f_25_1(x, y):
        return y * x**2 - 1.1 * y
    def y_exata_25_1(x):
        return np.exp(x**3 / 3 - 1.1 * x)

    x0, y0, x_final = 0, 1.0, 2.0
    h = 0.1
    print("\n--- Problema 25.1: y' = yx^2 - 1.1y, y(0)=1 ---")
    
    # Gráfico do Problema 25.1
    methods_25_1 = {
        'Euler': euler,
        'Heun': heun_nao_iterativo,
        'Ponto Médio': ponto_medio,
        'RK4': rk4,
    }
    plot_results(f_25_1, x0, y0, x_final, h, methods_25_1, y_exata=y_exata_25_1, title="Problema 25.1")
    
    # Problema 25.2: Use o método de Euler com h=0.5 e 0.25 para resolver o Problema 25.1.
    print("\n--- Problema 25.2: Comparação de h no Método de Euler para o Problema 25.1 ---")
    h_values_25_2 = [0.5, 0.25]
    
    # Gráfico do Problema 25.2
    methods_25_2 = {
        'Euler h=0.5': lambda f, x0, y0, h_val, x_final: euler(f, x0, y0, 0.5, x_final),
        'Euler h=0.25': lambda f, x0, y0, h_val, x_final: euler(f, x0, y0, 0.25, x_final)
    }
    plot_results(f_25_1, x0, y0, x_final, h_values_25_2[0], methods_25_2, y_exata=y_exata_25_1, title="Problema 25.2")
    
    # Problema 25.3: Use o método de Heun com h=0.5 para resolver o Problema 25.1.
    print("\n--- Problema 25.3: Método de Heun com h=0.5 para o Problema 25.1 ---")
    # Gráfico do Problema 25.3
    methods_25_3 = {
        'Heun h=0.5': heun_nao_iterativo,
    }
    plot_results(f_25_1, x0, y0, x_final, 0.5, methods_25_3, y_exata=y_exata_25_1, title="Problema 25.3")
    
    # Problema 25.4: Use o método do ponto médio com h=0.5 e 0.25 para resolver o Problema 25.1.
    print("\n--- Problema 25.4: Método do Ponto Médio com h=0.5 e 0.25 para o Problema 25.1 ---")
    h_values_25_4 = [0.5, 0.25]
    
    # Gráfico do Problema 25.4
    methods_25_4 = {
        'Ponto Médio h=0.5': lambda f, x0, y0, h_val, x_final: ponto_medio(f, x0, y0, 0.5, x_final),
        'Ponto Médio h=0.25': lambda f, x0, y0, h_val, x_final: ponto_medio(f, x0, y0, 0.25, x_final)
    }
    plot_results(f_25_1, x0, y0, x_final, h_values_25_4[0], methods_25_4, y_exata=y_exata_25_1, title="Problema 25.4")
    
    # Problema 25.5: Use o método RK4 com h=0.5 para resolver o Problema 25.1.
    print("\n--- Problema 25.5: Método de RK4 com h=0.5 para o Problema 25.1 ---")
    # Gráfico do Problema 25.5
    methods_25_5 = {
        'RK4 h=0.5': rk4,
    }
    plot_results(f_25_1, x0, y0, x_final, 0.5, methods_25_5, y_exata=y_exata_25_1, title="Problema 25.5")

    # Problema 25.6: Repita os problemas 25.1 a 25.5, mas para a nova EDO.
    def f_25_6(x, y):
        return (1 + 2*x) * np.sqrt(y)
    def y_exata_25_6(x):
        return (x**2 + x + 1)**2

    x0, y0, x_final = 0, 1, 1.0
    h = 0.01

    print("\n--- Problema 25.6: Resolução dos problemas 25.1 a 25.5 para a nova EDO ---")
    
    # Gráfico comparativo geral para o Problema 25.6
    methods_25_6_plot = {
        'Euler': euler,
        'Heun': heun_nao_iterativo,
        'Ponto Médio': ponto_medio,
        'RK4': rk4,
    }
    plot_results(f_25_6, x0, y0, x_final, h, methods_25_6_plot, y_exata=y_exata_25_6, title="Problema 25.6")

# Funções de auxílio para plotagem
def plot_results_adaptive(x_vals, y_vals, y_exata, title):
    plt.figure(figsize=(12, 8))
    x_true = np.linspace(min(x_vals), max(x_vals), 500)
    y_true = y_exata(x_true)
    plt.plot(x_true, y_true, 'k--', label='Solução Exata')
    plt.plot(x_vals, y_vals, 'bo-', markersize=4, label='RKF45 (Adaptativo)')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

# Definição do problema do Exemplo 25.12 (verifique o livro)
def f_25_12(x, y):
    return 4 * np.exp(0.8 * x) - 0.5 * y

def y_exata_25_12(x):
    return (4 / 1.3) * (np.exp(0.8 * x) - np.exp(-0.5 * x)) + 2 * np.exp(-0.5 * x)

def desafio_3_9():
    print("\n--- 3.9) [DESAFIO OPCIONAL] Reproduzindo o EXEMPLO 25.14 ---")
    
    # Parâmetros da simulação
    x0 = 0.0
    y0 = 2.0
    h_inicial = 1.0
    x_final = 1.0
    tolerancia = 1e-5 # Tolerância padrão para o método adaptativo

    x_rkf, y_rkf = rk_fehlberg(f_25_12, x0, y0, h_inicial, x_final, tol=tolerancia)

    print(f"Resultados do Método RKF45 com tolerância = {tolerancia}:")
    for i in range(len(x_rkf)):
        erro_local = abs(y_rkf[i] - y_exata_25_12(x_rkf[i]))
        print(f"x = {x_rkf[i]:.6f}, y = {y_rkf[i]:.6f}, Erro Absoluto = {erro_local:.6e}")
    
    plot_results_adaptive(x_rkf, y_rkf, y_exata_25_12, "Exemplo 25.14: Método Adaptativo RKF45")

def desafio_3_10():
    print("\n--- 3.10) [DESAFIO OPCIONAL] Resolvendo o problema 25.27 ---")

    # Definir a função f(x) do problema 25.27
    def f_25_27(x, y):
        # Note que a função f(x) do problema 25.27 não depende de y
        # O argumento y é mantido para compatibilidade com a função do método
        term1 = 1 / ((x - 0.3)**2 + 0.01)
        term2 = 1 / ((x - 0.9)**2 + 0.04)
        return term1 + term2 - 6

    # Parâmetros da simulação
    x0 = 0.0
    y0 = 0.0 # Valor inicial da integral
    h_inicial = 0.1 # Passo inicial
    x_final = 1.0
    tolerancia = 1e-5

    # Rodar o método RKF45
    x_rkf, y_rkf = rk_fehlberg(f_25_27, x0, y0, h_inicial, x_final, tol=tolerancia)

    valor_integral = y_rkf[-1]

    print(f"O valor da integral de f(x) de 0 a 1 é: {valor_integral:.6f}")
    
    plot_results_adaptive(x_rkf, y_rkf, "Solução do Problema 25.27 (Método Adaptativo RKF45)")



if __name__ == "__main__":
    # Descomente a linha para executar cada parte da tarefa
    # problema_3_1_e_3_4()
    # problema_3_2()
    # problema_3_3()
    # problema_3_5()
    # problema_3_6()
    # problema_3_7()
    # problema_3_8()
    desafio_3_9()