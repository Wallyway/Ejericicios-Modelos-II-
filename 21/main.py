import random

def cards(forms, values):
    return [(form, value) for value in values for form in forms]

def shuff(list):
    random.shuffle(list)
    return list

def opt():
    if input() == '1':
        return True
    else:
        return False

def game(cards, result: int, vals):
    print(result)
    if opt() == True and result < 21:
        return cards[:1] + game(cards[1:], result+vals[cards[:1][0][1]], vals)
    return [result]

def vals(key):
    return {'A': 1,'2': 2, '3': 3, '4':4, '5':5, '6':6, '7':7, '8':9, '9':9, '10':10, 'J':10, 'Q':10, 'K': 10}[key]
    
def pocker():
    return cards(["club", "diamonds", "hearts", "spades"], ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'])

# Player and house are tuples
# Retorno [player, dealer]
# Player es la tupla ([cards], value)
# TODO: hacer que el usuario decida si continuar, hacer que el dealer pare aleatoriamente. El que tenga el mayor puntaje (value) menor o igual a 21 es el que gana
def match(player, dealer, cards):
    if player[1] < 21 and dealer[1] < 21:
        return match((player[0]+cards[:1], player[1]+vals(cards[0][1])), (dealer[0]+cards[1:2], dealer[1]+vals(cards[1][1])), cards[2:])
    return [player, dealer]

print(match(([], 0), ([], 0), shuff(pocker())))

