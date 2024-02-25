import sys
from random import choice

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
    if n in ['y', 'да', 'го', 'yes']:
        word = get_words()
        print('*' * len(word))
        input_letter(word)
    else:
        print('Ну ладно')


def input_letter(word: str):
    # print(word)
    count = 0
    for i in sys.stdin:
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
                print(HANGMAN[count])
                count += 1
            except IndexError:
                print('Вы проиграли')
                greeting()


greeting()
