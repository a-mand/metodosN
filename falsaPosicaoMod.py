def modified_false_position(f_expr, a, b, tol=1e-6, max_iter=100):
    """
    Implementa o método da falsa posição modificado para encontrar raízes de uma função.
    
    Parâmetros:
    f_expr (str): Expressão da função
    a (float): Limite inferior do intervalo
    b (float): Limite superior do intervalo
    tol (float): Tolerância para convergência
    max_iter (int): Número máximo de iterações
    
    Retorna:
    dict: Dicionário com a raiz, histórico de iterações e status
    """
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
            'iteration': i+1,
            'a': a,
            'b': b,
            'c': c,
            'f(c)': fc
        })
        
        if fc == 0 or abs(fc) < tol:
            return {
                'root': c,
                'iterations': i+1,
                'history': history,
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
        'root': c,
        'iterations': max_iter,
        'history': history,
        'status': 'Máximo de iterações atingido'
    }