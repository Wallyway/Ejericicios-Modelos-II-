## Estructura e implementacion de Factory Method

El patrón Factory Method es un patrón de diseño creacional que proporciona una interfaz para crear objetos en una superclase, pero permite a las subclases alterar el tipo de objetos que se crearán.

## 1. Patron Factory Method

The workspace contains two folders by default, where:

- En este código, el método `create_instrument()` en la clase  `InstrumentCreator()`actúa como el Factory Method. Permite crear instancias de objetos de tipo Instrument (ya sea un Guitarra o un violín) sin especificar su clase concreta directamente en el código cliente.

## 2. Características del Factory Method

- `Interfaz comun`: El Factory Method declara una interfaz común para crear objetos. En este caso, la interfaz es el método `create_instrument()` en `InstrumentCreator`.

- `Subclases concretas`: Las subclases (Guitar, Piano, Violin, etc) implementan el Factory Method para crear objetos concretos.

-  `Decision en timepo de ejecucion`: La decisión sobre qué objeto crear se toma en tiempo de ejecución, según la probabilidad aleatoria en este caso.

## 3. Estructura del codigo

- `InstrumentCreator`: La clase creadora abstracta que declara el Factory Method `create_instrument()`.

- `Guitar`, `Violin`, etc:  Las clases concretas que implementan el Factory Method y crean instancias de instrumentos.

- `Musician`: Utiliza el Factory Method para crear músicos con instrumentos aleatorios.

- `Instrument`: Define la estructura básica que todos los instrumentos deben seguir.Proporciona un método abstracto `play()` que debe ser implementado por las subclases.
No se puede instanciar directamente; solo se utiliza como base para otros instrumentos específicos.
