from punto import Punto

class Linea: #Linea herda de punto. A punto ya le puse sus excepciones, podemos confiar de la instacia punto  
    def __init__(self, punto_inicial:Punto, punto_final:Punto):
        self.punto_inicial = punto_inicial	
        self.punto_final = punto_final
        self.largo = self.Calcular_largo() 
    def Calcular_largo(self):
        return self.punto_inicial.CalcularDistancia(self.punto_final)
    
