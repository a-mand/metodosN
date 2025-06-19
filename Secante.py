def secant_method(f_expr, x0, x1, tol=1e-6, max_iter=100):
    """
    Implementa o método da secante para encontrar raízes.
    
    Parâmetros:
    f_expr (str): Expressão da função
    x0 (float): Primeiro ponto inicial
    x1 (float): Segundo ponto inicial
    tol (float): Tolerância para convergência
    max_iter (int): Número máximo de iterações
    
    Retorna:
    dict: Dicionário com a raiz, histórico de iterações e status
    """
    x = symbols('x')
    try:
        f = lambdify(x, sympify(f_expr), 'numpy')
    except:
        return {'error': 'Expressão inválida.'}
    
    history = []
    x_vals = [x0, x1]
    
    for i in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)
        
        if abs(fx1 - fx0) < 1e-10:
            return {
                'root': x1,
                'iterations': i+1,
                'history': history,
                'status': 'Diferença entre pontos muito pequena'
            }
        
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        history.append({
            'iteration': i+1,
            'x': x2,
            'f(x)': f(x2)
        })
        x_vals.append(x2)
        
        if abs(x2 - x1) < tol:
            plot_secant_convergence(f_expr, x_vals)
            return {
                'root': x2,
                'iterations': i+1,
                'history': history,
                'status': 'Convergido'
            }
        
        x0, x1 = x1, x2
    
    plot_secant_convergence(f_expr, x_vals)
    return {
        'root': x1,
        'iterations': max_iter,
        'history': history,
        'status': 'Máximo de iterações atingido'
    }

def plot_secant_convergence(f_expr, x_vals):
    """Plota a convergência do método da secante."""
    x = symbols('x')
    f = lambdify(x, sympify(f_expr), 'numpy')
    
    # Cria um intervalo para plotagem
    x_min, x_max = min(x_vals), max(x_vals)
    margin = 0.1 * (x_max - x_min)
    x_plot = np.linspace(x_min - margin, x_max + margin, 400)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_plot, f(x_plot), 'b-', label=f'f(x) = {f_expr}')
    plt.axhline(0, color='k', linestyle='--', linewidth=0.7)
    
    # Plota as secantes
    for i in range(len(x_vals)-2):
        x0, x1 = x_vals[i], x_vals[i+1]
        fx0, fx1 = f(x0), f(x1)
        
        secant = lambda x: fx0 + (fx1 - fx0)/(x1 - x0) * (x - x0)
        x_secant = np.linspace(min(x0, x1), max(x0, x1), 2)
        plt.plot(x_secant, secant(x_secant), 'r--', alpha=0.5)
        plt.plot([x1, x1], [0, fx1], 'g:', alpha=0.5)
    
    plt.scatter(x_vals, [f(x) for x in x_vals], color='red', zorder=5)
    plt.title('Convergência do Método da Secante')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()