# Métodos Numéricos para Encontrar Raízes de Funções

Este repositório contém a implementação em Python de diversos métodos numéricos para a determinação de raízes de funções (valores de $x$ para os quais $f(x) = 0$). O projeto foi desenvolvido como parte da disciplina de Métodos Numéricos, utilizando o Visual Studio Code (VS Code) e bibliotecas como `NumPy`, `Matplotlib` e `SymPy`.

## Visão Geral do Projeto

O objetivo principal é fornecer uma ferramenta interativa para explorar e aplicar métodos numéricos na resolução de equações não lineares. O programa é modular, com cada método implementado em funções dedicadas, permitindo fácil integração e reuso.

### Métodos Implementados:

**Métodos Intervalares:**
* **Busca Incremental (Varredura de Raízes):** Para pré-localizar intervalos onde há mudança de sinal da função.
* **Método da Bisseção:** Garante convergência, dividindo o intervalo ao meio.
* **Método da Falsa Posição (Regula Falsi):** Utiliza uma reta secante para estimar a raiz, geralmente mais rápido que a Bisseção.
* **Método da Falsa Posição Modificado:** Versão aprimorada da Falsa Posição para evitar convergência lenta em certos cenários.

**Métodos Abertos:**
* **Método da Iteração de Ponto Fixo Simples:** Baseado na reescrita da função para $x = g(x)$.
* **Método de Newton-Raphson:** Utiliza a derivada da função para convergência rápida (derivada calculada automaticamente).
* **Método da Secante:** Alternativa a Newton-Raphson que não requer a derivada.
* **Método da Secante Modificado:** Variante da Secante com perturbação relativa.

**Outros:**
* **Fórmula Quadrática:** Para validação de raízes de funções de segundo grau.

