import random

def cards(forms, values):
    return [(form, value) for value in values for form in forms]

def shuff(list):
    random.shuffle(list)
    return list

def opt(previous):
    print("Digite 1 para continuar o 0 para parar: ")
    if input() == '1':
        return True == previous
    return False

def rand(probabilty, previous):
    if random.random() > probabilty:
        return False 
    return True == previous

def play(player, card, fn):
    if player[2]:
        return (player[0]+card, player[1]+vals(card[0][1], player[1]), fn)
    return player

def vals(key, score):
    if score < 11:
        return {'A': 11,'2': 2, '3': 3, '4':4, '5':5, '6':6, '7':7, '8':9, '9':9, '10':10, 'J':10, 'Q':10, 'K': 10}[key]
    return {'A': 1,'2': 2, '3': 3, '4':4, '5':5, '6':6, '7':7, '8':9, '9':9, '10':10, 'J':10, 'Q':10, 'K': 10}[key]
  
def pocker():
    return cards(["club", "diamonds", "hearts", "spades"], ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'])

# Player and house are tuples
# Retorno [player, dealer]
# Player es la tupla ([cards] : list, value : int, want's to play : bool)

def result(res):
    print("\n")
    print("Tu puntaje:", res[0][1], ", tu mano:", res[0][0])
    print("Puntaje del dealer:", res[1][1], ", mano del dealer:",res[1][0])

def match(player, dealer, cards):
    print("Tu mano:", player[0], "Tu puntaje:", player[1])
    if player[1] < 21 and dealer[1] < 21 and (dealer[2] or player[2]): 
        return match(play(player, cards[:1], opt(player[2])), play(dealer, cards[1:2], rand(0.7, dealer[2])), cards[2:])
    return [player, dealer]

result(match(([], 0, True), ([], 0, True), shuff(pocker())))

