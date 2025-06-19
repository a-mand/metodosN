def newton_raphson(f_expr, x0, tol=1e-6, max_iter=100):
    """
    Implementa o método de Newton-Raphson para encontrar raízes.
    
    Parâmetros:
    f_expr (str): Expressão da função
    x0 (float): Chute inicial
    tol (float): Tolerância para convergência
    max_iter (int): Número máximo de iterações
    
    Retorna:
    dict: Dicionário com a raiz, histórico de iterações e status
    """
    x = symbols('x')
    try:
        f = lambdify(x, sympify(f_expr), 'numpy')
        df = lambdify(x, diff(sympify(f_expr), x), 'numpy')
    except:
        return {'error': 'Expressão inválida.'}
    
    history = []
    x_vals = [x0]
    
    for i in range(max_iter):
        fx = f(x0)
        dfx = df(x0)
        
        if abs(dfx) < 1e-10:
            return {
                'root': x0,
                'iterations': i+1,
                'history': history,
                'status': 'Derivada zero encontrada'
            }
        
        x1 = x0 - fx / dfx
        history.append({
            'iteration': i+1,
            'x': x1,
            'f(x)': fx,
            'f\'(x)': dfx
        })
        x_vals.append(x1)
        
        if abs(x1 - x0) < tol:
            plot_newton_convergence(f_expr, x_vals)
            return {
                'root': x1,
                'iterations': i+1,
                'history': history,
                'status': 'Convergido'
            }
        
        x0 = x1
    
    plot_newton_convergence(f_expr, x_vals)
    return {
        'root': x0,
        'iterations': max_iter,
        'history': history,
        'status': 'Máximo de iterações atingido'
    }

def plot_newton_convergence(f_expr, x_vals):
    """Plota a convergência do método de Newton-Raphson."""
    x = symbols('x')
    f = lambdify(x, sympify(f_expr), 'numpy')
    
    # Cria um intervalo para plotagem
    x_min, x_max = min(x_vals), max(x_vals)
    margin = 0.1 * (x_max - x_min)
    x_plot = np.linspace(x_min - margin, x_max + margin, 400)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_plot, f(x_plot), 'b-', label=f'f(x) = {f_expr}')
    plt.axhline(0, color='k', linestyle='--', linewidth=0.7)
    
    # Plota as tangentes
    for i in range(len(x_vals)-1):
        xi = x_vals[i]
        fxi = f(xi)
        df = diff(sympify(f_expr), x)
        dfxi = lambdify(x, df, 'numpy')(xi)
        
        tangent = lambda x: fxi + dfxi * (x - xi)
        x_tangent = np.linspace(xi - 0.5, xi + 0.5, 2)
        plt.plot(x_tangent, tangent(x_tangent), 'r--', alpha=0.5)
        plt.plot([xi, xi], [0, fxi], 'g:', alpha=0.5)
    
    plt.scatter(x_vals, [f(x) for x in x_vals], color='red', zorder=5)
    plt.title('Convergência do Método de Newton-Raphson')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()