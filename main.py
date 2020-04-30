# -*- coding: UTF8 -*-
import sys
from search import context
from bot import telegram

'''
# Desafio Python

O stackoverflow é um site de perguntas e respostas enviadas pelos usuários do
site. Todos conhecemos. ;)

A ideia do desafio é fazer um cliente que consuma a
(api)[https://api.stackexchange.com/docs] do stackoverflow.


# Entrada
- Palavras chave para a pesquisa no stackoverflow

# Parte 1

Fazer uma interface em linha de comando que receba a pesquisa e imprima
o titulo da pergunta, o número de votos e o link para a resposta.

# Parte 2

Fazer um robô no telegram que receba as suas pesquisas e te mostre as respotas
com os links.
'''

# # Stackexchange

TOKEN = '1231789684:AAEW4pZu6J-zFR53FJV2UxUujuSIZjqWbwk'
CHAT_ID = '522574697'


def main():
    while True:
        research = input(
            'Type your research in Stackoverflow: '
            '(Press ctrl+c to exit) ')

        api = context.Stackoverflow()

        data_s = api.search(research)

        msg = 'Looking for research for '.format(research)

        for item in data_s["items"]:

            print(f'Question: {item["title"]}')
            print(f'Score: {item["score"]}')
            print(f'Link: {item["link"]}')
            print('')

        telegram.BotHandler(TOKEN).send_message(
            CHAT_ID,
            msg)


if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:
        sys.exit()
