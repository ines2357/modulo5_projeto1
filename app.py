from flask import Flask, render_template, request
import fornecedores
import consumidor
import transportadoras


app = Flask(__name__)

@app.route('/')
def index():
    produtos_disponiveis = ['Arroz', 'Trigo', 'Milho', 'Cevada']
    return render_template('index.html', produtos=produtos_disponiveis)

@app.route('/escolher_produto', methods=['POST'])
def escolher_produto():
    produto_nome = request.form['produto_nome']
    produto_nome = consumidor.escolher_produto(produto_nome)
    
    # Decompõe corretamente a tupla retornada pelas funções
    pontuacoes_por_produto_localizacao, scores_fornecedores = fornecedores.somar_pontuacoes_por_produto_localizacao()
    pontuacoes_por_transportadora_origem, scores_transportadoras = transportadoras.somar_pontuacoes_por_transportadora_origem()

    # Se você precisar das pontuações totais, use pontuacoes_por_produto_localizacao
    impactos_fornecedores = [
        (localizacao, pontuacao) 
        for (produto, localizacao), pontuacao in pontuacoes_por_produto_localizacao.items() 
        if produto == produto_nome
    ]
    
    # Calcula os impactos das transportadoras
    impactos_transportadoras = [
        (origem_percurso, pontuacao) 
        for (transportadora, origem_percurso), pontuacao in pontuacoes_por_transportadora_origem.items()
    ]
    
    # Calculando o impacto total
    impactos_totais = []
    for (localizacao, impacto_fornecedor) in impactos_fornecedores:
        impacto_transporte = next(
            (impacto for (origem_percurso, impacto) in impactos_transportadoras if origem_percurso == localizacao),
            0
        )
        impacto_total = impacto_fornecedor + impacto_transporte
        impactos_totais.append((localizacao, impacto_total))

    # Encontrar o menor impacto
    menor_impacto = min(impactos_totais, key=lambda x: x[1])
    localizacao_menor_impacto, impacto_total = menor_impacto

    return render_template('resultado.html', 
                           produto=produto_nome,
                           impactos=impactos_totais, 
                           menor_impacto=(localizacao_menor_impacto, impacto_total))




@app.route('/resumo_impactos')
def resumo_impactos():
   
    pontuacoes_por_produto_localizacao = fornecedores.somar_pontuacoes_por_produto_localizacao()
    pontuacoes_por_transportadora_origem = transportadoras.somar_pontuacoes_por_transportadora_origem()

   
    print("Pontuações por produto e localização:")
    print(pontuacoes_por_produto_localizacao)

    print("Pontuações por transportadora e origem:")
    print(pontuacoes_por_transportadora_origem)

    pontuacoes_por_produto_localizacao_dict = dict(pontuacoes_por_produto_localizacao)
    pontuacoes_por_transportadora_origem_dict = dict(pontuacoes_por_transportadora_origem)

    print("Pontuações por produto e localização (convertidas em dicionário):")
    print(pontuacoes_por_produto_localizacao_dict)

    print("Pontuações por transportadora e origem (convertidas em dicionário):")
    print(pontuacoes_por_transportadora_origem_dict)

    dados_resumo = []

    for (localizacao, produto), pontuacao in pontuacoes_por_produto_localizacao_dict.items():
        
        score_agua = pontuacao.get('score_agua', 0) if isinstance(pontuacao, dict) else 0
        score_eletricidade = pontuacao.get('score_eletricidade', 0) if isinstance(pontuacao, dict) else 0
        score_combustiveis = pontuacao.get('score_combustiveis', 0) if isinstance(pontuacao, dict) else 0
        score_desperdicio = pontuacao.get('score_desperdicio', 0) if isinstance(pontuacao, dict) else 0
        score_contaminacao = pontuacao.get('score_contaminacao', 0) if isinstance(pontuacao, dict) else 0
        score_emissoes = pontuacao.get('score_emissoes', 0) if isinstance(pontuacao, dict) else 0

        transportadora_data = next(
            (data for (origem_percurso, transportadora), data in pontuacoes_por_transportadora_origem_dict.items() if origem_percurso == localizacao),
            None
        )

        if transportadora_data:
            score_combustivel = transportadora_data.get('score_combustivel', 0)
            score_emissoes_transporte = transportadora_data.get('score_emissoes', 0)
        else:
            score_combustivel = 0
            score_emissoes_transporte = 0

        dados_resumo.append({
            'produto': produto,
            'localizacao': localizacao,
            'score_agua': score_agua,
            'score_eletricidade': score_eletricidade,
            'score_combustiveis_fornecedor': score_combustiveis,
            'score_desperdicio': score_desperdicio,
            'score_contaminacao': score_contaminacao,
            'score_emissoes': score_emissoes,
            'score_combustiveis_transportadora': score_combustivel,
            'score_emissoes_transportadora': score_emissoes_transporte
           
})

 
    return render_template('resumo_impactos.html', dados_resumo=dados_resumo)


@app.route('/historico')
def historico():

    caminho_arquivo = './historico_de_escolhas.txt'
    
    try:
        with open(caminho_arquivo, "r") as arquivo:
            escolhas = arquivo.readlines()
    except FileNotFoundError:
        escolhas = []
    
    return render_template('historico.html', escolhas=escolhas)

if __name__ == "__main__":
    app.run(debug=True)




