
import fornecedores  
import consumidor    

# Função principal que gerencia o fluxo do programa
def main():
    # Chama o script do consumidor e permite que ele escolha o produto
    produto_nome = consumidor.escolher_produto()

    # Obter as pontuações do produto do fornecedor
    pontuacoes_por_produto_localizacao = fornecedores.somar_pontuacoes_por_produto_localizacao()

    # Filtra as pontuações relacionadas ao produto escolhido
    impactos = [(localizacao, pontuacao) for (produto, localizacao), pontuacao in pontuacoes_por_produto_localizacao.items() if produto == produto_nome]
    
    if not impactos:
        print(f"Produto {produto_nome} não encontrado.")
        return
    
    # Mostrar os resultados para o consumidor
    print(f"\nImpacto ambiental do produto '{produto_nome}':")
    for localizacao, impacto_total in impactos:
        print(f"\n- Localização: {localizacao}")
        print(f"  Impacto total: {impacto_total}")
    
    # Determinar a localização com o menor impacto ambiental
    menor_impacto = min(impactos, key=lambda x: x[1])
    localizacao_menor_impacto, impacto_total = menor_impacto
    
    print(f"\nO produto {produto_nome} com menor impacto ambiental corresponde ao local de produção {localizacao_menor_impacto}.")
   
# Execução do programa
if __name__ == "__main__":
    main()


