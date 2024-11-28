# Family Relationships Prolog Program

Este programa en Prolog define un conjunto de relaciones familiares y reglas que se pueden utilizar para consultar diversos aspectos de la dinámica familiar, como identificar padres, hermanos, abuelos, tíos, tías, y más. También incluye información de género de los individuos, así como relaciones como el matrimonio (pareja) y la felicidad.

## Características

- **Datos de Relaciones Familiares**: Se especifican las relaciones entre diversos individuos, como padres e hijos, utilizando hechos.
- **Información de Género**: Se declara el género de cada individuo para apoyar reglas más específicas sobre las relaciones (por ejemplo, padre, madre).
- **Reglas**: Se proporcionan diversas reglas de relaciones familiares, como `fatherof`, `motherof`, `siblingof`, y `uncleof`, entre otras.
- **Predicados Adicionales**: Se incluyen predicados adicionales como `happy/1`, `partner/2`, y `all_parents/2`, que permiten hacer consultas más complejas sobre la estructura familiar.

## Datos Familiares

### Padres
- David y Sofía son los padres de Alexander, Brayan, Carolina, Diego, Emilia y Fernanda.
- Alexander y María son los padres de Gabriel y Hugo.
- Carolina y Juan son los padres de Isabella y Juliana.

### Géneros
- **Hombres**: David, Alexander, Brayan, Diego, Gabriel, Hugo, Juan.
- **Mujeres**: Sofía, Carolina, Emilia, Fernanda, María, Isabella, Juliana.

## Reglas

### Relaciones Familiares
- **childof(A, B)**: Define la relación `childof`, que es la inversa de la relación `parentof`.
- **fatherof(A, B)**: Define la relación `fatherof`, donde `A` es el padre de `B` (solo para hombres).
- **motherof(A, B)**: Define la relación `motherof`, donde `A` es la madre de `B` (solo para mujeres).
- **grandparentof(A, B)**: Define la relación `grandparentof`, donde `A` es abuelo o abuela de `B` a través de su hijo `C`.
- **siblingof(A, B)**: Define la relación `siblingof`, donde `A` y `B` comparten al menos un padre.
- **uncleof(A, B)**: Define la relación `uncleof`, donde `A` es el hermano masculino de uno de los padres de `B`.
- **auntof(A, B)**: Define la relación `auntof`, donde `A` es la hermana femenina de uno de los padres de `B`.
- **father_in_law(A, B)**: Define la relación `father_in_law`, donde `A` es el padre de la pareja de `B`.
- **brotherof(A, B)**: Define la relación `brotherof`, donde `A` y `B` son hermanos y `A` es hombre.
- **brother_in_lawof(A, B)**: Define la relación `brother_in_lawof`, donde `A` es el hermano de uno de los cónyuges de `B`.
- **cousinof(A, B)**: Define la relación `cousinof`, donde `A` y `B` son primos (comparten al menos un abuelo pero no son hermanos).

### Predicados Adicionales
- **partner(A, B)**: Define la relación donde `A` y `B` son pareja (es decir, tienen al menos un hijo en común).
- **happy(X)**: Define la relación donde `X` es feliz, basada en tener una pareja.
- **all_parents(R, M)**: Encuentra todos los padres de una persona `R` y los devuelve en una lista `M`.

## Consultas de Ejemplo

A continuación, algunos ejemplos de consultas que puedes realizar basadas en los datos y reglas proporcionados:

1. **¿Quiénes son los hijos de David?**
   ```prolog
   ?- all_parents('david', Children).
