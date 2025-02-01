from punto import Punto
from Linea import Linea
from Shapes.shapes import shape
#from Shapes.Rectángulo import Rectangulo, Cuadrado  
#from Shapes.triangulo import *
#No son necesarios para esta prueba



A= Punto(1, 1)
B= Punto(1, 2)  
M= (A.CalcularDistancia(B)) # 1.0
print (M)

A = Punto(1, 1)     
B = Punto(2, 2)

M= (A.CalcularDistancia(B)) # 1.4142135623730951
print(M)

l= Linea(A,B)
print(l.largo) # 1.4142135623730951

p= [Punto(0,0), Punto(0,1), Punto(1,1), Punto(1,0)]
l = [Linea(p[0], p[1]), Linea(p[1], p[2]), Linea(p[2], p[3]), Linea(p[3], p[0])]
a = [90, 90, 90, 90]

s = shape(p, l, a)
print(s.calcular_perimetro())
print(s.es_poligono_regular)
print(s.calcular_angulos_internos())

