from punto import Punto 
from Linea import Linea 

class shape:
    def __init__(self, vertices: list[Punto], edges: list[Linea], angulos_internos: list[float]):
        try:
            self.vertices = vertices
            self.edges = edges
            self.angulos_internos = angulos_internos
            self.es_poligono_regular = self._verificar_poligono_regular()
            if len(edges)<= 2:
                raise ValueError("Una figura debe tener almenos tres líneas para ser creada")
            if any(angulos_internos==0 for i in angulos_internos):
                raise ValueError ("El ángulo inteno debe ser diferente de 0")
        except ValueError as vs:
            print("Hubo un error inceperado en shape")

    def _verificar_poligono_regular(self):    
        lados = [edge.largo for edge in self.edges]
        angulos = self.angulos_internos
        return all(lado == lados[0] for lado in lados) and all(angulo == angulos[0] for angulo in angulos)

    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        return sum(edge.largo for edge in self.edges)

    def calcular_angulos_internos(self):
        return self.angulos_internos