import csv
import collections

def somar_pontuacoes_por_produto_localizacao():
    # Dicionário para armazenar a soma total das pontuações por produto e localização
    pontuacoes_por_produto_localizacao = collections.defaultdict(lambda: 0)
    
    # Ler o ficheiro CSV
    with open('fornecedores.csv', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Ignorar cabeçalho
        
        for row in reader:
            localizacao = row[0]
            produto = row[1]
            chave = (produto, localizacao)
            pontuacao_total = sum(map(int, row[2:]))  # Somar todas as pontuações
            
            # Acumular a soma total
            pontuacoes_por_produto_localizacao[chave] += pontuacao_total
    
    return pontuacoes_por_produto_localizacao

# Testar a função
if __name__ == "__main__":
    resultado = somar_pontuacoes_por_produto_localizacao()
    for chave, valor in resultado.items():
        print(f"{chave}: {valor}")


