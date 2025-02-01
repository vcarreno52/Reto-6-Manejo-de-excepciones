class Punto:
    def __init__(self, x:float, y:float):
        try:
            self.x = float(x)
            self.y = float(y)
        except ValueError:
            print ("Debes ingresar números")
        except Exception as e:
            print ("Esrror inesperado,"+ e)
        finally:
            print ("sirvió")
        
        
    def CalcularDistancia(self, punto):
        if not isinstance(Punto, Punto): #Si arriba hay un error y sigue corriendo, toca capturar el "mismo" error en el método
            print("los puntos no han sido creados correctamente, intentalo otra vez")
            return(0.0)
        return ((self.x - punto.x)**2 + (self.y - punto.y)**2)**0.5

P1=Punto("a","s")
P2=Punto(2,3)
c1=P1.CalcularDistancia(P1)
print(c1)