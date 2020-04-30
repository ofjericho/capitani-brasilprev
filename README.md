# Desafio Python

O stackoverflow é um site de perguntas e respostas enviadas pelos usuários do
site. Todos conhecemos. ;)

A ideia do desafio é fazer um cliente que consuma a (api)[https://api.stackexchange.com/docs] do stackoverflow.


## Entrada
- Palavras chave para a pesquisa no stackoverflow

### Parte 1

Fazer uma interface em linha de comando que receba a pesquisa e imprima
o titulo da pergunta, o número de votos e o link para a resposta.

### Parte 2

Fazer um robô no telegram que receba as suas pesquisas e te mostre as respotas
com os links.


# Resolução

### Clone do projeto

Realizar o clone do projeto 

git clone https://github.com/ofjericho/capitani-brasilprev.git

### Criação do ambiente virtual

Para criação do ambiente virtual:

- entrar no diretório capitani-brasilprev
- python -m venv .venv

### Instalação dos requisitos

Para instalação dos requisitos 

- pip install -r requirements.txt

### Executar a aplicação em linha de comando

Para executarmos a aplicação em linha de comando

- python main.py

### Para utilização da aplicação

- Digitar a palavra chave ou texto para busca no Stackoverflow
- Serão listado questões relativo à busca desejada com o score e o link para as respostas
- Será enviado nesse momento um alerta para o Telegran sobre a consulta realizada