## Como Usar

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/a-mand/metodosN.git](https://github.com/a-mand/metodosN.git)
    cd metodosN
    ```
2.  **Instale as dependências:**
    ```bash
    pip install numpy matplotlib sympy
    ```
3.  **Execute o programa principal:**
    ```bash
    python metodos_atividade1.py
    ```
    O programa apresentará um menu interativo para escolher o método e inserir os parâmetros.

## Testes Automatizados

Para garantir a corretude e a confiabilidade dos algoritmos, o projeto inclui uma suíte de testes automatizados. Utilizando o framework `unittest` do Python, os testes validam a lógica de cada método numérico de forma isolada, verificando casos de sucesso conhecidos e o tratamento de erros esperados.

### Executando os Testes

Para rodar a suíte de testes e verificar a integridade do código, execute o seguinte comando no terminal, a partir da pasta raiz do projeto:

```bash
python -m unittest -v testes.py
```

## Questões Resolvidas do Livro "Métodos Numéricos para Engenharia" (Steven C. Chapra e Raymond P. Canale)

Este projeto foi testado e validado resolvendo problemas específicos do livro-texto, demonstrando a aplicação prática de cada método.

### Capítulo 5 - Métodos Intervalares (Página 114)

* **Questão 5.1:** Análise de uma função quadrática.
    * **Letra A (Busca Incremental):** Utilizada para localizar visualmente as regiões de raiz da função $f(x) = 0.5x^2 - 2.5x - 4.5$ no intervalo $[-3, 10]$ com 20 subdivisões.
    * **Letra B (Fórmula Quadrática):** Validação analítica das raízes da mesma função quadrática, confirmando as raízes exatas $x_1 = 6.40512484$ e $x_2 = -1.40512484$.
    * **Letra C (Método da Bisseção):** Refinamento da raiz em $[5, 10]$ com tolerância de $4 \times 10^{-3}$, convergindo para $x \approx 6.40380859$ em 11 iterações.

* **Questão 5.2:** Análise de uma função cúbica.
    * **Letra A (Busca Incremental):** Identificação de possível raiz para $f(x) = 5x^3 - 5x^2 + 6x - 2$ no intervalo $[0, 1]$ com 20 subdivisões, detectando mudança de sinal em $[0.4, 0.45]$.
    * **Letra B (Método da Bisseção):** Refinamento da raiz no mesmo intervalo com tolerância de $0.1$, convergindo para $x \approx 0.43750000$ em 4 iterações.

* **Questão 5.3:** Análise de uma função polinomial de 5º grau.
    * **Letra A (Busca Incremental):** Localização de raiz para $f(x) = -25 + 82x - 90x^2 + 44x^3 - 8x^4 + 0.7x^5$ em $[0.5, 1.0]$ com 20 subdivisões, detectando em $[0.55, 0.60]$.
    * **Letra B (Método da Bisseção):** Convergência para $x \approx 0.75000000$ em 1 iteração com tolerância $1.0$.
    * **Letra C (Método da Falsa Posição):** Convergência para $x \approx 0.58801717$ em 2 iterações com tolerância $0.2$.

* **Questão 5.4:** Análise de uma função cúbica com múltiplas raízes.
    * **Letra A (Busca Incremental):** Identificação de raízes para $f(x) = -12 - 21x + 18x^2 - 2.75x^3$ em $[-1, 4]$ com 30 subdivisões, localizando em $[-0.5, 0]$ e $[2, 2.5]$.
    * **Letra B (Método da Bisseção):** Refinamento da raiz em $[-1, 0]$ com tolerância $1.0$, convergindo para $x \approx -0.5000000$ em 1 iteração.
    * **Letra C (Método da Falsa Posição):** Refinamento da raiz em $[-1, 0]$ com tolerância $1.0$, convergindo para $x \approx -0.40523213$ em 3 iterações.

* **Questão 5.5:** Análise de uma função transcendente.
    * **Letra A (Busca Incremental):** Localização de raiz para $f(x) = \sin(x) - x^3$ em $[0.5, 1.0]$ com 20 subdivisões, detectando em $[0.95, 1.0]$.
    * **Letra B (Método da Bisseção):** Refinamento da raiz em $[0.5, 1.0]$ com tolerância $2$, convergindo para $x \approx 0.75000000$ em 1 iteração.

* **Questão 5.13:** Problema de engenharia com função complexa.
    * **Letra A (Método da Falsa Posição):** Refinamento de raiz para $f(x) = 9.8x/15 \cdot (1 - \exp(-15/(x \cdot 9))) - 35$ em $[50, 100]$ com tolerância $0.1$, convergindo para $x \approx 60.02274939$ em 2 iterações.

### Capítulo 6 - Métodos Abertos (Páginas 136 e 137)

* **Questão 6.2:** Análise de uma função cúbica com múltiplos métodos abertos.
    * **Letra A (Busca Incremental):** Pré-localização de raízes para $f(x) = 2x^3 - 11.7x^2 + 17.7x - 5$ em $[0, 4]$ com 20 subdivisões, identificando em $[0.3, 0.4]$, $[1.5, 1.6]$ e $[3.5, 3.6]$.
    * **Letra B (Método do Ponto Fixo):** Convergência para $x \approx 3.05812578$ em 1 iteração (tolerância $1$, $g(x) = ((11.7x^2 - 17.7x + 5)/2)^{1/3}$, $x_0 = 3$).
    * **Letra C (Método de Newton-Raphson):** Convergência para $x \approx 4.26975006$ em 2 iterações (tolerância $1$, $x_0 = 3$).
    * **Letra D (Método da Secante):** Convergência para $x \approx 3.32653061$ em 1 iteração (tolerância $1$, $x_0 = 4, x_1 = 3$).
    * **Letra E (Método da Secante Modificado):** Convergência para $x \approx 3.56316083$ em 9 iterações (tolerância $1 \times 10^{-6}$, $x_0 = 3.0$, $\delta = 0.01$).

* **Questão 6.5:** Análise da sensibilidade do Método de Newton-Raphson ao chute inicial.
    * **Letra A (Método de Newton-Raphson):** Convergência para $x \approx 0.2068570$ em 18 iterações (tolerância $0.1$, $x_0 = 4.52$) para $f(x) = -1 + 5.5x - 4x^2 + 0.5x^3$.
    * **Letra B (Método de Newton-Raphson):** Convergência para $x \approx 6.40463041$ em 11 iterações (tolerância $1$, $x_0 = 4.54$) para a mesma função, demonstrando a influência do chute inicial.

* **Questão 6.10:** Análise de função transcendente com métodos abertos.
    * **Letra A (Busca Incremental):** Pré-localização de raiz para $f(x) = 8\sin(x)\exp(-x) - 1$ em $[0, 1]$ com 20 subdivisões, detectando em $[0.1, 0.15]$.
    * **Letra B (Método de Newton-Raphson):** Convergência para $x \approx 0.14501481$ em 4 iterações (tolerância $1 \times 10^{-3}$, $x_0 = 0.3$).
    * **Letra C (Método da Secante):** Convergência para $x \approx 0.14501497$ em 6 iterações (tolerância $1 \times 10^{-3}$, $x_0 = 0.4, x_1 = 0.5$).
    * **Letra D (Método da Secante Modificado):** Convergência para $x \approx 0.14501481$ em 5 iterações (tolerância $1 \times 10^{-6}$, $x_0 = 0.3$, $\delta = 0.01$).

* **Questão 6.24:** Análise de função polinomial de 4º grau.
    * **Letra A (Busca Incremental):** Pré-localização de raiz para $f(x) = 0.0074x^4 - 0.284x^3 + 3.355x^2 - 12.183x + 5$ em $[15, 20]$ com 30 subdivisões, detectando em $[18.8, 19.0]$.
    * **Letra B (Método de Newton-Raphson):** Convergência para $x \approx 0.46847975$ em 9 iterações (tolerância $1 \times 10^{-6}$, $x_0 = 16.15$).

## Estrutura do Repositório

* `metodos_atividade1.py`: Contém todo o código-fonte dos métodos e a interface interativa.
* * `Metodos_numericos_para_engenharia`: Livro da disciplina.
* `Relatório/`: Pasta contendo o relatório acadêmico e suas figuras geradas.
    * `Relatório/Figuras/`: Contém as imagens dos gráficos e saídas do console para as questões resolvidas.
* `testes.py`: Testes unitários para verificar a funcionalidade dos métodos implementados.
* `README.md`: Este arquivo.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Autor

Amanda Lopes
