import numpy as np

def euler(f, x0, y0, h, x_final):
    """
    Implementação do Método de Euler para EDOs.

    Args:
        f (function): A função f(x, y) da EDO dy/dx = f(x, y).
        x0 (float): A condição inicial para x.
        y0 (float): A condição inicial para y.
        h (float): O tamanho do passo.
        x_final (float): O valor final de x para a simulação.

    Returns:
        tuple: Arrays numpy dos valores de x e y calculados.
    """
    x_values = [x0]
    y_values = [y0]
    n_steps = int((x_final - x0) / h)

    for _ in range(n_steps):
        x = x_values[-1]
        y = y_values[-1]
        y_novo = y + h * f(x, y)
        x_novo = x + h
        x_values.append(x_novo)
        y_values.append(y_novo)

    return np.array(x_values), np.array(y_values)

def heun_nao_iterativo(f, x0, y0, h, x_final):
    """
    Implementação do Método de Heun (não iterativo).

    Args:
        f (function): A função f(x, y) da EDO dy/dx = f(x, y).
        x0 (float): A condição inicial para x.
        y0 (float): A condição inicial para y.
        h (float): O tamanho do passo.
        x_final (float): O valor final de x para a simulação.

    Returns:
        tuple: Arrays numpy dos valores de x e y calculados.
    """
    x_values = [x0]
    y_values = [y0]
    n_steps = int((x_final - x0) / h)

    for _ in range(n_steps):
        x = x_values[-1]
        y = y_values[-1]
        
        # Preditor: Estimativa inicial para o próximo ponto
        y_preditor = y + h * f(x, y)
        
        # Corretor: Corrige a estimativa usando a média das inclinações
        y_novo = y + 0.5 * h * (f(x, y) + f(x + h, y_preditor))
        
        x_values.append(x + h)
        y_values.append(y_novo)
        
    return np.array(x_values), np.array(y_values)

def heun_iterativo(f, x0, y0, h, x_final, max_iter=100, tol=1e-8):
    """
    Implementação do Método de Heun (iterativo).

    Args:
        f (function): A função f(x, y) da EDO dy/dx = f(x, y).
        x0 (float): A condição inicial para x.
        y0 (float): A condição inicial para y.
        h (float): O tamanho do passo.
        x_final (float): O valor final de x para a simulação.
        max_iter (int): Número máximo de iterações do corretor.
        tol (float): Tolerância para a convergência.

    Returns:
        tuple: Arrays numpy dos valores de x e y calculados.
    """
    x_values = [x0]
    y_values = [y0]
    n_steps = int((x_final - x0) / h)
    
    for _ in range(n_steps):
        x = x_values[-1]
        y = y_values[-1]
        
        # Preditor inicial
        y_pred = y + h * f(x, y)
        y_novo = y_pred
        
        # Corretor Iterativo
        for _ in range(max_iter):
            y_anterior = y_novo
            y_novo = y + 0.5 * h * (f(x, y) + f(x + h, y_anterior))
            if abs(y_novo - y_anterior) < tol:
                break
        
        x_values.append(x + h)
        y_values.append(y_novo)
        
    return np.array(x_values), np.array(y_values)

def ponto_medio(f, x0, y0, h, x_final):
    """
    Implementação do Método do Ponto Médio.

    Args:
        f (function): A função f(x, y) da EDO dy/dx = f(x, y).
        x0 (float): A condição inicial para x.
        y0 (float): A condição inicial para y.
        h (float): O tamanho do passo.
        x_final (float): O valor final de x para a simulação.

    Returns:
        tuple: Arrays numpy dos valores de x e y calculados.
    """
    x_values = [x0]
    y_values = [y0]
    n_steps = int((x_final - x0) / h)
    
    for _ in range(n_steps):
        x = x_values[-1]
        y = y_values[-1]
        
        y_mid = y + 0.5 * h * f(x, y)
        y_novo = y + h * f(x + 0.5 * h, y_mid)
        
        x_values.append(x + h)
        y_values.append(y_novo)
    
    return np.array(x_values), np.array(y_values)

def nystrom(f, x0, y0, h, x_final):
    """
    Implementação do Método de Nystrom. Requer um ponto de partida adicional,
    que é calculado usando o método de Heun.

    Args:
        f (function): A função f(x, y) da EDO dy/dx = f(x, y).
        x0 (float): A condição inicial para x.
        y0 (float): A condição inicial para y.
        h (float): O tamanho do passo.
        x_final (float): O valor final de x para a simulação.

    Returns:
        tuple: Arrays numpy dos valores de x e y calculados.
    """
    # Usar Heun para o 1º ponto (y1), conforme instruído pelo material suplementar.
    _, y1_heun = heun_nao_iterativo(f, x0, y0, h, x0 + h)
    
    x_values = [x0, x0 + h]
    y_values = [y0, y1_heun[-1]]
    
    n_steps = int((x_final - x0) / h) - 1
    
    for i in range(n_steps):
        x_i = x_values[-1]
        y_i_minus_1 = y_values[-2]
        y_i = y_values[-1]
        
        y_novo = y_i_minus_1 + 2 * h * f(x_i, y_i)
        
        x_values.append(x_i + h)
        y_values.append(y_novo)
        
    return np.array(x_values), np.array(y_values)

