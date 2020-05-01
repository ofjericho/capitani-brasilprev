# -*- coding: UTF8 -*-
import sys
import os
from search import context
from bot import telegram


TOKEN = '1231789684:AAEW4pZu6J-zFR53FJV2UxUujuSIZjqWbwk'
CHAT_ID = '522574697'


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def result_in_screen(keyword, question, score, link):
    print(f'Resultado de sua pesquisa no Stackoverflow para {keyword} : \n ')
    print(question)
    print(score)
    print(link)


def main():

    clear()

    while True:
        keyword = input(
            '\n O que deseja pesquisar no Stackoverflow ? '
            '( Crtl+c para sair ): ')

        data_s = context.Stackoverflow().search(keyword)

        for item in data_s["items"]:

            question = 'Pergunta: {} \n \n'.format(item["title"])
            score = 'Votos: {} \n'.format(item["score"])
            link = 'Resposta: {}\n'.format(item["link"])

            research = 'Resultado de sua pesquisa no Stackoverflow para <b> {} </b> : \
                        \n \n'.format(keyword)

            research += question
            research += score
            research += link

            telegram.BotHandler(TOKEN).send_message(
                CHAT_ID,
                research)

            research = ''

            result_in_screen(keyword, question, score, link)


if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:
        sys.exit()
