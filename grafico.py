def compare_methods(f_expr, a, b, tol=1e-6, max_iter=50):
    """
    Compara graficamente os métodos da bisseção e falsa posição.
    
    Parâmetros:
    f_expr (str): Expressão da função
    a (float): Limite inferior do intervalo
    b (float): Limite superior do intervalo
    tol (float): Tolerância para convergência
    max_iter (int): Número máximo de iterações
    """
    # Executa os métodos
    bisection = bisection_method(f_expr, a, b, tol, max_iter)
    false_pos = false_position_method(f_expr, a, b, tol, max_iter)
    
    # Prepara dados para plotagem
    bisection_errors = [abs(item['f(c)']) for item in bisection['history']]
    false_pos_errors = [abs(item['f(c)']) for item in false_pos['history']]
    
    plt.figure(figsize=(10, 6))
    plt.semilogy(bisection_errors, 'bo-', label='Bisseção')
    plt.semilogy(false_pos_errors, 'r^-', label='Falsa Posição')
    plt.xlabel('Iteração')
    plt.ylabel('Erro |f(c)|')
    plt.title('Comparação da Convergência dos Métodos')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.show()
    
    # Imprime resumo
    print(f"Bisseção convergiu em {bisection['iterations']} iterações")
    print(f"Falsa Posição convergiu em {false_pos['iterations']} iterações")