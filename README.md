# 🛒 Calculadora de Compras de Mercado

Este é um projeto desenvolvido como parte de um desafio de programação na faculdade UNISUAM. O programa permite registrar produtos, calcular o valor total da compra e aplicar descontos com base na forma de pagamento.

---

## 💡 Funcionalidades

- Cadastro de produtos com nome, preço e quantidade  
- Cálculo do subtotal de cada item e total geral da compra  
- Aplicação de desconto de acordo com a forma de pagamento:
  - **À vista:**
  - 15% de desconto para compras acima de R$200
  - 10% de desconto entre R$100 e R$200
  - Sem desconto abaixo de R$100
  - **Cartão de crédito:** sem desconto  
- Exibição de relatório final detalhado da compra

---

## 💻 Tecnologias Utilizadas

- Linguagem: **Python 3.12.3**
- Conceitos: entrada de dados, listas, laços, condicionais, operações matemáticas e formatação de strings

---

## ▶️ Como Executar

1. Certifique-se de ter o Python instalado (versão 3.10+ recomendada)
2. Clone o repositório ou baixe o arquivo `calculadora_mercado.py`
3. Execute no terminal:

    ```bash
    python calculadora_mercado.py
    ```

## 📋 Exemplo de Uso

```plaintext
Informe quantos produtos serão registrados: 2
Produto 1:
Nome do produto: Arroz
Preço unitário (R$): 20
Quantidade comprada: 2

Produto 2:
Nome do produto: Feijão
Preço unitário (R$): 10
Quantidade comprada: 3

Total bruto da compra: R$ 70.00
INFORME QUAL SERÁ A SUA FORMA DE PAGAMENTO
(1) = À vista | (2) = Cartão de crédito
Digite sua forma de pagamento: 1

RELATÓRIO FINAL
Produto: Arroz
  Quantidade: 2
  Preço unitário: R$ 20.00
  Subtotal: R$ 40.00
Produto: Feijão
  Quantidade: 3
  Preço unitário: R$ 10.00
  Subtotal: R$ 30.00
Total bruto: R$ 70.00
Desconto aplicado: 0%
Total final a pagar: R$ 70.00
```

**Carlos Aguiar da Silva**  
- GitHub: [carlostechcode](https://github.com/carlostechcode)  
- LinkedIn: [Carlos Aguiar](https://www.linkedin.com/in/carlostechcode)
