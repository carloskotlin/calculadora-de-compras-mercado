print("================================================")
print(" SOFTWARE PARA CÁLCULO E DESCONTO EM MERCADO")
print(" Desenvolvedor: Carlos Patrick Aguiar da Silva")
print("================================================")

# Entrada de dados
print("------------------------------------------------")
quantidade_produtos = int(input("Informe quantos produtos serão registrados: "))
print("------------------------------------------------")

produtos = []
total_geral = 0

# Processamento dos dados
for i in range(quantidade_produtos):
    print(f"Produto {i + 1}:")
    nome = input("Nome do produto: ")
    preco = float(input("Preço unitário (R$): "))
    quantidade = int(input("Quantidade comprada: "))
    
    subtotal = preco * quantidade
    total_geral += subtotal
    
    produtos.append({
        'nome': nome,
        'preco': preco,
        'quantidade': quantidade,
        'subtotal': subtotal
    })
    
    print("------------------------------------------------")

print(f"Total bruto da compra: R$ {total_geral:.2f}")
print("------------------------------------------------")

# Forma de pagamento e desconto
print("INFORME QUAL SERÁ A SUA FORMA DE PAGAMENTO\n(1) = À vista | (2) = Cartão de crédito")

while True:
    forma_pagamento = int(input("Digite sua forma de pagamento: "))
    if forma_pagamento == 1:
        if total_geral > 200:
            desconto = 0.15  # 15%
        elif 100 <= total_geral <= 200:
            desconto = 0.10  # 10%
        else:
            desconto = 0.0   # Sem desconto
        total_final = total_geral * (1 - desconto)
        break
    elif forma_pagamento == 2:
        desconto = 0.0
        total_final = total_geral
        break
    else:
        print("Opção inválida, entre com a opção correta!")

# Relatório final
print("------------------------------------------------")
print("RELATÓRIO FINAL")
print("------------------------------------------------")
for p in produtos:
    print(f"Produto: {p['nome']}")
    print(f"  Quantidade: {p['quantidade']}")
    print(f"  Preço unitário: R$ {p['preco']:.2f}")
    print(f"  Subtotal: R$ {p['subtotal']:.2f}")
    print("------------------------------------------------")

print(f"Total bruto: R$ {total_geral:.2f}")
print(f"Desconto aplicado: {desconto * 100:.0f}%")
print(f"Total final a pagar: R$ {total_final:.2f}")
