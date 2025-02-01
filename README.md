# Reto-6-Manejo-de-excepciones
### Reto 6

-El objetivo de este reto es reforzar el manejo de excepciones. Para ello, se tomará un código previamente creado y se agregarán diferentes excepciones con el fin de anticipar y gestionar correctamente los posibles errores que puedan surgir.

###Characters
----
<p>La mayoría de las excepciones introducidas en el código corresponden a <code>ValueError</code>. En la clase <code>Punto</code>, se valida que los datos ingresados sean números. En <code>Línea</code>, se verifica que sus atributos sean instancias de <code>Punto</code> correctamente definidos. Para <code>Triángulo</code>, <code>Rectángulo</code> y <code>Cuadrado</code>, se comprueba que las áreas y perímetros no sean negativos ni iguales a cero. Además, dado que <code>Línea</code> hereda de <code>Punto</code>, y el resto de las figuras heredan de <code>Shape</code>, que a su vez deriva de <code>Línea</code> y <code>Punto</code>, el manejo de excepciones se propaga a todas las clases.</p>


``` mermaid
classDiagram
    class Punto {
        +x: float
        +y: float
    }
    
    class Línea {
        +punto1: Punto
        +punto2: Punto
        +largo(): float
    }
    
    class Shape {
        +vertices: list<Punto>
        +edges: list<Línea>
        +angulos_internos: list<float>
        +calcular_area()
        +calcular_perimetro()
        +calcular_angulos_internos()
    }

    class Triángulo {
        +calcular_area()
    }

    class TriánguloIsósceles {
        +calcular_area()
    }

    class TriánguloEscaleno {
        +calcular_area()
    }

    class TriánguloRectángulo {
        +calcular_area()
    }

    class TriánguloEquilátero {
        +calcular_area()
    }

    class Rectángulo {
        +calcular_area()
    }

    class Cuadrado {
        +calcular_area()
        +calcular_perimetro()
    }

    Línea *-- Punto : tiene
    Shape *-- Línea : compuesto por
    Shape *-- Punto : compuesto por
    Shape <|-- Triángulo:es un
    Shape <|-- Rectángulo: es un
    Rectángulo <|-- Cuadrado: es un
    Triángulo <|-- TriánguloIsósceles: es un
    Triángulo <|-- TriánguloEscaleno: es un
    Triángulo <|-- TriánguloRectángulo: es un
    Triángulo <|-- TriánguloEquilátero: es un
````
