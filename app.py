from flask import Flask, render_template, request
import fornecedores  
import consumidor    

app = Flask(__name__)

# Escolha do produto
@app.route('/')
def index():
    # Lista de produtos 
    produtos_disponiveis = ['Arroz', 'Trigo', 'Milho', 'Cevada']
    return render_template('index.html', produtos=produtos_disponiveis)

# Após a escolha
@app.route('/escolher_produto', methods=['POST'])
def escolher_produto():
    
    produto_nome = request.form['produto_nome']
    
    pontuacoes_por_produto_localizacao = fornecedores.somar_pontuacoes_por_produto_localizacao()

    impactos = [(localizacao, pontuacao) for (produto, localizacao), pontuacao in pontuacoes_por_produto_localizacao.items() if produto == produto_nome]
    
    if not impactos:
        return f"Produto {produto_nome} não encontrado.", 404
    
    # Determinar a localização com o menor impacto ambiental
    menor_impacto = min(impactos, key=lambda x: x[1])
    localizacao_menor_impacto, impacto_total = menor_impacto
    
    # Resultados para a página de resultados
    return render_template('resultado.html', produto=produto_nome, impactos=impactos, menor_impacto=(localizacao_menor_impacto, impacto_total))


if __name__ == "__main__":
    app.run(debug=True)


