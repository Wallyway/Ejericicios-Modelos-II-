## Funcionamiento

### 1. Cargar el archivo Prolog

El archivo `nomina.pl` contiene las reglas de Prolog necesarias para calcular el salario neto de un docente en función de su categoría. El código de Prolog también define los hechos básicos sobre los docentes y sus categorías. 

Las categorías posibles de los docentes son:

- **Auxiliar**: Salario base de 3,000,000.
- **Asociado**: Salario base de 5,000,000.
- **Titular**: Salario base de 7,000,000.

El salario neto se calcula en Prolog tomando en cuenta las deducciones y las bonificaciones que varían según la categoría.

### 2. API RESTful con FastAPI

La API proporciona dos endpoints:

- **POST /agregar_docente/**: Permite agregar un nuevo docente con su nombre y categoría.
- **POST /calculo_nomina/**: Permite calcular el salario neto de un docente dado su nombre.

#### 2.1 Endpoint: `/agregar_docente/`

Este endpoint permite agregar un nuevo docente a la base de datos con su nombre y categoría.

- **Método**: `POST`
- **Cuerpo de la solicitud** (en formato JSON):
  
  ```json
  {
    "nombre": "juan_perez",
    "categoria": "auxiliar"
  }


### 2.2 Endpoint: `/calculo_nomina/`

Este endpoint permite obtener el salario neto de un docente dado su nombre. El salario neto es calculado a partir de su categoría, tomando en cuenta las deducciones por salud y pensión, y las bonificaciones asociadas a cada categoría.

- **Método**: `POST`
- **Cuerpo de la solicitud** (en formato JSON):

  ```json
  {
    "nombre": "juan_perez"
  }


### 3. Cálculo del Salario Neto en Prolog

El cálculo del salario neto se realiza de acuerdo a las siguientes reglas:

#### Deducciones:
- **Deducción por salud**: 4% del salario base.
- **Deducción por pensión**: 4% del salario base.

#### Bonificaciones por categoría:
- **Auxiliar**: 5% del salario base.
- **Asociado**: 10% del salario base.
- **Titular**: 15% del salario base.

#### Fórmula para el salario neto:
El salario neto se calcula con la siguiente fórmula:

```Salario Neto = Salario Base - Deducción Salud - Deducción Pensión + Bonificación``

La bonificación depende de la categoría del docente:

- **Auxiliar**: Se calcula el 5% del salario base.
- **Asociado**: Se calcula el 10% del salario base.
- **Titular**: Se calcula el 15% del salario base.

El sistema también realiza las deducciones correspondientes:
- **Deducción por salud**: 4% del salario base.
- **Deducción por pensión**: 4% del salario base.

Finalmente, el salario neto se obtiene restando las deducciones y sumando la bonificación:

```Salario Neto = Salario Base - (Salario Base * 0.04) - (Salario Base * 0.04) + Bonificación```


Por ejemplo, para un docente de categoría **auxiliar** con un salario base de 3,000,000:

- **Deducción por salud**: 3,000,000 * 0.04 = 120,000
- **Deducción por pensión**: 3,000,000 * 0.04 = 120,000
- **Bonificación**: 3,000,000 * 0.05 = 150,000

El cálculo del salario neto sería:

```Salario Neto = 3,000,000 - 120,000 - 120,000 + 150,000 = 2,910,000```
