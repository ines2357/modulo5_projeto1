# Introdução

O projeto tem como objetivo a construção de uma aplicação para gestão de encomendas para fornecer o Continente do Centro Comercial Colombo, tendo em conta o impacto ambiental que a produção e transporte dos seus produtos provocam.
Assim sendo, foi considerado a comercialização de quatro produtos (arroz, trigo, milho e cevada), que são produzidos em três localizações diferentes (ver tabela 1).

Tabela 1: Lista de fornecedores e produtos.

<img width="602" alt="imagem" src="https://github.com/user-attachments/assets/9e3b6c2c-c73a-4d37-be32-e250d690df48" />


# Diagrama de processo

Foi considerado que cada localização tem uma transportadora associada que irá fornecer o consumidor final definido para o projeto, o Centro Comercial Colombo (figura 1).

![imagem](https://github.com/user-attachments/assets/6ae3dde1-276b-4819-b182-528d79cdcf9c)

Figura 1: Diagrama de Processo.

# Fatores de impacto ambiental

Para a análise dos impactos ambientais dos fornecedores e das transportadoras, existem duas categorias de impacto ambiental: os recursos consumidos e a poluição gerada (tabela 2).

Os recursos consumidos pelos fornecedores são calculados com base: na água utilizada na rega; na eletricidade das instalações; e nos combustíveis utilizados pelas máquinas agrícolas. A poluição gerada pelos fornecedores foi calculada com base: no desperdício alimentar; na contaminação dos solos através de pesticidas; e nas emissões de CO2 associadas ao cultivo dos produtos.

Os recursos consumidos pelas transportadoras são calculados com base no combustível utilizado pelos camiões de transporte. A poluição gerada pelas transportadoras foi calculada com base nas emissões de CO2 associadas aos camiões.

Tabela 2: categorias de impacto ambiental

![imagem](https://github.com/user-attachments/assets/39ac9a62-c909-4761-8fa4-e7e7c472a2d8)


# Organização dos dados

O processo de organização dos dados começou com a recolha e tratamento destes. Primeiramente, foram pesquisados e recolhidos os dados relevantes. Após esta etapa, os scores foram calculados utilizando o Excel, onde se aplicaram fórmulas e critérios predefinidos. Depois do cálculo, os dados foram armazenados num ficheiro CSV, facilitando o processamento e a importação dos dados pelos ficheiros de python. 

Para o cálculo dos scores, adotou-se uma escala de 1 a 5. Inicialmente, determinou-se a diferença entre o valor mínimo e o valor máximo dos dados recolhidos para cada categoria. De seguida, essa diferença foi dividida por cinco, criando intervalos que serviram como referência para a classificação. Por fim, os scores foram atribuídos de acordo com esses intervalos, garantindo uma padronização na avaliação dos diferentes critérios analisados.

# Divisão de ramos no GitHub

Para a realização da aplicação final, foram criados cinco ramos, um para definir o impacto ambiental provocado pela produção (fornecedores), um para definir o impacto ambiental provocado pelo transporte (transportadoras) e um último para definir a escolha do consumidor (consumidor_final). Existe ainda o ramo main, que contém a aplicação final e as suas dependências, e um ramo referências, para repositório de referências e material auxiliar.

No caso dos ramos fornecedores e transportadoras, cada um tem uma aplicação que calcula o impacto ambiental, uma aplicação de teste que verifica que o cálculo está correto, um ficheiro csv que contém os dados usados para a construção da aplicação do ramo, e um ficheiro xlsx para o cálculo dos scores. No caso do ramo consumidor_final, este tem a aplicação onde o consumidor pode fazer a sua encomenda, como é possível observar na figura 2:

![imagem](https://github.com/user-attachments/assets/17a518ab-9f92-4b62-b653-366a5aee734e)

Figura 2: Documentos dos ramos fornecedores, transportadoras e consumidor_final.

A figura 3 apresenta os documentos incluídos no ramo main: a aplicação final (app.py), os templates da aplicação (ficheiros html), e um ficheiro txt para armazenar o histórico das escolhas do consumidor. No ramo das referências, incluíram-se ficheiros com as referências e outro material acessório.

![imagem](https://github.com/user-attachments/assets/ce034f74-13db-48f0-9cc3-a32f10bb4946)

Figura 3: Documentos dos ramos main e referências

# Funções e variáveis

As funções e variáveis usadas na construção das diferentes aplicações estão descritas nas tabelas 3 e 4.

Tabela 3: Funções e variáveis fornecedores e transportadoras

![imagem](https://github.com/user-attachments/assets/679f8563-6f27-44e4-be87-5eaa1da0d7e6)

Tabela 4: Funções e variáveis consumidor e app

![imagem](https://github.com/user-attachments/assets/c2534fc3-7584-4bde-8995-6e81baa040cf)

# Fluxo das funções

A seguinte figura apresenta uma visualização do fluxo das funções, desde as aplicações python que contêm os dados dos fornecedores, transportadores e consumidor, até às dependências da aplicação final, que corre em html (figura 4). Após correr o script app.py, o resultado será a página web, com a qual o consumidor interage, e o ficheiro com o histórico de escolhas.

![imagem](https://github.com/user-attachments/assets/01e70561-fa28-473d-b1bd-5ebf3cdfe45c)

Figura 4: Fluxo das funções

O script app.py corre através do comando:

> python3 app.py

Após correr o comando, a página web fica disponível através de: 

> http://127.0.0.1:5000