def ralston(f, x0, y0, h, x_final):
    """
    Implementação do Método de Ralston (Runge-Kutta de 2ª ordem).

    Args:
        f (function): A função f(x, y) da EDO dy/dx = f(x, y).
        x0 (float): A condição inicial para x.
        y0 (float): A condição inicial para y.
        h (float): O tamanho do passo.
        x_final (float): O valor final de x para a simulação.

    Returns:
        tuple: Arrays numpy dos valores de x e y calculados.
    """
    x_values = [x0]
    y_values = [y0]
    n_steps = int((x_final - x0) / h)

    for _ in range(n_steps):
        x = x_values[-1]
        y = y_values[-1]
        
        k1 = f(x, y)
        k2 = f(x + 3/4 * h, y + 3/4 * h * k1)
        
        y_novo = y + h * (1/3 * k1 + 2/3 * k2)
        
        x_values.append(x + h)
        y_values.append(y_novo)

    return np.array(x_values), np.array(y_values)

def rk3(f, x0, y0, h, x_final):
    """
    Implementação do Método de Runge-Kutta Clássico de 3ª Ordem.

    Args:
        f (function): A função f(x, y) da EDO dy/dx = f(x, y).
        x0 (float): A condição inicial para x.
        y0 (float): A condição inicial para y.
        h (float): O tamanho do passo.
        x_final (float): O valor final de x para a simulação.

    Returns:
        tuple: Arrays numpy dos valores de x e y calculados.
    """
    x_values = [x0]
    y_values = [y0]
    n_steps = int((x_final - x0) / h)
    
    for _ in range(n_steps):
        x = x_values[-1]
        y = y_values[-1]
        
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x + h, y - k1 + 2 * k2)
        
        y_novo = y + (1/6) * (k1 + 4*k2 + k3)
        
        x_values.append(x + h)
        y_values.append(y_novo)
        
    return np.array(x_values), np.array(y_values)

def rk4(f, x0, y0, h, x_final):
    """
    Implementação do Método de Runge-Kutta Clássico de 4ª Ordem.

    Args:
        f (function): A função f(x, y) da EDO dy/dx = f(x, y).
        x0 (float): A condição inicial para x.
        y0 (float): A condição inicial para y.
        h (float): O tamanho do passo.
        x_final (float): O valor final de x para a simulação.

    Returns:
        tuple: Arrays numpy dos valores de x e y calculados.
    """
    x_values = [x0]
    y_values = [y0]
    n_steps = int((x_final - x0) / h)
    
    for _ in range(n_steps):
        x = x_values[-1]
        y = y_values[-1]
        
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(x + h, y + k3)
        
        y_novo = y + (1/6) * (k1 + 2*k2 + 2*k3 + k4)
        
        x_values.append(x + h)
        y_values.append(y_novo)
        
    return np.array(x_values), np.array(y_values)


def rk_fehlberg(f, x0, y0, h, x_final, tol=1e-5):
    """
    Implementação do Método Adaptativo de Runge-Kutta Fehlberg (RKF45).
    Este método usa duas estimativas, de 4ª e 5ª ordem, para controlar o passo h.
    
    Args:
        f (function): A função f(x, y) da EDO dy/dx = f(x, y).
        x0 (float): A condição inicial para x.
        y0 (float): A condição inicial para y.
        h (float): O tamanho inicial do passo.
        x_final (float): O valor final de x para a simulação.
        tol (float): Tolerância para o erro local.

    Returns:
        tuple: Arrays numpy dos valores de x e y calculados.
    """
    x_values = [x0]
    y_values = [y0]
    x = x0
    y = y0
    
    while x < x_final:
        # Aumenta h para não ultrapassar x_final
        if x + h > x_final:
            h = x_final - x
        
        # Coeficientes para o método RKF45
        k1 = h * f(x, y)
        k2 = h * f(x + 0.25 * h, y + 0.25 * k1)
        k3 = h * f(x + 3/8 * h, y + 3/32 * k1 + 9/32 * k2)
        k4 = h * f(x + 12/13 * h, y + 1932/2197 * k1 - 7200/2197 * k2 + 7296/2197 * k3)
        k5 = h * f(x + h, y + 439/216 * k1 - 8 * k2 + 3680/513 * k3 - 845/4104 * k4)
        k6 = h * f(x + 0.5 * h, y - 8/27 * k1 + 2 * k2 - 3544/2565 * k3 + 1859/4104 * k4 - 11/40 * k5)

        # Estimativas de 4ª e 5ª ordem
        y4_est = y + 25/216 * k1 + 1408/2565 * k3 + 2197/4104 * k4 - 0.2 * k5
        y5_est = y + 16/135 * k1 + 6656/12825 * k3 + 28561/56430 * k4 - 9/50 * k5 + 2/55 * k6

        # Estimar o erro
        erro = abs(y5_est - y4_est)

        # Controlar o tamanho do passo
        if erro <= tol:
            x += h
            y = y5_est
            x_values.append(x)
            y_values.append(y)
            # Aumentar o passo se o erro for muito pequeno
            h_novo = h * min(2, (tol / erro)**0.25)
            h = h_novo
        else:
            # Reduzir o passo se o erro for muito grande
            h_novo = h * max(0.1, (tol / (2 * erro))**0.25)
            h = h_novo

    return np.array(x_values), np.array(y_values)