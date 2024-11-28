import random

def cards(forms, values):
    # Genera un mazo de cartas basado en los tipos (palos) y valores (rango).
    return [(form, value) for value in values for form in forms]

def shuffle(list):
    # Mezcla el mazo en su lugar utilizando la biblioteca random.
    random.shuffle(list)
    return list

def ask_continue():
    # Pregunta al jugador si quiere seguir recibiendo cartas.
    return input("¿Quieres seguir recibiendo cartas? (1 para sí, cualquier otra tecla para no):  \n") == '1'

def choose_ace_value():
    # Pregunta al jugador si un As debe ser valorado como 1 o 11.
    return int(input("¿Quieres que A sea 1 o 11? (escribe 1 o 11): "))

def get_card_value(card):
    # Determina el valor de una carta dada.
    if card[1] == 'A':
        # Si la carta es un As, pregunta por su valor.
        return choose_ace_value()
    return {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
        '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10
    }[card[1]]

def add_card_to_hand(hand, card):
    # Añade una nueva carta a la mano del jugador y actualiza el valor total.
    return (hand[0] + [card], hand[1] + get_card_value(card))

def print_player_hand(player_hand):
    # Imprime la mano actual y su valor total.
    print("Mano del jugador:", player_hand[0])
    print("Valor del jugador:", player_hand[1])

def player_turn(list, player_hand):
    # Maneja el turno del jugador.
    print_player_hand(player_hand) # Muestra la mano actual.

    # Verifica si la mano del jugador es al menos 21 o si elige no continuar.
    return (
        player_hand if player_hand[1] >= 21 or not ask_continue() 
        else player_turn(list[1:], add_card_to_hand(player_hand, list[0])) # Llamada recursiva para sacar una carta.
    )

    

def dealer_turn(list, dealer_hand):
    # Maneja el turno del dealer; el dealer saca cartas hasta que su mano sea al menos 17
    return (
        dealer_hand if dealer_hand[1] >= 17 
        else dealer_turn(list[1:], add_card_to_hand(dealer_hand, list[0]))# Llamada recursiva para sacar una carta.
    )

def match(player_hand, dealer_hand, list):
    #Realiza una ronda completa del juego.
   
    return (
        (lambda final_player_hand: (
            final_player_hand,
            dealer_turn(list [len(final_player_hand[0]):], dealer_hand)  # Turno del dealer.
        ))(player_turn(list , player_hand))  # Turno del jugador.
    )
  
def poker():
    # Crea un mazo completo de cartas.
    return cards(["club", "diamonds", "hearts", "spades"], ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'])

def print_results(player_hand, dealer_hand):
    # Muestra las manos finales y sus valores para el jugador y el dealer.
    print(" \n","Mano del jugador:", player_hand[0])
    print("Valor del jugador:", player_hand[1])
    print("Mano del dealer:", dealer_hand[0])
    print("Valor del dealer:", dealer_hand[1])

def determine_winner(player_hand, dealer_hand):
    # Determina el resultado del juego basado en los valores finales de las manos.
    return (
        "¡El jugador ha perdido! Se pasó de 21." if player_hand[1] > 21 else
        "¡El jugador ha ganado!" if dealer_hand[1] > 21 or player_hand[1] > dealer_hand[1] else
        "¡El dealer ha ganado!" if player_hand[1] < dealer_hand[1] else
        "¡Empate!"
    )

def main():
    # Punto de entrada del programa; ejecuta una ronda del juego e imprime resultados.
    print(
        (lambda results: (print_results(*results), determine_winner(*results)))(  # Llama a print_results y determine_winner en una sola línea.
            match(([], 0), ([], 0), shuffle(poker())  # Llama a match para obtener resultados.
         ))
    )  # Imprime las manos y determina el ganador.
    
if __name__ == "__main__":
    main()  # Ejecuta la función principal para iniciar el juego.


