# -*- coding: UTF8 -*-
import sys
import os
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


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def main():

    clear()

    while True:
        keyword = input(
            'Digite o que deseja pesquisar no Stackoverflow '
            '(ctrl+c para sair): ')

        data_s = context.Stackoverflow().search(keyword)

        for item in data_s["items"]:

            question = 'Pergunta: {} \n'.format(item["title"])
            score = 'Votos: {} \n'.format(item["score"])
            link = 'Resposta: {}\n'.format(item["link"])

            research = 'Sua pesquisa no Stackoverflow para {} \n'\
                .format(keyword)

            print(research)
            print(question)
            print(score)
            print(link)
            print('')

            research += question
            research += score
            research += link

            telegram.BotHandler(TOKEN).send_message(
                CHAT_ID,
                research)

            research = ''


if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:
        sys.exit()
