# API Gerador de vocabulários e vetores para NLP

Várias aplicações de processamento de linguagem natural necessitam que o texto seja formatado 
de forma estruturada, diferente da linguagem natural. Uma solução para isso é organizar as palavras 
do texto em um vetor que represente o documento em termos das palavras que ocorrem no mesmo.

## Funcionalidade

* Adicione quantos textos quiser
* API retornará os textos, o vocabulário 1-gram e 2-gram e os vetores 1-gram e 2-grams de cada texto

## Utilização

### Com interface gráfica

* Se preferir usar uma interface gráfica vá para o endpoint "/home" e lá poderar adicionar os textos e resetar o banco de dados através de uma caixa de entradas e botões intuitivos.

### Sem interface gráfica

#### Endpoints:

* *"/adc_text"* -> Adiciona textos ao banco de dados já fazendo os algorítmos necessários através de um POST, usando JSON com o tipo "texto"

##### ex: curl --request POST --url http://127.0.0.1:8000/adc_texto  --data '{"texto" : "o_texto_em_si_vem_aqui"}'

* *"/"* -> Recebe os textos adicionados, os vocabulários e os vetores através de um GET

##### ex: curl --request GET --url http://127.0.0.1:8000/

* *"/reset"* -> Reseta o banco de dados e limpa todos os textos

##### ex: curl --request POST --url http://127.0.0.1:8000/reset
