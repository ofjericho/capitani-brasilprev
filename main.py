# -*- coding: UTF8 -*-
import sys
import os
from search import context
from bot import chatbot


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def result_in_screen(keyword, question, score, link):
    print('\n')
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

            question = 'Pergunta: {}'.format(item["title"])
            score = 'Votos: {}'.format(item["score"])
            link = 'Resposta: {}'.format(item["link"])

            research = 'Resultado de sua pesquisa no Stackoverflow para <b> {} </b> : \
                        \n\n'.format(keyword)

            research += question + '\n\n'
            research += score + '\n'
            research += link + '\n'

            # Send a message to Telegram

            bot = chatbot.Telegram()
            bot.send_message(research)

            research = ''

            # Print a research on screen

            result_in_screen(keyword, question, score, link)


if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:
        sys.exit()
