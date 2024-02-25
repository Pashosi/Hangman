import sys
from random import choice
import re

HANGMAN = (
    """
     ------
     |    |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |    |
     | 
     |   
     |    
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   
     |   
     |     
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |   
     |    
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |   
     |   
    ----------
    """
)


def get_words():
    with open(r'C:\Hangman\nouns.txt', 'r', encoding='utf-8') as word:
        return choice(word.readlines()).strip('\n')


def greeting():  # приветствие
    print('Начинаем игру?: y-Да, n-Нет ')
    n = input()
    if n in ['y', 'да', 'го', 'yes', 'д']:
        word = get_words()
        input_letter(word)

    else:
        print('Ну ладно')


def input_letter(word: str):
    count = 0
    print(HANGMAN[count])
    print('*' * len(word))
    for i in sys.stdin:
        if bool(re.search(r'[а-яА-Я]', i.strip())):
            if i.strip('\n') in word:
                word = ''.join([letter.upper() if (i.strip('\n') == letter) else letter for letter in word])
                print(''.join(['*' if i.islower() else i for i in word]))
                if all(i.isupper() for i in word):
                    print('Вы победили')
                    greeting()
            elif i.strip('\n').upper() in word:
                print('Такую букву уже вводили')
            else:
                try:
                    count += 1
                    print(HANGMAN[count])
                    print(''.join(['*' if i.islower() else i for i in word]))
                except IndexError:
                    print('Вы проиграли')
                    greeting()
        else:
            print('Не правильный символ')



greeting()
