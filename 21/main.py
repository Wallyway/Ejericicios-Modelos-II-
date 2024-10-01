import random

def cards(forms, values):
    return [[form, value] for value in values for form in forms]

def shuff(list):
    random.shuffle(list)
    return list

def opt():
    return bool(input())

def game(cards, result: int, vals):
    print(result)
    if opt() == True and result < 21:
        return cards[:1] + game(cards[1:], result+vals[cards[:1][0][1]], vals)
    return [result]

def vals():
    return {'A': 1,'2': 2, '3': 3, '4':4, '5':5, '6':6, '7':7, '8':9, '9':9, '10':10, 'J':10, 'Q':10, 'K': 10}
    
def pocker():
    return cards(["club", "diamonds", "hearts", "spades"], ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'])

#print(opt())    
print(game(shuff(pocker()),0,()))