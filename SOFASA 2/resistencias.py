import math


class Resistencias:

    def __init__(self, cabina):

        self.cabina = cabina

        # Estado del sistema
        self.sistema_encendido = False

    # ENCENDER / APAGAR
    

    def encender(self):
        self.sistema_encendido = True

    def apagar(self):
        self.sistema_encendido = False

    
    # COLOR DE LAS RESISTENCIAS

    def obtener_color(self):

        if self.sistema_encendido:
            return "#ff0000"

        return "#ff802b"

    
    # RESISTENCIA LATERAL
    

    def resistencia_lateral(self, z, y):

        puntos = []

        inicio_x = -6.2
        final_x = 6.2

        cantidad_puntos = 100

        amplitud = 0.22

        for i in range(cantidad_puntos):

            proporcion = i / (cantidad_puntos - 1)

            x = inicio_x + (
                final_x - inicio_x
            ) * proporcion

            onda = math.sin(
                proporcion * math.pi * 14
            )

            resistencia_y = y + (
                amplitud * onda
            )

            puntos.append(
                (x, resistencia_y, z)
            )

        # Dibujar todos los segmentos
        for i in range(len(puntos) - 1):

            p1 = puntos[i]
            p2 = puntos[i + 1]

            self.cabina.linea_3d(
                p1[0],
                p1[1],
                p1[2],
                p2[0],
                p2[1],
                p2[2],
                self.obtener_color(),
                6 if self.sistema_encendido else 5
            )

    
    # RESISTENCIA SUPERIOR

    def resistencia_superior(self, z):

        puntos = []

        inicio_x = -6.2
        final_x = 6.2

        cantidad_puntos = 100

        amplitud = 0.20

        altura_base = 4.55

        for i in range(cantidad_puntos):

            proporcion = i / (cantidad_puntos - 1)

            x = inicio_x + (
                final_x - inicio_x
            ) * proporcion

            onda = math.sin(
                proporcion * math.pi * 14
            )

            y = altura_base + (
                amplitud * onda
            )

            puntos.append(
                (x, y, z)
            )

        # Dibujar segmentos
        for i in range(len(puntos) - 1):

            p1 = puntos[i]
            p2 = puntos[i + 1]

            self.cabina.linea_3d(
                p1[0],
                p1[1],
                p1[2],
                p2[0],
                p2[1],
                p2[2],
                self.obtener_color(),
                6 if self.sistema_encendido else 5
            )

    # DIBUJAR LAS 6 RESISTENCIAS
    

    def dibujar(self):

        
        # LADO IZQUIERDO
        

        # Resistencia 1
        self.resistencia_lateral(
            -3.65,
            2.2
        )

        # Resistencia 2
        self.resistencia_lateral(
            -3.65,
            0.8
        )

        
        # LADO DERECHO
        

        # Resistencia 3
        self.resistencia_lateral(
            3.65,
            2.2
        )

        # Resistencia 4
        self.resistencia_lateral(
            3.65,
            0.8
        )

        # PARTE SUPERIOR
        

        # Resistencia 5
        self.resistencia_superior(
            -1.4
        )

        # Resistencia 6
        self.resistencia_superior(
            1.4
        )