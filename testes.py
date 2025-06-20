import unittest
from metodos_atividade1 import bisection_method, newton_raphson, quadratic_formula


class TestMetodosNumericos(unittest.TestCase):

    def test_bissecao_sucesso(self):
        """Testa o método da Bisseção com um caso de sucesso conhecido."""
        f_expr = "x**3 - x - 2"
        resultado = bisection_method(f_expr, a=1, b=2, tol=1e-7)

        # self.assertAlmostEqual é ideal para comparar números de ponto flutuante (floats)
        self.assertAlmostEqual(resultado['raiz'], 1.5213797, places=6)
        self.assertEqual(resultado['status'], 'Convergido')

    def test_newton_raphson_sucesso(self):
        """Testa o método de Newton-Raphson com um caso clássico."""
        f_expr = "exp(-x) - x"
        resultado = newton_raphson(f_expr, x0=0, tol=1e-7)

        self.assertAlmostEqual(resultado['raiz'], 0.5671432, places=6)
        self.assertLess(resultado['iterações'], 10)  # Newton deve ser rápido

    def test_formula_quadratica_raizes_reais(self):
        """Testa a fórmula quadrática para um caso com duas raízes reais."""
        # Para x^2 - 3x + 2 = 0, as raízes são 1 e 2.
        raizes = quadratic_formula(a=1, b=-3, c=2)

        # Verifica se a tupla de raízes é a esperada.
        # A função sympy.sqrt pode retornar a ordem (2.0, 1.0)
        self.assertAlmostEqual(raizes[0], 2.0)
        self.assertAlmostEqual(raizes[1], 1.0)

    def test_formula_quadratica_sem_raiz_real(self):
        """Testa a fórmula quadrática para um caso sem raízes reais."""
        # Para x^2 + x + 1 = 0, o discriminante é negativo.
        raizes = quadratic_formula(a=1, b=1, c=1)
        self.assertIsNone(raizes)

    def test_bissecao_falha_sem_mudanca_de_sinal(self):
        """Testa o comportamento de erro da Bisseção quando não há mudança de sinal."""
        f_expr = "x**2 + 2"  # Sempre positivo
        resultado = bisection_method(f_expr, a=1, b=2)

        # self.assertIn verifica se uma chave ('error') existe no dicionário de resultado
        self.assertIn('error', resultado)
        self.assertEqual(resultado['error'], 'A função não muda de sinal no intervalo dado.')


# Esta parte permite executar os testes diretamente do arquivo
if __name__ == '__main__':
    unittest.main()