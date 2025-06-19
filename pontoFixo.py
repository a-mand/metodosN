def fixed_point_iteration(g_expr, x0, tol=1e-6, max_iter=100):
    """
    Implementa o método da iteração de ponto fixo.
    
    Parâmetros:
    g_expr (str): Expressão da função de iteração g(x)
    x0 (float): Chute inicial
    tol (float): Tolerância para convergência
    max_iter (int): Número máximo de iterações
    
    Retorna:
    dict: Dicionário com a raiz, histórico de iterações e status
    """
    x = symbols('x')
    try:
        g = lambdify(x, sympify(g_expr), 'numpy')
    except:
        return {'error': 'Expressão inválida.'}
    
    history = []
    x_vals = []
    
    for i in range(max_iter):
        x1 = g(x0)
        history.append({
            'iteration': i+1,
            'x': x1,
            'g(x)': x1
        })
        x_vals.append(x0)
        
        if abs(x1 - x0) < tol:
            x_vals.append(x1)
            plot_fixed_point_convergence(g_expr, x_vals)
            return {
                'root': x1,
                'iterations': i+1,
                'history': history,
                'status': 'Convergido'
            }
        
        x0 = x1
    
    x_vals.append(g(x0))
    plot_fixed_point_convergence(g_expr, x_vals)
    
    return {
        'root': x0,
        'iterations': max_iter,
        'history': history,
        'status': 'Máximo de iterações atingido'
    }

def plot_fixed_point_convergence(g_expr, x_vals):
    """Plota a convergência do método do ponto fixo."""
    x = symbols('x')
    g = lambdify(x, sympify(g_expr), 'numpy')
    
    # Cria um intervalo para plotagem
    x_min, x_max = min(x_vals), max(x_vals)
    margin = 0.1 * (x_max - x_min)
    x_plot = np.linspace(x_min - margin, x_max + margin, 400)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_plot, x_plot, 'k-', label='y = x')
    plt.plot(x_plot, g(x_plot), 'b-', label=f'y = g(x) = {g_expr}')
    
    # Desenha as linhas de iteração
    for i in range(len(x_vals)-1):
        plt.plot([x_vals[i], x_vals[i]], [x_vals[i], x_vals[i+1]], 'r--')
        if i < len(x_vals)-2:
            plt.plot([x_vals[i], x_vals[i+1]], [x_vals[i+1], x_vals[i+1]], 'r--')
    
    plt.scatter(x_vals, [g(x) for x in x_vals], color='red', zorder=5)
    plt.title('Convergência do Método do Ponto Fixo')
    plt.xlabel('x')
    plt.ylabel('g(x)')
    plt.legend()
    plt.grid(True)
    plt.show()