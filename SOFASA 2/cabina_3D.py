import math


class Cabina3D:

    def __init__(self, canvas):
        self.canvas = canvas

        # Ángulo de la cámara?
        self.angulo = 0.0

        # giro con maus
        self.arrastrando = False
        self.ultimo_mouse_x = 0

        # cambio
        self.redibujar_callback = None

        # click maus
        self.canvas.bind("<ButtonPress-1>", self.iniciar_arrastre)
        self.canvas.bind("<B1-Motion>", self.mover_camara)
        self.canvas.bind("<ButtonRelease-1>", self.terminar_arrastre)

        # Cuando cambia el tamaño de la ventana
        self.canvas.bind("<Configure>", self.redimensionar)
   
    # CONEXIÓN CON MAIN

    def establecer_callback(self, callback):
        """
        Permite que main.py le diga a la cabina
        qué función debe ejecutar cuando cambie la cámara.
        """
        self.redibujar_callback = callback

    # CÁMARA
   
    def iniciar_arrastre(self, evento):
        self.arrastrando = True
        self.ultimo_mouse_x = evento.x

    def mover_camara(self, evento):

        if not self.arrastrando:
            return

        diferencia = evento.x - self.ultimo_mouse_x

        self.angulo += diferencia * 0.8

        self.angulo %= 360

        self.ultimo_mouse_x = evento.x

        if self.redibujar_callback:
            self.redibujar_callback()

    def terminar_arrastre(self, evento):
        self.arrastrando = False

    def redimensionar(self, evento):

        if self.redibujar_callback:
            self.redibujar_callback()

    # PROYECCIÓN 3D
    
    def proyectar(self, x, y, z):

        ancho = self.canvas.winfo_width()
        alto = self.canvas.winfo_height()

        # Convertir ángulo a radianes
        rad = math.radians(self.angulo)

        # Rotación horizontal alrededor del eje Y
        xr = x * math.cos(rad) - z * math.sin(rad)
        zr = x * math.sin(rad) + z * math.cos(rad)

        # Distancia para perspectiva
        distancia = 20 + zr

        if distancia < 2:
            distancia = 2

        escala = 440 / distancia

        # Centro de la pantalla
        pantalla_x = ancho / 2 + xr * escala
        pantalla_y = alto / 2 - y * escala

        return pantalla_x, pantalla_y, zr

    
    # CUBOS 3D
    
    def cubo(self, x, y, z, ancho, alto, profundidad, color):

        # Mitades
        hx = ancho / 2
        hy = alto / 2
        hz = profundidad / 2

        # 8 vértices del cubo
        vertices = [
            (x - hx, y - hy, z - hz),
            (x + hx, y - hy, z - hz),
            (x + hx, y + hy, z - hz),
            (x - hx, y + hy, z - hz),

            (x - hx, y - hy, z + hz),
            (x + hx, y - hy, z + hz),
            (x + hx, y + hy, z + hz),
            (x - hx, y + hy, z + hz)
        ]

        # Caras del cubo
        caras = [
            (0, 1, 2, 3),
            (4, 5, 6, 7),
            (0, 1, 5, 4),
            (2, 3, 7, 6),
            (1, 2, 6, 5),
            (0, 3, 7, 4)
        ]

        caras_proyectadas = []

        for cara in caras:

            puntos = []

            profundidad_promedio = 0

            for indice in cara:

                px, py, pz = self.proyectar(*vertices[indice])

                puntos.append((px, py))
                profundidad_promedio += pz

            profundidad_promedio /= len(cara)

            caras_proyectadas.append(
                (profundidad_promedio, puntos)
            )

        # Dibujar primero las caras más lejanas
        caras_proyectadas.sort(
            key=lambda elemento: elemento[0],
            reverse=True
        )

        for _, puntos in caras_proyectadas:

            coordenadas = []

            for punto in puntos:
                coordenadas.extend(punto)

            self.canvas.create_polygon(
                coordenadas,
                fill=color,
                outline="#202028"
            )

    
    # LÍNEAS 3D
    

    def linea_3d(
        self,
        x1, y1, z1,
        x2, y2, z2,
        color="#777777",
        ancho=2
    ):

        px1, py1, _ = self.proyectar(x1, y1, z1)
        px2, py2, _ = self.proyectar(x2, y2, z2)

        self.canvas.create_line(
            px1,
            py1,
            px2,
            py2,
            fill=color,
            width=ancho
        )

    
    # CABINA
    
    def dibujar_cabina(self):

       
        # PISO
        

        self.cubo(
            0,
            -2.5,
            0,
            14,
            0.3,
            8,
            "#45454f"
        )

       
        # TECHO
        

        self.cubo(
            0,
            5,
            0,
            14,
            0.25,
            8,
            "#35353d"
        )

        
        # PARED LATERAL IZQUIERDA
        
        self.cubo(
            0,
            1.25,
            -4,
            14,
            7.5,
            0.25,
            "#292932"
        )

      
        # PARED LATERAL DERECHA
        
        self.cubo(
            0,
            1.25,
            4,
            14,
            7.5,
            0.25,
            "#292932"
        )

        # PARED DEL FONDO
        

        self.cubo(
            7,
            1.25,
            0,
            0.25,
            7.5,
            8,
            "#24242c"
        )

       
        # RIELES
        
        # intento de riel izquierdo
        self.linea_3d(
            -6.3,
            -2.15,
            -1.5,
            6.3,
            -2.15,
            -1.5,
            "#9b9ba5",
            5
        )

        # Riel derecho
        self.linea_3d(
            -6.3,
            -2.15,
            1.5,
            6.3,
            -2.15,
            1.5,
            "#9b9ba5",
            5
        )

        # Línea central de referencia
        self.linea_3d(
            -6.3,
            -2.28,
            0,
            6.3,
            -2.28,
            0,
            "#555560",
            1
        )