from flask import Flask, render_template, request
import fornecedores  
import consumidor    

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    produtos_disponiveis = ['Arroz', 'Trigo', 'Milho', 'Cevada']

    
    impacto_resultado = None
    produto_escolhido = None
    novos_produtos = []
    pontuacoes = {}

    
    if request.method == 'POST':
        produto_nome = request.form['produto_nome']
        produto_escolhido = produto_nome

        
        pontuacoes_por_produto_localizacao = fornecedores.somar_pontuacoes_por_produto_localizacao()

       
        impactos = [(localizacao, pontuacao) for (produto, localizacao), pontuacao in pontuacoes_por_produto_localizacao.items() if produto == produto_nome]

        if impactos:
            
            menor_impacto = min(impactos, key=lambda x: x[1])
            localizacao_menor_impacto, impacto_total = menor_impacto
            impacto_resultado = (localizacao_menor_impacto, impacto_total)

        
        for (produto, localizacao), pontuacao_total in pontuacoes_por_produto_localizacao.items():
            recursos = pontuacao_total * 0.6 
            poluicao = pontuacao_total * 0.4 
            pontuacoes[(produto, localizacao)] = {'recursos': recursos, 'poluicao': poluicao}

            if produto not in novos_produtos:
                novos_produtos.append(produto)

    
    return render_template('index.html', 
                           produtos=produtos_disponiveis, 
                           produto_escolhido=produto_escolhido,
                           impacto_resultado=impacto_resultado,
                           pontuacoes=pontuacoes,
                           novos_produtos=novos_produtos)


if __name__ == "__main__":
    app.run(debug=True)


