# Proyecto Algoritmo de Newton-Raphson.

### Cada participante debe completar su módulo y luego solicitar el Pull-Request (PR).

A cada participante se le presenta un módulo en lenguaje *Python* con la siguiente estructura:

```python
import math

def derivada(f, h = 0.02):
    """
    Retorna la función derivada de f dado un h.

    Parámetros:
    f: función de variable real f(x).
    h: tamaño del paso.
    """

    def _(x):
        return (f(x + h) - f(x))/h

    return _

def newton_raphson(f, x, ER, N):
    """
    Implementa el Algoritmo de Newton-Raphson y retorna la aproximación de la
    raiz.

    Parámetros:
    f: función de variable real f(x).
    x: aproximación inicial.
    ER: cota mínima del error relativo.
    N: número máximo de iteraciones.
    """

    print("Iteración:", i, "Aproximación:", xi, "Error:", err)

    return xi


if __name__ == "__main__":
    # Pruebe aquí su función.
    pass
```
## Requerimientos.

1. El participante deberá completar en su módulo **solamente** la función `newton_raphson(f, x, ER, N)`, utilizando la función `derivada(f, h = 0.02)` y mostrando por pantalla mediante la instrucción `print()` el **contador de iteración**, la **aproximación** y el **error relativo** de la iteración, mediante `print("Iteración:", i, "aproximación:", xi, "Error:", err)`.
2. La función `newton_raphson(f, x, ER, N)` **deberá retornar** la aproximación de la raíz o cero de la función `f` pasada por parámetro; es decir, deberá retornar el **último valor xi** calculado (`xi`).
3. El participante deberá probar su función `newton_raphson(f, x, ER, N)` en la sección `main` del código, pudiendo implementar funciones adicionales para las pruebas. Las **funciones lambda** pueden ser de utilidad.

## Notas.

**NOTA 1**: Cualquier duda o pregunta sobre este proyecto, por favor abra un [**issue**](https://github.com/ejdecena/proyecto_newton_raphson/issues).

**NOTA 2**: Solo se recibirá UNA y solo una petición de PR por participante.

**NOTA 3**: Marque con **Watch** este repositorio para que reciba todas las notificaciones.

**NOTA 4**: Recuerde que hay un [**Tutorial Git**](https://github.com/ejdecena/tutorial_git) y un [**Tutorial Python**](https://github.com/ejdecena/tutorial_python) que pueden ser útiles en caso de cualquier duda.

**NOTA 5**: Se recibirán solicitudes de PR hasta el día **miércoles 06 de noviembre de 2019, 11:59 pm**, SIN PRÓRROGA.