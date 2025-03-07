import csv
import collections

def somar_pontuacoes_por_transportadora_origem():
    #Dicionário para armazenar a soma total das pontuações por transportadora e origem do percurso
    pontuacoes_por_transportadora_origem = collections.defaultdict(lambda: 0)
    
    #Ler o ficheiro CSV com delimitador ";"
    with open('transportadoras.csv', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',')  # Define "," como delimitador
        next(reader)  #Ignorar cabeçalho
        
        for row in reader:
            origem_percurso = row[0]
            transportadora = row[1]
            chave = (transportadora, origem_percurso)
            
            #Converter os valores numéricos de forma correta
            score_combustivel = int(row[3])  # Coluna 'score_combustivel'
            score_emissoes = int(row[4])     # Coluna 'score_emissoes'
            pontuacao_total = score_combustivel + score_emissoes  # Somar os scores relevantes
            
            #Fazer a soma total
            pontuacoes_por_transportadora_origem[chave] += pontuacao_total
    
    return pontuacoes_por_transportadora_origem



