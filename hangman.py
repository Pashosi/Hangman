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
        game(word)
    else:
        print('Ну ладно')


def basket_miss_latter(letters_list: list, letter):
    if letter not in letters_list:
        letters_list.append(letter)
        return True
    else:
        return False


def game(word: str):
    count = -1
    miss_letters_list = []
    # print(HANGMAN[count])
    print('*' * len(word))
    for letter_input in sys.stdin:
        letter_input = letter_input.strip()
        if bool(re.search(r'[а-яА-Я]', letter_input)):
            if letter_input in word:
                word = ''.join([letter.upper() if (letter_input == letter) else letter for letter in word])
                print(''.join(['*' if i.islower() else i for i in word]))
                if all(i.isupper() for i in word):
                    print('Вы победили')
                    greeting()
            elif letter_input.upper() in word:
                print('Такую букву уже вводили')
            elif len(letter_input) > 1:
                print('Писать по одной букве')
            else:
                try:
                    count += 1
                    if basket_miss_latter(miss_letters_list, letter_input):
                        print(HANGMAN[count])
                    print(''.join(['*' if i.islower() else i for i in word]))
                except IndexError:
                    print('Вы проиграли')
                    greeting()
        else:
            print('Не правильный символ')


if __name__ == '__main__':
    greeting()
