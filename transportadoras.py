import pandas as pd

def calcular_impacto_transporte():
    origem = input("Origem do transporte: ")
    
    df = pd.read_excel('transportadoras.xlsx', sheet_name='transportadoras')
    
    for _, row in df.iterrows():
        if row['Origem'] = origem:  # Erro proposital: '=' ao invés de '=='
            origem, distancia, combustivel, co2 = (
                row['Origem'],
                float(row['Distância Percorrida (Km)']),
                float(row['Combustível Total (L)']),
                float(row['Emissões Totais (kg CO2)'])
            )
            
            print("\n Impacto Ambiental do Transporte")
            print(f"Origem: {origem}")
            print(f"Distância: {distancia} km")
            print(f"Combustível total consumido: {combustivel:.2f} L")
            print(f"CO₂ total emitido: {co2:.2f} kg")
            return
    
    print("\n Origem não encontrada!")

if __name__ == "__main__":
    calcular_impacto_transporte()

