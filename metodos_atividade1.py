import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify, lambdify, symbols, diff, sqrt
import math

def incremental_search(f_expr, a, b, N):
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
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, f_vals, 'b-', label='Função')
    plt.axhline(0, color='k', linestyle='--', linewidth=0.7)
    
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

def bisection_method(f_expr, a, b, tol=1e-6, max_iter=100):
    x = symbols('x')
    f = lambdify(x, sympify(f_expr), 'numpy')
    
    if f(a) * f(b) >= 0:
        return {'error': 'A função não muda de sinal no intervalo dado.'}
    
    history = []
    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        history.append({
            'iteração': i+1,
            'a': a,
            'b': b,
            'c': c,
            'f(c)': fc,
            'erro': abs(b - a)/2
        })
        
        if fc == 0 or (b - a)/2 < tol:
            return {
                'raiz': c,
                'iterações': i+1,
                'histórico': history,
                'status': 'Convergido'
            }
        
        if f(a) * fc < 0:
            b = c
        else:
            a = c
    
    return {
        'raiz': (a + b) / 2,
        'iterações': max_iter,
        'histórico': history,
        'status': 'Máximo de iterações atingido'
    }

def false_position_method(f_expr, a, b, tol=1e-6, max_iter=100):
    x = symbols('x')
    f = lambdify(x, sympify(f_expr), 'numpy')
    
    if f(a) * f(b) >= 0:
        return {'error': 'A função não muda de sinal no intervalo dado.'}
    
    history = []
    for i in range(max_iter):
        fa = f(a)
        fb = f(b)
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)
        history.append({
            'iteração': i+1,
            'a': a,
            'b': b,
            'c': c,
            'f(c)': fc,
            'erro': abs(fc)
        })
        
        if fc == 0 or abs(fc) < tol:
            return {
                'raiz': c,
                'iterações': i+1,
                'histórico': history,
                'status': 'Convergido'
            }
        
        if fa * fc < 0:
            b = c
        else:
            a = c
    
    return {
        'raiz': c,
        'iterações': max_iter,
        'histórico': history,
        'status': 'Máximo de iterações atingido'
    }

def modified_false_position(f_expr, a, b, tol=1e-6, max_iter=100):
    x = symbols('x')
    f = lambdify(x, sympify(f_expr), 'numpy')
    
    if f(a) * f(b) >= 0:
        return {'error': 'A função não muda de sinal no intervalo dado.'}
    
    history = []
    fa = f(a)
    fb = f(b)
    last_side = None
    
    for i in range(max_iter):
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)
        history.append({
            'iteração': i+1,
            'a': a,
            'b': b,
            'c': c,
            'f(c)': fc,
            'erro': abs(fc)
        })
        
        if fc == 0 or abs(fc) < tol:
            return {
                'raiz': c,
                'iterações': i+1,
                'histórico': history,
                'status': 'Convergido'
            }
        
        if fa * fc < 0:
            b = c
            fb = fc
            if last_side == 'left':
                fa /= 2
            last_side = 'left'
        else:
            a = c
            fa = fc
            if last_side == 'right':
                fb /= 2
            last_side = 'right'
    
    return {
        'raiz': c,
        'iterações': max_iter,
        'histórico': history,
        'status': 'Máximo de iterações atingido'
    }

def fixed_point_iteration(g_expr, x0, tol=1e-6, max_iter=100):
    x = symbols('x')
    try:
        g = lambdify(x, sympify(g_expr), 'numpy')
    except:
        return {'error': 'Expressão inválida.'}
    
    history = []
    for i in range(max_iter):
        x1 = g(x0)
        history.append({
            'iteração': i+1,
            'x': x1,
            'erro': abs(x1 - x0)
        })
        
        if abs(x1 - x0) < tol:
            return {
                'raiz': x1,
                'iterações': i+1,
                'histórico': history,
                'status': 'Convergido'
            }
        
        x0 = x1
    
    return {
        'raiz': x0,
        'iterações': max_iter,
        'histórico': history,
        'status': 'Máximo de iterações atingido'
    }

def newton_raphson(f_expr, x0, tol=1e-6, max_iter=100):
    x = symbols('x')
    try:
        f = lambdify(x, sympify(f_expr), 'numpy')
        df = lambdify(x, diff(sympify(f_expr), x), 'numpy')
    except:
        return {'error': 'Expressão inválida ou derivada não calculável.'}
    
    history = []
    for i in range(max_iter):
        fx = f(x0)
        dfx = df(x0)
        
        if abs(dfx) < 1e-10:
            return {'error': 'Derivada zero encontrada. Método falhou.'}
        
        x1 = x0 - fx / dfx
        history.append({
            'iteração': i+1,
            'x': x1,
            'f(x)': fx,
            'erro': abs(x1 - x0)
        })
        
        if abs(x1 - x0) < tol:
            return {
                'raiz': x1,
                'iterações': i+1,
                'histórico': history,
                'status': 'Convergido'
            }
        
        x0 = x1
    
    return {
        'raiz': x1,
        'iterações': max_iter,
        'histórico': history,
        'status': 'Máximo de iterações atingido'
    }

