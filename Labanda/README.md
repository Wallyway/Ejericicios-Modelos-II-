## Estructura e implementacion de Factory Method

El patrón Factory Method es un patrón de diseño creacional que proporciona una interfaz para crear objetos en una superclase, pero permite a las subclases alterar el tipo de objetos que se crearán.

## 1. Patron Factory Method

- En este código, el método `random()` en la clase  `InstrumentFactory()`actúa como el Factory Method. Permite crear instancias de objetos de tipo Instrument aleatoriamente (ya sea un Guitarra o un violín).

## 2. Características del Factory Method

- `Interfaz comun`: El Factory Method declara una interfaz común para crear objetos. En este caso, la interfaz es el método `random()` en `InstrumentFactory`.

- `Subclases concretas`: Las subclases (clases hijas) (Guitar, Piano, Violin, etc) heredan el Factory Method para crear objetos concretos.

## 3. Estructura del codigo

- `InstrumentFactory`: La clase creadora abstracta que declara el Factory Method `random()`.

- `Guitar`, `Violin`, etc:  Las clases concretas que heredan el Factory Method y crean instancias de instrumentos.

- `Musician`: Utiliza el Factory Method y define los metodos para afinar y tocar.

- `Instrument`: Define la estructura básica que todos los instrumentos deben seguir.Proporciona un método abstracto `play()` que debe ser implementado por las subclases.
No se puede instanciar directamente; solo se utiliza como base para otros instrumentos específicos los cuales, gracias a  `super() `aseguramos que cualquier inicialización o configuración necesaria en la clase padre también se realice al crear una instancia de la subclase.
