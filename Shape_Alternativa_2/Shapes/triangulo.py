from shapes import shape

class Triangulo(shape):
    def calcular_area(self):
        try:
            a, b, c = [edge.largo for edge in self.edges]
            s= (a + b + c) / 2 
            if s >0:
                return ((s * (s - a) * (s - b) * (s - c)))**0.5 
        except ValueError :
            print("El área no puede ser un número negativo ")

class TrianguloIsosceles(Triangulo):
    def calcular_area(self):
        a, b, c = [edge.largo for edge in self.edges]
        if a == b or b == c or a == c:
            s = (a + b + c) / 2
            return ((s * (s - a) * (s - b) * (s - c)))**0.5
        return ("No es isósceles")


class TrianguloEscaleno(Triangulo):
    def calcular_area(self):
        a, b, c = [edge.largo for edge in self.edges]
        if a != b and b != c and a != c:
            s = (a + b + c) / 2
            return ((s * (s - a) * (s - b) * (s - c)))**0.5

class TrianguloRectangulo(Triangulo):
    def calcular_area(self):
        a, b, c = sorted([edge.largo for edge in self.edges])
        return (a * b) / 2
    
class TrianguloEquilatero(Triangulo):
    def calcular_area(self):
        a = self.edges[0].largo
        return ((3)**1/2 / 4) * (a ** 2)