def secant_method(f_expr, x0, x1, tol=1e-6, max_iter=100):
    x = symbols('x')
    try:
        f = lambdify(x, sympify(f_expr), 'numpy')
    except:
        return {'error': 'Expressão inválida.'}
    
    history = []
    for i in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)
        
        if abs(fx1 - fx0) < 1e-10:
            return {'error': 'Diferença entre pontos muito pequena.'}
        
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        history.append({
            'iteração': i+1,
            'x': x2,
            'f(x)': f(x2),
            'erro': abs(x2 - x1)
        })
        
        if abs(x2 - x1) < tol:
            return {
                'raiz': x2,
                'iterações': i+1,
                'histórico': history,
                'status': 'Convergido'
            }
        
        x0, x1 = x1, x2
    
    return {
        'raiz': x1,
        'iterações': max_iter,
        'histórico': history,
        'status': 'Máximo de iterações atingido'
    }

def quadratic_formula(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    x1 = (-b + sqrt(discriminant)) / (2*a)
    x2 = (-b - sqrt(discriminant)) / (2*a)
    return x1, x2

def print_results(result):
    if 'error' in result:
        print("Erro:", result['error'])
        return
    
    print(f"\nRaiz encontrada: {result['raiz']:.8f}")
    print(f"Status: {result['status']}")
    print(f"Iterações: {result['iterações']}")
    
    if 'histórico' in result:
        print("\nHistórico de iterações:")
        headers = result['histórico'][0].keys()
        print("\t".join(headers))
        for row in result['histórico']:
            print("\t".join(f"{row[h]:.6f}" if isinstance(row[h], float) else str(row[h]) for h in headers))

def main_menu():
    while True:
        print("\n=== MÉTODOS NUMÉRICOS PARA ENCONTRAR RAÍZES ===")
        print("1. Métodos Intervalares")
        print("2. Métodos Abertos")
        print("3. Fórmula Quadrática")
        print("4. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            interval_methods_menu()
        elif choice == '2':
            open_methods_menu()
        elif choice == '3':
            a = float(input("Coeficiente a: "))
            b = float(input("Coeficiente b: "))
            c = float(input("Coeficiente c: "))
            roots = quadratic_formula(a, b, c)
            if roots:
                print(f"\nRaízes encontradas: {roots[0]:.8f} e {roots[1]:.8f}")
            else:
                print("Não há raízes reais para esses coeficientes.")
        elif choice == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

def interval_methods_menu():
    while True:
        print("\n=== MÉTODOS INTERVALARES ===")
        print("1. Busca Incremental")
        print("2. Método da Bisseção")
        print("3. Método da Falsa Posição")
        print("4. Método da Falsa Posição Modificado")
        print("5. Voltar")
        
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            f_expr = input("Digite a expressão da função (use 'x' como variável): ")
            a = float(input("Limite inferior do intervalo: "))
            b = float(input("Limite superior do intervalo: "))
            N = int(input("Número de subdivisões: "))
            intervals = incremental_search(f_expr, a, b, N)
            print("\nIntervalos com mudança de sinal:", intervals)
        elif choice in ['2', '3', '4']:
            f_expr = input("Digite a expressão da função (use 'x' como variável): ")
            a = float(input("Limite inferior do intervalo: "))
            b = float(input("Limite superior do intervalo: "))
            tol = float(input("Tolerância desejada (ex: 1e-6): "))
            
            if choice == '2':
                result = bisection_method(f_expr, a, b, tol)
            elif choice == '3':
                result = false_position_method(f_expr, a, b, tol)
            elif choice == '4':
                result = modified_false_position(f_expr, a, b, tol)
            
            print_results(result)
        elif choice == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

def open_methods_menu():
    while True:
        print("\n=== MÉTODOS ABERTOS ===")
        print("1. Método do Ponto Fixo")
        print("2. Método de Newton-Raphson")
        print("3. Método da Secante")
        print("4. Voltar")
        
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            g_expr = input("Digite a expressão da função de iteração g(x): ")
            x0 = float(input("Chute inicial: "))
            tol = float(input("Tolerância desejada (ex: 1e-6): "))
            result = fixed_point_iteration(g_expr, x0, tol)
            print_results(result)
        elif choice == '2':
            f_expr = input("Digite a expressão da função f(x): ")
            x0 = float(input("Chute inicial: "))
            tol = float(input("Tolerância desejada (ex: 1e-6): "))
            result = newton_raphson(f_expr, x0, tol)
            print_results(result)
        elif choice == '3':
            f_expr = input("Digite a expressão da função f(x): ")
            x0 = float(input("Primeiro ponto inicial: "))
            x1 = float(input("Segundo ponto inicial: "))
            tol = float(input("Tolerância desejada (ex: 1e-6): "))
            result = secant_method(f_expr, x0, x1, tol)
            print_results(result)
        elif choice == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main_menu()