import csv

def fornecedores_impacto():
    with open('fornecedores_final.csv', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
    
        print("Calculando impacto ambiental...\n--------------------------------")
        for row in reader:
            localizacao, produto, score_agua, score_eletricidade, score_combustiveis, score_desperdicio, score_contaminacao, score_emissoes, score_final = row[0], row[1], row[2], row[3], row[4], row [5], row[6], row[7], row[8]
            print(f"Localização: {localizacao} | Produto: {produto} | Consumo de água: {score_agua} | Consumo de eletricidade: {score_eletricidade} | Combustível máq. agrícolas: {score_combustiveis} | Desperdício alimentar: {score_desperdicio} | Contaminação dos solos: {score_contaminacao} | Emissões Co2: {score_emissoes}")
            print(f"Localização: {localizacao} | Produto: {produto} | Pontuação de impacto ambiental do fornecedor: {score_final}")
        print("--------------------------------")

if __name__ == "__main__":
    fornecedores_impacto()
