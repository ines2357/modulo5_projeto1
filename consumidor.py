def escolher_produto():
    
    produtos_disponiveis = ['Arroz', 'Trigo', 'Milho', 'Cevada']

    print("Produtos disponíveis para encomenda:")
    for i, produto in enumerate(produtos_disponiveis, 1):
        print(f"{i}. {produto}")
    
    opcao_produto = int(input("Escolha o número do produto desejado: "))
    produto_nome = produtos_disponiveis[opcao_produto - 1]
    
    return produto_nome


