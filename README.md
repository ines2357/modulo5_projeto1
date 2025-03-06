# modulo5_projeto1

O projeto tem como objetivo a construção de uma aplicação para gestão de encomendas para fornecer o Continente do Centro Comercial Colombo, tendo em conta o impacto ambiental que a produção e transporte dos seus produtos provocam. 

Assim sendo, foi considerado a comercialização de quatro produtos (arroz, trigo, milho e cevada), que são produzidos em três localizações diferentes (ver tabela 1).

Tabela 1: Lista de fornecedores e produtos.

![Produtos](https://github.com/user-attachments/assets/7c75f8ba-e24d-4331-8fdb-5df9b9bab02f)


Foi considerado que cada localização tem uma transportadora associada que irá fornecer o consumidor final definido para o projeto, o Centro Comercial Colombo (figura 1). 

Figura 1: Diagrama de Processo.

![Diagrama de Processo](https://github.com/user-attachments/assets/322ba14b-c0de-4686-8f1d-a6805a4aaf66)



Para a realização da aplicação, foram criados três ramos, um para definir o impacto ambiental provocado pela produção (fornecedores), um para definir o impacto ambiental provocado pelo transporte (transportadoras) e um último para definir a escolha do consumidor (Continente do CC Colombo). 

No caso dos ramos fornecedores e transportadoras, cada um tem uma aplicação que calcula o impacto ambiental, uma apliação de teste que verifica que o cálculo está correto e um ficheiro csv que contém os dados usados para a construção da aplicação do ramo. 
No caso do ramo consumidor final, este tem a aplicação onde o consumidor pode fazer a sua encomenda, figura 2: 

Figura 2: Documentos dos ramos fornecedores, transportadoras e consumidor final. 

![image](https://github.com/user-attachments/assets/cc429229-abd9-4daf-9d53-f67675ee4eaa)

Adicionalmente, criou-se um ramo referências para repositório de referências e material auxiliar. 

Por último, as variáveis usadas na construção das diferentes aplicações estão descritas na figura 3. 

Figura 3: Variáveis. 

![Variáveis](https://github.com/user-attachments/assets/4cf9ba05-bf6e-47e7-a0e7-3effc3fa144c)

A junção das diferentes aplicações de cada ramo numa aplicação final foi feita no master: app.py.








