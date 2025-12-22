# Sistema de Pedidos de Açaí
- Projeto desenvolvido em Python para simular um terminal de autoatendimento de uma loja de açaí.
- O foco principal foi praticar lógica de programação, validação de dados e manipulação de listas.

## 🎯 Objetivo
Treinar conceitos fundamentais da linguagem Python, como:
- **Estruturas de Repetição:** Uso de `while` para loops de escolha.
- **Estruturas Condicionais:** Aplicação de `if / elif / else` para seleção de menus.
- **Manipulação de Listas:** Uso de `append()`, `len()` e verificações de pertinência (`in`).
- **Tratamento de Strings:** Padronização de entradas com `.lower()` e `.capitalize()`.
- **Interação com Sistema:** Uso da biblioteca `os` para limpar o terminal e `sys` para encerrar o programa.

## 🚀 Funcionalidades
- **Menu de Tamanhos:** Escolha entre 300ml, 500ml e 750ml com preços específicos.
- **Limite de Ingredientes:** O sistema permite a escolha de exatamente 3 acompanhamentos por pedido.
- **Validação de Estoque:** Verifica se o ingrediente digitado consta na lista de itens disponíveis.
- **Interface Limpa:** Limpeza automática do console para melhorar a legibilidade durante o uso.
- **Opção de Saída:** Encerramento seguro do programa através da opção [S].

## 🧠 Aprendizados e Desafios
Durante o desenvolvimento, foquei em resolver problemas reais de lógica:
1. Ajustei a posição do `os.system("cls")` para garantir que mensagens importantes não sumissem antes de serem lidas.
2. Implementei métodos de string para que o programa não diferenciasse "Morango" de "morango".
3. Refinei o loop `while` para garantir que o usuário não ultrapassasse o limite de 3 ingredientes.

Feedbacks e sugestões são bem-vindos