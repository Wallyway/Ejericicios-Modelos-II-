# Simulación del Juego de 21 (Blackjack)

Esta es una simulación básica del juego de 21 (Blackjack) implementada en Python. El programa permite a un jugador jugar contra un dealer, siguiendo las reglas estándar del Blackjack.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Lógica del Juego](#logica-del-juego)
- [Interacción con el Usuario](#interacción-con-el-usuario)
- [Flujo de Ejecucion](#flujo-de-ejecución)
- [Instrucciones](#instrucciones)


## Descripción

El objetivo del juego es alcanzar un valor total de 21 o lo más cercano posible sin pasarse. El jugador compite contra un dealer que también juega bajo ciertas reglas predefinidas.

### Cartas

- Las cartas se representan como tuplas `(form, value)`, donde:
  - `form` es el palo (corazones, tréboles, etc.).
  - `value` es el valor (A, 2, 3, ..., K).
- El mazo de cartas se crea utilizando una comprensión de listas que combina todos los palos con todos los valores.

### Manos

- Tanto el jugador como el dealer tienen manos representadas como tuplas que consisten en:
  - Una lista de cartas que tienen en la mano.
  - Un entero que representa el valor total de las cartas en la mano.

## Lógica del Juego

### Mazo de Cartas

- El mazo se crea en la función `poker()` y se mezcla usando `shuffle()`. La mezcla garantiza que las cartas se distribuyan de manera aleatoria en cada partida.

### Valores de las Cartas

- Los valores de las cartas se manejan de forma específica, ya que el As puede tener un valor de 1 o 11, dependiendo de la elección del jugador. Este aspecto es crucial, ya que influye en la estrategia del jugador.
- Los valores de las cartas de la 2 a la 10 son numéricos, mientras que las figuras (J, Q, K) tienen un valor de 10.

### Turnos

- La función `player_turn()` gestiona el turno del jugador:
  - Muestra la mano actual y pregunta si el jugador quiere seguir.
  - Si el jugador decide continuar, se agrega una carta a su mano y se vuelve a evaluar.
- La función `dealer_turn()` gestiona el turno del dealer, que sigue sacando cartas automáticamente hasta alcanzar al menos 17. Este es un aspecto clave en las reglas del Blackjack.

## Interacción con el Usuario

### Entradas

- El programa solicita entradas del usuario a través de `input()`, permitiendo decisiones en tiempo real. Esto incluye si el jugador quiere seguir pidiendo cartas y el valor que desea asignar a un As.

### Mensajes

- Se proporcionan mensajes claros para que el jugador sepa cuál es su mano actual y cómo va el juego. Esto mejora la experiencia del usuario y hace que el juego sea más accesible.

## Flujo de Ejecución

### Inicio del Juego

- Al ejecutar el programa, se invoca `main()`, que es el punto de entrada. Esta función organiza el flujo del juego.

### Mezcla y Distribución de Cartas

- Se crea el mazo de cartas, se mezcla y luego se pasa a la función `match()`.

### Ronda del Juego

- La función `match()` controla el flujo del juego:
  - Primero, se llama a `player_turn()` para gestionar el turno del jugador.
  - Luego, se llama a `dealer_turn()` para gestionar el turno del dealer.
- Ambos turnos están estructurados recursivamente, lo que permite que el juego siga hasta que se cumplan ciertas condiciones (21 o más para el jugador, 17 o más para el dealer).


## Instrucciones

Para ejecutar el juego, asegúrate de tener Python instalado en tu sistema. Luego, sigue estos pasos:

1. Clona este repositorio:
   ```bash
   git clone https://github.com/Wallyway/Ejericicios-Modelos-II-.git
   cd <NOMBRE_DEL_DIRECTORIO>
