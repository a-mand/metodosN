def main_menu():
    """Menu principal para interação com o usuário."""
    print("\n=== MÉTODOS NUMÉRICOS PARA ENCONTRAR RAÍZES ===")
    print("1. Métodos Intervalares")
    print("2. Métodos Abertos")
    print("3. Sair")
    
    choice = input("Escolha uma opção: ")
    
    if choice == '1':
        interval_methods_menu()
    elif choice == '2':
        open_methods_menu()
    elif choice == '3':
        return
    else:
        print("Opção inválida. Tente novamente.")
        main_menu()

def interval_methods_menu():
    """Menu para métodos intervalares."""
    print("\n=== MÉTODOS INTERVALARES ===")
    print("1. Busca Incremental")
    print("2. Método da Bisseção")
    print("3. Método da Falsa Posição")
    print("4. Método da Falsa Posição Modificado")
    print("5. Comparar Métodos")
    print("6. Voltar")
    
    choice = input("Escolha uma opção: ")
    
    if choice == '1':
        f_expr = input("Digite a expressão da função (use 'x' como variável): ")
        a = float(input("Limite inferior do intervalo: "))
        b = float(input("Limite superior do intervalo: "))
        N = int(input("Número de subdivisões: "))
        intervals = incremental_search(f_expr, a, b, N)
        print("\nIntervalos com mudança de sinal:", intervals)
        
        refine = input("Deseja refinar com um N diferente? (s/n): ")
        if refine.lower() == 's':
            N = int(input("Novo número de subdivisões: "))
            intervals = incremental_search(f_expr, a, b, N)
            print("\nIntervalos com mudança de sinal:", intervals)
        
        if intervals:
            proceed = input("Deseja calcular as raízes nos intervalos encontrados? (s/n): ")
            if proceed.lower() == 's':
                for i, interval in enumerate(intervals):
                    a, b = interval
                    print(f"\nCalculando raiz no intervalo {i+1}: [{a}, {b}]")
                    tol = float(input("Tolerância desejada: "))
                    
                    print("\nMétodo da Bisseção:")
                    result = bisection_method(f_expr, a, b, tol)
                    print_iteration_history(result)
                    
                    print("\nMétodo da Falsa Posição:")
                    result = false_position_method(f_expr, a, b, tol)
                    print_iteration_history(result)
                    
                    print("\nMétodo da Falsa Posição Modificado:")
                    result = modified_false_position(f_expr, a, b, tol)
                    print_iteration_history(result)
    
    elif choice == '2':
        f_expr = input("Digite a expressão da função (use 'x' como variável): ")
        a = float(input("Limite inferior do intervalo: "))
        b = float(input("Limite superior do intervalo: "))
        tol = float(input("Tolerância desejada: "))
        result = bisection_method(f_expr, a, b, tol)
        print_iteration_history(result)
    
    elif choice == '3':
        f_expr = input("Digite a expressão da função (use 'x' como variável): ")
        a = float(input("Limite inferior do intervalo: "))
        b = float(input("Limite superior do intervalo: "))
        tol = float(input("Tolerância desejada: "))
        result = false_position_method(f_expr, a, b, tol)
        print_iteration_history(result)
    
    elif choice == '4':
        f_expr = input("Digite a expressão da função (use 'x' como variável): ")
        a = float(input("Limite inferior do intervalo: "))
        b = float(input("Limite superior do intervalo: "))
        tol = float(input("Tolerância desejada: "))
        result = modified_false_position(f_expr, a, b, tol)
        print_iteration_history(result)
    
    elif choice == '5':
        f_expr = input("Digite a expressão da função (use 'x' como variável): ")
        a = float(input("Limite inferior do intervalo: "))
        b = float(input("Limite superior do intervalo: "))
        tol = float(input("Tolerância desejada: "))
        compare_methods(f_expr, a, b, tol)
    
    elif choice == '6':
        main_menu()
    else:
        print("Opção inválida. Tente novamente.")
        interval_methods_menu()

def open_methods_menu():
    """Menu para métodos abertos."""
    print("\n=== MÉTODOS ABERTOS ===")
    print("1. Método do Ponto Fixo")
    print("2. Método de Newton-Raphson")
    print("3. Método da Secante")
    print("4. Voltar")
    
    choice = input("Escolha uma opção: ")
    
    if choice == '1':
        g_expr = input("Digite a expressão da função de iteração g(x): ")
        x0 = float(input("Chute inicial: "))
        tol = float(input("Tolerância desejada: "))
        result = fixed_point_iteration(g_expr, x0, tol)
        print_iteration_history(result)
    
    elif choice == '2':
        f_expr = input("Digite a expressão da função f(x): ")
        x0 = float(input("Chute inicial: "))
        tol = float(input("Tolerância desejada: "))
        result = newton_raphson(f_expr, x0, tol)
        print_iteration_history(result)
    
    elif choice == '3':
        f_expr = input("Digite a expressão da função f(x): ")
        x0 = float(input("Primeiro ponto inicial: "))
        x1 = float(input("Segundo ponto inicial: "))
        tol = float(input("Tolerância desejada: "))
        result = secant_method(f_expr, x0, x1, tol)
        print_iteration_history(result)
    
    elif choice == '4':
        main_menu()
    else:
        print("Opção inválida. Tente novamente.")
        open_methods_menu()

def print_iteration_history(result):
    """Imprime o histórico de iterações de um método."""
    if 'error' in result:
        print("Erro:", result['error'])
        return
    
    print("\nRESULTADO:")
    print(f"Raiz aproximada: {result.get('root', 'N/A')}")
    print(f"Status: {result.get('status', 'N/A')}")
    print(f"Iterações: {result.get('iterations', 'N/A')}")
    
    if 'history' in result:
        print("\nHISTÓRICO DE ITERAÇÕES:")
        headers = result['history'][0].keys()
        print("\t".join(headers))
        for row in result['history']:
            print("\t".join(f"{row[h]:.6f}" if isinstance(row[h], float) else str(row[h]) for h in headers))

# Inicia o programa
if __name__ == "__main__":
    main_menu()