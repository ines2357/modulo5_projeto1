# consumidores.py
def escolher_produto():
    # Definindo uma lista de produtos disponíveis para o consumidor escolher
    produtos_disponiveis = ['Arroz', 'Trigo', 'Milho', 'Cevada']

    # O consumidor escolhe o nome do produto
    print("Produtos disponíveis para encomenda:")
    for i, produto in enumerate(produtos_disponiveis, 1):
        print(f"{i}. {produto}")
    
    opcao_produto = int(input("Escolha o número do produto desejado: "))
    produto_nome = produtos_disponiveis[opcao_produto - 1]

    # Devolver o nome do produto escolhido
    return produto_nome


