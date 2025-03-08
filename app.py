from flask import Flask, render_template, request
import fornecedores  # Módulo de fornecedores
import consumidor    # Módulo de consumidor
import transportadoras  # Módulo de transportadoras

# Criando o app Flask
app = Flask(__name__)

# Rota principal que exibe a página de escolha do produto
@app.route('/')
def index():
    # Lista de produtos disponíveis para o consumidor escolher
    produtos_disponiveis = ['Arroz', 'Trigo', 'Milho', 'Cevada']
    return render_template('index.html', produtos=produtos_disponiveis)

# Rota para quando o consumidor escolhe um produto
@app.route('/escolher_produto', methods=['POST'])
def escolher_produto():
    # Obtendo o produto escolhido pelo consumidor
    produto_nome = request.form['produto_nome']

    # Obter as pontuações do produto do fornecedor
    pontuacoes_por_produto_localizacao = fornecedores.somar_pontuacoes_por_produto_localizacao()

    # Obter as pontuações de transportadoras por origem do percurso
    pontuacoes_por_transportadora_origem = transportadoras.somar_pontuacoes_por_transportadora_origem()

    # Filtra as pontuações relacionadas ao produto escolhido nos fornecedores
    impactos_fornecedores = [(localizacao, pontuacao) for (produto, localizacao), pontuacao in pontuacoes_por_produto_localizacao.items() if produto == produto_nome]
    
    if not impactos_fornecedores:
        return f"Produto {produto_nome} não encontrado nos fornecedores.", 404

    # Filtra as pontuações relacionadas ao produto escolhido nos transportes
    impactos_transportadoras = [(origem_percurso, pontuacao) for (transportadora, origem_percurso), pontuacao in pontuacoes_por_transportadora_origem.items()]

    # Combinar os impactos de fornecedores e transportes
    impactos_totais = []
    for (localizacao, impacto_fornecedor) in impactos_fornecedores:
        impacto_transporte = next((impacto for (origem_percurso, impacto) in impactos_transportadoras if origem_percurso == localizacao), 0)
        impacto_total = impacto_fornecedor + impacto_transporte
        impactos_totais.append((localizacao, impacto_total))

    # Determinar a localização com o menor impacto total
    menor_impacto = min(impactos_totais, key=lambda x: x[1])
    localizacao_menor_impacto, impacto_total = menor_impacto
    
    # Resumo dos diferentes impactos ambientais (fornecedores e transportadoras)
    resumo_impactos = {
        'fornecedores': sum(impacto for _, impacto in impactos_fornecedores),
        'transportes': sum(impacto for _, impacto in impactos_transportadoras)
    }

    # Passa os resultados para a página de resultados
    return render_template('resultado.html', produto=produto_nome, impactos=impactos_totais, menor_impacto=(localizacao_menor_impacto, impacto_total), resumo_impactos=resumo_impactos)

# Execução do app
if __name__ == "__main__":
    app.run(debug=True)

