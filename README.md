# 100 Exercícios de Python

Este repositório reúne uma sequência de exercícios práticos em Python, organizados por módulos para o desenvolvimento gradual da lógica de programação e dos conceitos básicos da linguagem.

A proposta do material é consolidar a aprendizagem por meio da resolução de problemas simples, com foco em entrada e saída de dados, operadores matemáticos, conversões de tipos, estruturas condicionais e organização do código.

---

## Sobre o projeto

Os exercícios contemplam:

- leitura e escrita de dados com `input()` e `print()`
- conversão de tipos (`int()`, `float()`, `str()`)
- variáveis e operadores aritméticos
- uso de estruturas condicionais (`if`, `elif`, `else`)
- resolução de problemas aplicados à lógica computacional
- organização por módulos e níveis de complexidade

O material foi estruturado como um conjunto de atividades de estudo, com arquivos independentes para execução individual.

---

## Estrutura do repositório

```text
100Exercicios-Python/
├── README.md
├── Apoio-de-estudo/
│   ├── README.md
│   ├── if.py
│   ├── elif.py
│   ├── else.py
│   └── for.py
├── Modulo-01/
│   ├── exercicio_01.py
│   ├── exercicio_02.py
│   ├── exercicio_03.py
│   ├── exercicio_04.py
│   ├── exercicio_05.py
│   ├── exercicio_06.py
│   ├── exercicio_07.py
│   ├── exercicio_08.py
│   ├── exercicio_09.py
│   ├── exercicio_10.py
│   ├── exercicio_14.py
│   └── exercicio_15.py
├── Modulo-02/
│   ├── exercicio_16.py
│   ├── exercicio_17.py
│   ├── exercicio_18.py
│   ├── exercicio_19.py
│   ├── exercicio_20.py
│   ├── exercicio_21.py
│   ├── exercicio_22.py
│   ├── exercicio_23.py
│   ├── exercicio_24.py
│   ├── exercicio_25.py
│   ├── exercicio_26.py
│   ├── exercicio_27.py
│   ├── exercicio_28.py
│   ├── exercicio_29.py
│   ├── exercicio_30.py
│   ├── exercicio_31.py
│   ├── exercicio_32.py
│   ├── exercicio_33.py
│   ├── exercicio_34.py
│   └── exercicio_35.py
└── Fluxogramas.pdf
```

---

## Módulo 01 — fundamentos da linguagem

O primeiro módulo reúne os exercícios iniciais de Python e tem como objetivo introduzir os conceitos básicos da linguagem e da lógica de programação.

Nesse conjunto, os programas abordam:

- entrada de dados via terminal
- variáveis e operações matemáticas
- conversão de valores
- cálculos de soma, média, desconto e reajuste
- uso de `print()` para apresentar resultados
- organização básica do código

### Exercícios incluídos no módulo 01

- Exercício 01: soma de dois números
- Exercício 02: cálculo de média simples
- Exercício 03: antecessor e sucessor
- Exercício 04: dobro, triplo e metade
- Exercício 05: conversão de metros para centímetros e milímetros
- Exercício 06: cálculo de área e perímetro de um retângulo
- Exercício 07: conversão de Celsius para Fahrenheit
- Exercício 08: aplicação de desconto em um produto
- Exercício 09: reajuste de salário
- Exercício 10: cálculo de comissão de vendas
- Exercício 14: troca de valores entre variáveis
- Exercício 15: cálculo de compra com frete

Esse módulo foi essencial para consolidar a base da linguagem, principalmente em relação à leitura de dados do usuário e ao processamento de informações.

---

## Módulo 02 — estruturas condicionais e tomada de decisão

A partir do exercício 16, a abordagem passa a enfatizar a lógica condicional, em que o programa toma decisões com base em condições específicas.

Os conteúdos trabalhados incluem:

- `if`
- `elif`
- `else`
- comparação de valores
- classificação de números
- validação de regras por meio de condicionais
- resolução de problemas com estrutura de decisão

### Exercícios incluídos no módulo 02

- Exercício 16: positivo, negativo ou zero
- Exercício 17: par ou ímpar
- Exercício 18: maior entre dois números
- Exercício 19: desconto por faixa de valor
- Exercício 20: dia da semana
- Exercício 21: validação de senha
- Exercício 22: triângulo pelo ângulo
- Exercício 23: calculadora com tratamento de erros
- Exercício 24 a 35: continuação da prática com lógica condicional e exercícios mais elaborados

Esse módulo foi importante porque introduziu uma parte mais profunda da programação: além de calcular, o programa agora precisa tomar decisões com base em condições.

---

## Executáveis e por que eles existem

Alguns exercícios deste repositório incluem arquivos com extensão `.bat`, como `exercicio_16.bat`, `exercicio_17.bat` e assim por diante. Esses arquivos são executáveis do sistema operacional Windows e servem como uma camada simples para rodar o script Python correspondente.

Em termos práticos, o `.bat` funciona como um atalho automatizado. Em vez de o usuário precisar abrir o terminal e digitar algo como:

```bash
py exercicio_16.py
```

ou

```bash
python exercicio_16.py
```

basta clicar no arquivo `.bat` ou executá-lo diretamente no prompt de comando. Isso facilita muito o aprendizado, principalmente para quem está começando, porque reduz a necessidade de lembrar comandos e deixa a execução mais intuitiva.

O arquivo `.bat` não substitui o código em Python; ele apenas chama o interpretador do Python para rodar o arquivo `.py` automaticamente. Em muitos casos, o comando dentro do `.bat` tenta primeiro usar `py` e, se não estiver disponível, usa `python`. Essa estratégia aumenta a compatibilidade entre diferentes instalações do Windows e ajuda a garantir que o programa execute corretamente com menos esforço.

Essa abordagem é útil em projetos didáticos porque permite focar na lógica do programa em vez de perder tempo com detalhes de execução do ambiente. O código continua sendo Python puro, enquanto o `.bat` atua como um facilitador para abrir e testar os exercícios de forma prática.

---

## Observações

- Os arquivos estão organizados por módulo e por sequência numérica.
- O estudo foi desenvolvido de forma gradual, começando pelos fundamentos e avançando para estruturas condicionais mais complexas.
- A pasta `Apoio-de-estudo` reúne materiais complementares com exemplos práticos sobre `if`, `elif`, `else` e `for`.
- O arquivo `Fluxogramas.pdf` complementa a parte visual do conteúdo e auxilia na compreensão da lógica por meio de representações gráficas.
- Os arquivos `.bat` existem para simplificar a execução no Windows e servir como atalho para os scripts em Python.

---

## Objetivo do projeto

Este repositório representa uma etapa de aprendizagem em Python, com foco no desenvolvimento da lógica de programação e na aplicação de conceitos básicos em exercícios práticos.

Os desafios propostos têm como finalidade transformar noções teóricas em soluções concretas, por meio da escrita de scripts simples e da execução de comandos no terminal.

---

#### Projeto desenvolvido como material de estudo em lógica de programação e Python.




