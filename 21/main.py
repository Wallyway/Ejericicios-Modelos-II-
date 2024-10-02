import random

def cards(forms, values):
    return [(form, value) for value in values for form in forms]

def shuffle(list):
    random.shuffle(list)
    return list

def ask_continue():
    return input("¿Quieres seguir recibiendo cartas? (1 para sí, cualquier otra tecla para no):  \n") == '1'

def choose_ace_value():
    return int(input("¿Quieres que A sea 1 o 11? (escribe 1 o 11): "))

def get_card_value(card):
    if card[1] == 'A':
        return choose_ace_value()
    return {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
        '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10
    }[card[1]]

def add_card_to_hand(hand, card):
    return (hand[0] + [card], hand[1] + get_card_value(card))

def print_player_hand(player_hand):
    print("Mano del jugador:", player_hand[0])
    print("Valor del jugador:", player_hand[1])

def player_turn(list, player_hand):
    print_player_hand(player_hand)
    return (
        player_hand if player_hand[1] >= 21 or not ask_continue() 
        else player_turn(list[1:], add_card_to_hand(player_hand, list[0]))
    )

def dealer_turn(list, dealer_hand):
    return (
        dealer_hand if dealer_hand[1] >= 17 
        else dealer_turn(list[1:], add_card_to_hand(dealer_hand, list[0]))
    )

def match(player_hand, dealer_hand, list):
    final_player_hand = player_turn(list, player_hand)
    return (
        final_player_hand,
        dealer_turn(list[len(final_player_hand[0]):], dealer_hand)
    )

def poker():
    return cards(["club", "diamonds", "hearts", "spades"], ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'])

def print_results(player_hand, dealer_hand):
    print(" \n","Mano del jugador:", player_hand[0])
    print("Valor del jugador:", player_hand[1])
    print("Mano del dealer:", dealer_hand[0])
    print("Valor del dealer:", dealer_hand[1])

def determine_winner(player_hand, dealer_hand):
    return (
        "¡El jugador ha perdido! Se pasó de 21." if player_hand[1] > 21 else
        "¡El jugador ha ganado!" if dealer_hand[1] > 21 or player_hand[1] > dealer_hand[1] else
        "¡El dealer ha ganado!" if player_hand[1] < dealer_hand[1] else
        "¡Empate!"
    )

def main():
    results = match(([], 0), ([], 0), shuffle(poker()))
    print_results(*results)
    print(determine_winner(*results))

if __name__ == "__main__":
    main()
