import numpy as np
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
    def f(x, y):
        return y - x
    def y_exata(x):
        return np.exp(x) + x + 1

    x0, y0 = 0, 2.0
    x_final = 2.0
    h = 0.01
    
    methods = {
        'Euler': euler,
        'Heun': heun_nao_iterativo,
        'Nystrom': nystrom,
        'Ralston': ralston,
        'RK4': rk4
    }

    print("\n--- 3.5) Gerando gráfico comparativo para y' = y - x ---")
    plot_results(f, x0, y0, x_final, h, methods, y_exata=y_exata)

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
    plot_results(f_33_1, 0, 2.0, x_final, h, methods_1, y_exata=y_exata_33_1)
    
    print("\n--- 3.7) Gerando gráfico comparativo para y' = y com RK3 e RK4 ---")
    plot_results(f_33_2, 0, 1.0, x_final, h, methods_1, y_exata=y_exata_33_2)

## 3.8) Resolver os problemas 25.1 a 25.6 (exemplos)
def problema_3_8():
    print("\n--- 3.8) Resolvendo problemas 25.1 a 25.6 (exemplos) ---")
    
    # Problema 25.1: dy/dx = 4x^3, y(0)=0. Solução Exata: y = x^4
    def f_25_1(x, y):
        return 4 * x**3
    def y_exata_25_1(x):
        return x**4

    x0, y0, h, x_final = 0, 0, 0.1, 1.0
    print("\n--- Problema 25.1: y' = 4x^3, y(0)=0 ---")
    print("--- Método de RK4 ---")
    x_rk4, y_rk4 = rk4(f_25_1, x0, y0, h, x_final)
    print_table(x_rk4, y_rk4, y_exata_25_1, h, "RK4")
    plot_results(f_25_1, x0, y0, x_final, h, {'RK4': rk4}, y_exata=y_exata_25_1, title="Problema 25.1 com RK4")
    
    # Problema 25.2: dy/dx = 5x^4, y(0)=0. Solução Exata: y = x^5
    def f_25_2(x, y):
        return 5 * x**4
    def y_exata_25_2(x):
        return x**5
    
    x0, y0, h, x_final = 0, 0, 0.1, 1.0
    print("\n--- Problema 25.2: y' = 5x^4, y(0)=0 ---")
    print("--- Método de RK4 ---")
    x_rk4, y_rk4 = rk4(f_25_2, x0, y0, h, x_final)
    print_table(x_rk4, y_rk4, y_exata_25_2, h, "RK4")
    plot_results(f_25_2, x0, y0, x_final, h, {'RK4': rk4}, y_exata=y_exata_25_2, title="Problema 25.2 com RK4")

    # Problema 25.3: y' = -y, y(0)=1. Solução Exata: y = e^-x
    def f_25_3(x, y):
        return -y
    def y_exata_25_3(x):
        return np.exp(-x)

    x0, y0, h, x_final = 0, 1, 0.1, 1.0
    print("\n--- Problema 25.3: y' = -y, y(0)=1 ---")
    print("--- Métodos de RK4, Euler e Heun ---")
    methods_25_3 = {
        'RK4': rk4,
        'Euler': euler,
        'Heun': heun_nao_iterativo,
    }
    plot_results(f_25_3, x0, y0, x_final, h, methods_25_3, y_exata=y_exata_25_3, title="Problema 25.3 com RK4, Euler e Heun")
    
    # Problema 25.4: y' = -y + x + 2, y(0)=2. Solução Exata: y = e^-x + x + 1
    def f_25_4(x, y):
        return -y + x + 2
    def y_exata_25_4(x):
        return np.exp(-x) + x + 1

    x0, y0, h, x_final = 0, 2, 0.1, 1.0
    print("\n--- Problema 25.4: y' = -y + x + 2, y(0)=2 ---")
    print("--- Métodos de RK4, Euler e Heun ---")
    methods_25_4 = {
        'RK4': rk4,
        'Euler': euler,
        'Heun': heun_nao_iterativo,
    }
    plot_results(f_25_4, x0, y0, x_final, h, methods_25_4, y_exata=y_exata_25_4, title="Problema 25.4 com RK4, Euler e Heun")

    # Problema 25.5: dy/dx = 2x, y(1)=1. Solução Exata: y = x^2
    def f_25_5(x, y):
        return 2 * x
    def y_exata_25_5(x):
        return x**2
    
    x0, y0, h, x_final = 1, 1, 0.1, 2.0
    print("\n--- Problema 25.5: y' = 2x, y(1)=1 ---")
    print("--- Métodos de RK4, Euler e Heun ---")
    methods_25_5 = {
        'RK4': rk4,
        'Euler': euler,
        'Heun': heun_nao_iterativo,
    }
    plot_results(f_25_5, x0, y0, x_final, h, methods_25_5, y_exata=y_exata_25_5, title="Problema 25.5 com RK4, Euler e Heun")

    # Problema 25.6: dy/dx = y^2+1, y(0)=0. Solução Exata: y = tan(x)
    def f_25_6(x, y):
        return y**2 + 1
    def y_exata_25_6(x):
        return np.tan(x)
    
    x0, y0, h, x_final = 0, 0, 0.1, 1.0
    print("\n--- Problema 25.6: y' = y^2+1, y(0)=0 ---")
    print("--- Métodos de RK4, Euler e Heun ---")
    methods_25_6 = {
        'RK4': rk4,
        'Euler': euler,
        'Heun': heun_nao_iterativo,
    }
    plot_results(f_25_6, x0, y0, x_final, h, methods_25_6, y_exata=y_exata_25_6, title="Problema 25.6 com RK4, Euler e Heun")


if __name__ == "__main__":
    # Descomente a linha para executar cada parte da tarefa
    # problema_3_1_e_3_4()
    # problema_3_2()
    # problema_3_3()
    # problema_3_5()
    # problema_3_6()
    # problema_3_7()
    problema_3_8()