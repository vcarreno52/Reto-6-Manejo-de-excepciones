from shapes import shape    

class Rectangulo(shape):
    def calcular_area(self): 
        a, b = [self.edges[0].largo, self.edges[1].largo]
        if a*b <=0:
            raise ValueError("El área ebe ser un número mayor que 0")       
        return a * b


class Cuadrado(Rectangulo):
    def calcular_area(self):
        lado = self.edges[0].largo
        if lado**2 <=0:
            raise ValueError("El área debe ser un número mayor que 0")
        return lado ** 2

    def calcular_perimetro(self):
        lado = self.edges[0].largo
        if 4*lado <=0:
            raise ValueError("El perímetro debe ser mayor que 0")
        return 4 * lado