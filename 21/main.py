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

    
def pocker():
    return cards(["club", "diamonds", "hearts", "spades"], ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'])

def match(player, dealer, cards):
    if player[1] < 21 and dealer[1] < 21:
        return match((player[0]+cards[:1], player[1]+vals(cards[0][1])), (dealer[0]+cards[1:2], dealer[1]+vals(cards[1][1])), cards[2:])
    return [player, dealer]

print(match(([], 0), ([], 0), shuff(pocker())))

