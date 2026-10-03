class Calculos:

    def __init__(self):

        # Temperatura inicial de la cabina
        self.temperatura = 25.0

        # Límites
        self.temperatura_minima = 25.0
        self.temperatura_maxima = 120.0

        # Incremento de temperatura
        self.incremento_temperatura = 1.5

   
    # TEMPERATURA
   

    def aumentar_temperatura(self):

        if self.temperatura < self.temperatura_maxima:

            self.temperatura += self.incremento_temperatura

            if self.temperatura > self.temperatura_maxima:
                self.temperatura = self.temperatura_maxima

    
    # DISMINUIR TEMPERATURA
   

    def disminuir_temperatura(self):

        if self.temperatura > self.temperatura_minima:

            self.temperatura -= self.incremento_temperatura

            if self.temperatura < self.temperatura_minima:
                self.temperatura = self.temperatura_minima

    
    # OBTENER TEMPERATURA
   
    def obtener_temperatura(self):

        return self.temperatura

    
    # REINICIAR TEMPERATURA
  

    def reiniciar(self):

        self.temperatura = self.temperatura_minima

    
    # VELOCIDAD


    def calcular_desplazamiento(self, velocidad):

        return velocidad * 0.03

    
    # ESTADO DE SECADO
    
    def temperatura_adecuada(self):

        return self.temperatura >= 80.0