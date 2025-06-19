import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify, lambdify, symbols, diff

def incremental_search(f_expr, a, b, N):
    """
    Realiza uma busca incremental por raízes no intervalo [a,b] dividido em N subintervalos.
    
    Parâmetros:
    f_expr (str): Expressão da função a ser analisada
    a (float): Limite inferior do intervalo
    b (float): Limite superior do intervalo
    N (int): Número de subdivisões
    
    Retorna:
    list: Lista de subintervalos onde ocorre mudança de sinal
    """
    x = symbols('x')
    try:
        f = lambdify(x, sympify(f_expr), 'numpy')
    except:
        print("Expressão inválida. Por favor, insira uma expressão matemática válida.")
        return []
    
    x_vals = np.linspace(a, b, N+1)
    f_vals = f(x_vals)
    
    sign_changes = []
    for i in range(len(x_vals)-1):
        if f_vals[i] == 0:
            sign_changes.append((x_vals[i], x_vals[i]))
        elif f_vals[i] * f_vals[i+1] < 0:
            sign_changes.append((x_vals[i], x_vals[i+1]))
    
    # Plotagem
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, f_vals, 'b-', label='Função')
    plt.axhline(0, color='k', linestyle='--', linewidth=0.7)
    
    # Destacar intervalos com mudança de sinal
    for interval in sign_changes:
        x1, x2 = interval
        mask = (x_vals >= x1) & (x_vals <= x2)
        plt.plot(x_vals[mask], f_vals[mask], 'r-', linewidth=2)
        plt.axvline(x1, color='g', linestyle=':', alpha=0.5)
        plt.axvline(x2, color='g', linestyle=':', alpha=0.5)
    
    plt.title(f'Busca Incremental com {N} Subdivisões')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    return sign_changes