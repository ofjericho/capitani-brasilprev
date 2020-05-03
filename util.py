import os


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def result_in_screen(keyword, question, score, link):
    print('\n')
    print(
        f'Resultado de sua pesquisa no Stackoverflow para {keyword} : \n ')
    print(question)
    print(score)
    print(link)
