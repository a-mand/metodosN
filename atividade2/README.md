### README - Calculadora de Sistemas de Equações Lineares

#### 1. Visão Geral
Este projeto consiste na implementação de uma calculadora de Sistemas de Equações Lineares. O objetivo é resolver sistemas de equações lineares, lidando com os três cenários possíveis: solução única, infinitas soluções e a ausência de solução (sistema inconsistente). A rotina foi implementada "do zero", sem a utilização de bibliotecas prontas como `numpy.linalg.solve` para as operações de eliminação.

#### 2. Funcionalidades
O programa segue um fluxo de trabalho em etapas:

1.  **Entrada do Sistema:** O usuário fornece o sistema linear ou a matriz aumentada correspondente. A matriz pode ter qualquer dimensão ($m$ linhas por $n$ colunas).

2.  **Redução à Forma Escalonada:** A matriz de entrada é processada através de operações elementares com linhas para alcançar a forma escalonada.
    * **Tratamento de Pivôs Nulos:** Se um pivô for zero, a linha é permutada com a primeira linha abaixo dela que possua um pivô não nulo na mesma coluna. Caso todos os elementos abaixo sejam nulos, o processamento é interrompido e a rotina passa para a próxima coluna.
    * **Otimização:** Elementos que já são nulos não são processados novamente.
    * **Verificação de Inconsistência:** O programa verifica a ocorrência de equações inconsistentes ($0x_1 + ... + 0x_n = b$ com $b \ne 0$). Caso isso ocorra, o processamento é interrompido e o sistema é declarado como sem solução.
    * **Feedback Visual:** A matriz é impressa a cada etapa de eliminação de uma coluna, e a matriz escalonada final é exibida.

3.  **Redução à Forma Canônica:** A partir da matriz na forma escalonada, o programa continua as operações elementares, desta vez de baixo para cima, para obter a forma canônica. A matriz na forma canônica é então impressa.

4.  **Análise e Solução:** O programa analisa a forma canônica da matriz para determinar o tipo de solução.
    * **Solução Única:** Se o número de equações com pivôs ($r$) for igual ao número de incógnitas ($n$), a solução única é exibida.
    * **Infinitas Soluções:** Se o número de equações com pivôs ($r$) for menor que o número de incógnitas ($n$), o programa exibe a quantidade de variáveis livres ($n-r$) e a solução geral em termos dessas variáveis.

#### 3. Exemplos
A rotina foi testada com os seguintes problemas do material de apoio para demonstrar sua funcionalidade em todos os cenários possíveis:
* **Problema 2.2:** Sistema inconsistente (sem solução).
* **Problema 2.3:** Sistema com solução única.
* **Problema 2.4:** Sistema com infinitas soluções (uma variável livre).
* **Problema 2.1:** Sistema com infinitas soluções (duas variáveis livres).