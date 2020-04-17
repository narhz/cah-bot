import json
from random import randint, shuffle
import pickle
import os


def getCards(color=None, count=None):
    """
    Return one black card, or given count of white cards.
    """

    with open('cards.json', 'r') as cards_file:
        cards = json.load(cards_file)['cards']

    if color == 'black':
        return cards['black'][randint(0, len(cards['black']) - 1)]

    elif color == 'white':
        white_cards = []
        for i in range(count):
            white_cards.append(cards['white'][randint(0, len(cards['white']) - 1)])

        return white_cards


def fillBlanks(w_cards, b_card):
    """
    Replace blanks in black card with white card text.
    Remove trailing periods from white cards.
    """
    b_card = b_card.replace('_', w_cards.replace('.', ''), 1)

    return b_card


def playCards():
    black_card = getCards(color="black")
    white_cards = getCards(color='white', count=black_card['pick'])
    b_text = black_card['text']


    if '_' in b_text:
        for card in white_cards:
            b_text = fillBlanks(card['text'], b_text)
        return b_text
    else:
        for card in white_cards:
            b_text += ' ' + card['text']
        return b_text


if __name__ == "__main__":
    print(playCards())
